# devielone-copy

Copies a list of files read from a csv-like file, from a source directory to a destination directory.

## Usage

```
devielone_copy.py [-h] [-N N] [-S S] [-E E] csv_file source_path destination_path

Copies files listed in a csv file.

positional arguments:
  csv_file          a csv file with a list of file names to be copied
  source_path       the source path to copy the files from
  destination_path  the destination path to copy the files

optional arguments:
  -h, --help        show this help message and exit
  -N N              the column number in which the file names are present,
                    default: 0
  -S S              the separator for the columns of the csv file, default:
                    ";"
  -E E              the source files extension, default: "csv"

```
