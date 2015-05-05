#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from shutil import copyfile
from os import path

parser = argparse.ArgumentParser(description='Copies files listed in a csv file.', epilog="© 2015 Cesare Ghirelli")
parser.add_argument(
    'csv_file', type=str, help='a csv file with a list of file names to be copied')
parser.add_argument(
    '-N', type=int, help='the number of the column where the file names are stored, default: 0', default=0, required=False)
parser.add_argument(
    '-S', type=str, help='the separator for the columns of the csv file, default: ";"', default=';', required=False)
parser.add_argument(
    '-E', type=str, help='the source files extension, default: "pdf"', default='pdf', required=False)
parser.add_argument(
    'source_path', type=str, help='the source path to copy the files')
parser.add_argument(
    'destination_path', type=str, help='the destination path to copy the files')


args = parser.parse_args()

with open(args.csv_file, 'r') as csv:
    for line in csv:
        filename = line.split(args.S)[args.N] + '.' + args.E
        print('Copying %s to %s', (path.join(args.source_path, filename),
                                   path.join(args.destination_path, filename)))
        copyfile(path.join(args.source_path, filename),
                 path.join(args.destination_path, filename))
