#create directory structure starting from current place


import os
import glob
import zipfile
import shutil
import random



def main():
	current_dir = os.getcwd()
	directory = current_dir +"/data/dogs-vs-cats-redux"
	train_path = os.path.join(directory,"train")
	test_path = os.path.join(directory,"test")
	validate_path = os.path.join(directory,"validate")
	print directory
	if not os.path.exists(directory):
		os.makedirs(directory)
	if not os.path.exists(train_path):
		os.makedirs(train_path)	
	if not os.path.exists(test_path):
		os.makedirs(test_path)	
	if not os.path.exists(validate_path):
		os.makedirs(validate_path)	
		
# unzip files onto train folder
	with zipfile.ZipFile('train.zip', "r") as z:
		z.extractall(directory)
#unzip files onto test folder
	with zipfile.ZipFile('test.zip', "r") as z:
		z.extractall(directory)

	split_train_validate_files(train_path,validate_path,.8)		
#copy ratio from train folder to validate folder		

def split_train_validate_files(train_path,validate_path, ratio):
	""" need to specify train path, validation path and ratio """
	file_list=glob.glob(train_path+'/*.*')
	random.shuffle(file_list)
	print "file count",len(file_list)
	print "second index", int(len(file_list)*ratio)
	#train_data = data[:50]
	validate_list = file_list[int(len(file_list)*ratio):]
	#print file_list
	for file in validate_list:
		shutil.copy2(file,validate_path)
		os.remove(file)
	
	
		
if __name__ =="__main__":
	main()
	
	