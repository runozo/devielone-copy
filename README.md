# devielone-copy

Copies a list of files listed in a csv file, from a source directory to a destination directory.

## Usage

```
devielone_copy.py [-h] [-N N] [-S S] [-E E] csv_file source_path destination_path


positional arguments:
  csv_file          a csv file with a list of file names to be copied
  source_path       the source path to copy the files
  destination_path  the destination path to copy the files

optional arguments:
  -h, --help        show this help message and exit
  -N N              the number of the column where the file names are stored,
                    default: "0"
  -S S              the separator for the columns of the csv file, default: ";"
  -E E              the file extension
```
