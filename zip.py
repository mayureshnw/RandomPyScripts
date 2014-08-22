#!/usr/bin/env python3
import sys
import os
import argparse
from zipfile import ZipFile

#open a zipfile object(e.g. zippy) and add the files,provided in the argument to it
def zf(archive, inpfile):
    zippy = ZipFile(archive,mode = 'w')
    for i in inpfile:
        zippy.write(i, os.path.basename(i))
    zippy.close()
    print('zip archive created')
    sys.exit()

def main():
    #force the zip creation with --f using argparse
    parser = argparse.ArgumentParser(description="create a zip archive with given files")
    parser.add_argument("-f", "--force", help="create zip file forcefully without prompting the user even if the file already exists", action="store_true")
    parser.add_argument("out", help="output archive")
    parser.add_argument("inp", help="input files", nargs='+')

    #assign variables to pass in functions
    args = parser.parse_args()
    archive = sys.argv[1]
    inps = args.inp

    #exit if wrong no. of arguments are passed
    if len(sys.argv) < 3:
        print("wrong number of arguments")
        sys.exit(1)

    #force the creation of archive if "--force" is passed
    if args.force:
        zf(archive, inps)

    #check if the file already exists and ask the user for further instructions
    if os.path.exists(archive):
        print("file already exists")
        print("Do you want to overwrite it?\nEnter yes or no")
        ans = input()
        if ans == 'yes':
            zf(archive, inps)
        else:
            sys.exit(1)

    #create the zip file if it doesn't exist
    zf(archive,inps)

#main()
if __name__ == '__main__':
    main()