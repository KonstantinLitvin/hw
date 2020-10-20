import random
import string
import tempfile
from pathlib import Path
from typing import List
from week_1 import task_1
from config import project_root, get_logger


logger = get_logger(__name__)

tmp_path = Path(project_root, 'tests', 'tmp')


class Test:
    files: List[str] = []

    @staticmethod
    def __get_content(k=100) -> bytes:
        return str.encode(''.join(random.choices(string.ascii_uppercase + string.digits, k=k)))

    @staticmethod
    def generate_test_files(files_n: int = 100) -> None:
        """
        Generate n files with random content. Each even file is duplicate of the previous one
        :param files_n: files number
        """
        content = Test.__get_content()

        for i in range(files_n):

            if i % 2 == 0:
                content = Test.__get_content()
            file = tempfile.NamedTemporaryFile(dir=tmp_path, delete=False)
            file.write(content)
            file.flush()

            Test.files.append(file.name)

            file.close()
        logger.info('files generated')


Test.generate_test_files(files_n=10)
input('We`ve just generated test files in tmp directory...')

# 2. Check the duplicates number...
task_1.find_duplicates(tmp_path, check_mode=True)

# 3. Remove the duplicates and create hardlinks
task_1.find_duplicates(tmp_path, check_mode=False)

# 4. Check one more time for the duplicated files
task_1.find_duplicates(tmp_path, check_mode=True)
