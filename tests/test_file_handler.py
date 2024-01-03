import unittest
import os
from filechunkcrud import FileHandler

class TestFileHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Создание временного файла для тестирования
        cls.test_file_path = "test_file.txt"
        with open(cls.test_file_path, "w") as file:
            file.write("Hello, World!\nThis is a test file.")

    @classmethod
    def tearDownClass(cls):
        # Удаление временного файла после тестирования
        os.remove(cls.test_file_path)

    def test_read_chunks(self):
        file_handler = FileHandler(self.test_file_path)
        content = ""
        for chunk in file_handler.read_chunks(chunk_size=5):
            content += chunk
        self.assertEqual(content, "Hello, World!\nThis is a test file.")

    def test_create_file(self):
        new_file_path = "new_test_file.txt"
        file_handler = FileHandler(new_file_path)
        file_handler.create_file("New content")
        with open(new_file_path, "r") as file:
            content = file.read()
        self.assertEqual(content, "New content")
        os.remove(new_file_path)  # Удаление файла после теста

    def test_update_file(self):
        file_handler = FileHandler(self.test_file_path)
        file_handler.update_file("\nAdditional content")
        with open(self.test_file_path, "r") as file:
            content = file.read()
        self.assertTrue("Additional content" in content)

    def test_delete_file(self):
        temp_file_path = "temp_file.txt"
        with open(temp_file_path, "w") as file:
            file.write("Temporary file.")
        file_handler = FileHandler(temp_file_path)
        file_handler.delete_file()
        self.assertFalse(os.path.exists(temp_file_path))

if __name__ == '__main__':
    unittest.main()
