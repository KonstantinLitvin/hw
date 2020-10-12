import hashlib
from collections import defaultdict
from pathlib import Path
from pprint import pprint

tmp_dir = '../tests/tmp'


def get_hash(path_to_file: Path) -> str:
    with open(path_to_file, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()


def find_duplicates(path, check_mode=True):
    p = Path(path)

    hs = defaultdict(list)
    for f in p.iterdir():
        h = get_hash(f)
        hs[h].append(f)
        print(f"f: {f}, {h}")
    pprint(hs)

    for k, v in hs.items():
        print(k)
        fn_original: Path = v.pop()
        print(f"fn_original: {fn_original}")
        while (l := len(v)) > 0:
            fn: Path = v.pop()

            # print(f"fn: {fn}")
            # fn.unlink()
            print(fn_original.samefile(fn))
        print(v)
        print()
