[![PyPI version](https://badge.fury.io/py/FileChunkCRUD.svg)](https://badge.fury.io/py/FileChunkCRUD)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/filechunkcrud)](https://pepy.tech/project/filechunkcrud)

# FileChunkCRUD

`FileChunkCRUD` is a Python tool designed for Create, Read, Update, and Delete operations on files, especially large files that need to be processed in chunks to fit into memory constraints.

## Installation

To install `FileChunkCRUD`, you can use pip:

```bash
pip install FileChunkCRUD
```

## Usage

### As a Python Module

`FileChunkCRUD` can be used as a Python module in your scripts for handling large file operations.

Example:

```python
from filechunkcrud import FileHandler

file_path = '/path/to/your/largefile.txt'

# Initialize the file handler with the target file path
file_handler = FileHandler(file_path)

# Example of reading file in chunks
for chunk in file_handler.read_chunks(chunk_size=1024):  # chunk_size in bytes
    print(chunk)
...
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/chigwell/FileChunkCRUD/issues).

## License


[MIT](https://choosealicense.com/licenses/mit/)