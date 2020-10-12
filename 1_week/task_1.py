import hashlib
import random
import string
import tempfile
import pathlib
from collections import defaultdict
from pathlib import Path
from pprint import pprint
from typing import List
import os

tmp_dir = 'tmp'


def get_hash(path_to_file: Path) -> str:
    with open(path_to_file, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()


class Test:
    files: List[str] = []

    @staticmethod
    def get_content(k=100) -> bytes:
        return str.encode(''.join(random.choices(string.ascii_uppercase + string.digits, k=k)))

    @staticmethod
    def generate_test_files(n: int = 100) -> None:
        """
        Generate n files with random content. Each even file is duplicate of the previous file
        :param n: files number
        """
        content = Test.get_content()

        for i in range(n):

            if i % 2 == 0:
                content = Test.get_content()
            file = tempfile.NamedTemporaryFile(dir=tmp_dir, delete=False)
            file.write(content)
            file.flush()

            Test.files.append(file.name)

            file.close()


Test.generate_test_files()

p = Path('tmp')

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
