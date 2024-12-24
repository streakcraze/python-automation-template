# My Automation Project

This project is designed to automate various tasks using Python scripts and utilities. Specifically, it copies files from a source directory to a destination directory as defined in `directories.txt`.

## Project Structure

```
my-automation-project
├── src
│   ├── main.py          # Entry point of the automation project
│   ├── utils
│   │   └── helpers.py   # Utility functions for scripts
│   └── scripts
│       └── example_script.py  # Example automation script
├── requirements.txt     # Project dependencies
├── directories.txt      # Source and destination directories
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-automation-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Define the source and destination directories in `directories.txt`:
   ```
   source_directory=/path/to/source
   destination_directory=/path/to/destination
   ```

## Usage

To run the automation project, execute the main script:
```
python src/main.py
```

The script will read the directories from `directories.txt` and copy files from the source directory to the destination directory.

For more specific usage of individual scripts, refer to their respective documentation within the script files.