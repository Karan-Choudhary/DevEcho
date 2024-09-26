# DevEcho

This Python project is designed to translate voice commands into system operations. The assistant supports a variety of common tasks such as directory creation, file handling, process management, and project templating for machine learning and general projects.

## Features

The assistant can interpret the following commands:

| **Command**              | **System Operation**            |
|--------------------------|---------------------------------|
| `make a directory 'directory name'`                          | Creates a new directory (`mkdir`) |
| `create a file 'filename'`                                               | Creates a new file (`touch`)     |
| `kill 'process_name'`                                                    | Terminates a process (`pkill`)   |
| `delete 'directory name or file name'`                      | Deletes a file or directory (`rm`) |
| `show stats`                                                                   | Shows file or directory stats (`stat`) |
| `start a machine learning project 'project name'` | Creates a machine learning project template |
| `start a general project 'project name'`                   | Creates a general project template |

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
2. Navigate to the project directory:
   ```bash
   cd your-repo-name
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python -m src.pipeline
   ```

## Contributing
Feel free to fork this repository, make your changes, and create a pull request. Any contributions are welcome!