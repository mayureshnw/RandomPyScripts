# finds duplicate files

import os
import argparse

def get_files(dir_name):
	files = []
	for a,b,c in list(os.walk('.')):
		files += c
	return files

def check_same(f1,f2):
	same = True
	for a,b in zip(f1,f2):
		if a!=b:
			same = False
			break
	return same

def get_size(f):
    f.seek(0,2)
    size = f.tell()
    return size

def find_dup(dirName):
	files = get_files(dirName)
	total_files = len(files)
	dup_list = []
	for i in range(total_files):
		for j in range(i,total_files):

			file1 = files[i]
			file2 = files[j]

			if file1==file2:
				continue

			try:
				f1 = open(file1)
				f2 = open(file2)
			except:
				continue

			if get_size(f1)==get_size(f2):
				if check_same(f1,f2):
					dup_list.append((file1,file2))

	return dup_list

if __name__=='__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("-dir", help="directory name",type=str)
	args = parser.parse_args()

	if args.dir==None:
		dirName = '.'
	else:
		dirName = args.dir

	dup_list = find_dup(dirName)
	print("Duplicate files : ")
	for file1,file2 in dup_list:
		print(file1," & ",file2)
