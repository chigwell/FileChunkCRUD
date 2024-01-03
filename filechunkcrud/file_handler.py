class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_chunks(self, chunk_size=1024):
        """Read large file in chunks with given size."""
        with open(self.file_path, 'r') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk

    def create_file(self, content):
        """Create a new file with the given content."""
        with open(self.file_path, 'w') as file:
            file.write(content)

    def update_file(self, content):
        """Update an existing file with the given content."""
        with open(self.file_path, 'a') as file:
            file.write(content)

    def delete_file(self):
        """Delete the file."""
        import os
        os.remove(self.file_path)
