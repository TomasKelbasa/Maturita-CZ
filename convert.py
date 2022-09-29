#!/usr/bin/env python3

import subprocess
from glob import glob
import os

# go through markdown files in the current directory
for file_path in glob("./díla/*.md"):
    file_name = file_path.split("/")[-1]

    # skip README.md
    if file_name == "README.md":
        continue

    # create the pandoc command
    command = 'pandoc "%s" -o "%s" -V %s' % (file_path,
                                             "pdf_output/%s.pdf" % file_name[:-3],
                                             "geometry:margin=1.5cm")

    # execute the command
    os.system(command)
