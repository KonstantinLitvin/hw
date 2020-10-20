import hashlib
import logging
from collections import defaultdict
from pathlib import Path
from pprint import pprint
from config import get_logger

logger = get_logger(__name__)


def get_hash(path_to_file: Path) -> str:
    with open(path_to_file, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()


def find_duplicates(path: str, check_mode=True):
    path = Path(path)

    hashes = defaultdict(list)
    for f in path.iterdir():
        h = get_hash(f)
        hashes[h].append(f)
        logger.debug(f"file: {f}, hash: {h}")

    pprint(f"hashes: {hashes}")
    for k, v in hashes.items():
        fn_original: Path = v.pop()
        logger.info(f"fn_original: {fn_original}")
        while (l := len(v)) > 0:
            fn: Path = v.pop()
            logger.info(f"fn: {fn}")
            if check_mode:
                logger.info(f'files with the same hash the same?: {fn_original.samefile(fn)}')
            else:
                logger.info(f"fn: {fn}")
                fn.unlink()
                fn_original.link_to(fn)
