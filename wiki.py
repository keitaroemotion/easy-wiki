#!/usr/bin/env python

from numpy.random import randint 

import glob
import os
import ntpath
import sys

title    = ""
wiki_dir = "/usr/local/etc/wiki"

if(not os.path.isdir(wiki_dir)):
    os.mkdir(wiki_dir)

def get_matching_files():
    regex = "*".join(sys.argv[2:])
    return [f for f in glob.glob("{}**/*{}*".format(wiki_dir, regex))]

def get_files():
    return [f for f in glob.glob("{}**/*".format(wiki_dir))]
 
if(len(sys.argv) < 2):
    title = raw_input("wiki title: ")
else:
    if  (sys.argv[1].startswith("-")):
        option = sys.argv[1]
        if  (option == "-h"):
            print
            print("wiki -h              ... show help menu")
            print("wiki -ls [kw1] [kw2] ... enlist pages with key words")
            print("wiki -ra             ... randomly show articles")
            print

        elif(option == "-ra"):
            files = get_files()            
            os.system("vim {}".format(files[randint(len(files))]))

        elif(option == "-rm"):
            for file in get_matching_files():
                os.remove(file)
                print "\ndeleted: {}\n".format(ntpath.basename(file))

        elif(option == "-ls"):
            for file in get_matching_files():
                print ntpath.basename(file)

        sys.exit()

    title = '_'.join(sys.argv[1:])

title = title.replace(" ", "_")
os.system("vim {}/{}".format(wiki_dir, title))

print(title)
