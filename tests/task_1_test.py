import random
import string
import tempfile
from typing import List
from week_1 import task_1

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
            file = tempfile.NamedTemporaryFile(dir='./tmp', delete=False)
            file.write(content)
            file.flush()

            Test.files.append(file.name)

            file.close()


Test.generate_test_files()

task_1.find_duplicates()