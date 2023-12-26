#!/usr/bin/python3

import os
path = input("Enter a file or directory path: ")

print(f"Checking {path} type: " )

if os.path.isdir(path):
	print(f"{path} is a directory")
elif os.path.isfile(path):
	print(f"{path} is a file")
else:
	print(f"{path} does not exists")
