#!/usr/bin/env python

import glob
import os
import ntpath
import sys

title    = ""
wiki_dir = "/usr/local/etc/wiki"

if(not os.path.isdir(wiki_dir)):
    os.mkdir(wiki_dir)

if(len(sys.argv) < 2):
    title = raw_input("wiki title: ")
else:
    if(sys.argv[1] == "-ls"):
        files = [f for f in glob.glob(wiki_dir + "**/*")]
        for file in files:
            print ntpath.basename(file)

        sys.exit()

    title = '_'.join(sys.argv[1:])

title = title.replace(" ", "_")
os.system("vim {}/{}".format(wiki_dir, title))

print(title)
