import os
import glob
import zipfile
import shutil
import random

def main():
	#inital path is use~ + "nbs" name of directory for notebooks
	# this is were script should be saved.
	nbs_dir = os.path.join(os.path.expanduser("~"),"nbs")
	data_dir = os.path.join(nbs_dir,"data")
	redux_dir = os.path.join(data_dir,"dogs-vs-cats-redux")
	train_dir = os.path.join(redux_dir,"train")
	test_dir = os.path.join(redux_dir,"test")
	test_dir_1=os.path.join(test_dir,"unknown")
	validate_dir = os.path.join(redux_dir,"validate")
	sample_dir = os.path.join(redux_dir,"sample")
		
	if not os.path.exists(nbs_dir):
		os.makedirs(nbs_dir)	
	if not os.path.exists(data_dir):
		os.makedirs(data_dir)	
	if not os.path.exists(redux_dir):
		os.makedirs(redux_dir)
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)	
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)	
	if not os.path.exists(test_dir_1):
		os.makedirs(test_dir_1)		
		
	if not os.path.exists(validate_dir):
		os.makedirs(validate_dir)	
	if not os.path.exists(sample_dir):
		os.makedirs(sample_dir)	
		
# unzip files onto train folder
	with zipfile.ZipFile(os.path.join(data_dir,'train.zip'), "r") as z:
		z.extractall(redux_dir)
#unzip files onto test folder
	with zipfile.ZipFile(os.path.join(data_dir,'test.zip'), "r") as z:
		z.extractall(redux_dir)
	
	test_files=glob.glob(test_dir+'/*.*')
	for files in test_files:
		shutil.copy2(files,test_dir_1)
		os.remove(files)
	
	
	# create and split between dogs and cats under train folder
	separate_cats_dogs(train_dir)
	# create validation sctructure
	split_train_validate_files(os.path.join(train_dir,"dogs"),os.path.join(validate_dir,"dogs"),.8,True)	
	split_train_validate_files(os.path.join(train_dir,"cats"),os.path.join(validate_dir,"cats"),.8,True)	
	#create sample structure
	split_train_validate_files(os.path.join(train_dir,"dogs"),os.path.join(sample_dir,"train","dogs"),.95,False)	
	split_train_validate_files(os.path.join(validate_dir,"dogs"),os.path.join(sample_dir,"validate","dogs"),.95,False)	
	split_train_validate_files(os.path.join(train_dir,"cats"),os.path.join(sample_dir,"train","cats"),.95,False)	
	split_train_validate_files(os.path.join(validate_dir,"cats"),os.path.join(sample_dir,"validate","cats"),.95,False)	
		

def separate_cats_dogs(train_dir):
	train_dogs_dir = os.path.join(train_dir,"dogs")
	train_cats_dir = os.path.join(train_dir,"cats")
	if not os.path.exists(train_dogs_dir):
		os.makedirs(train_dogs_dir)
	if not os.path.exists(train_cats_dir):
		os.makedirs(train_cats_dir)
	dogs =glob.glob(train_dir+'/d*.*')
	cats =glob.glob(train_dir+'/c*.*')
			
	for file in dogs:
		shutil.copy2(file,train_dogs_dir)
		os.remove(file)
	for file in cats:
		shutil.copy2(file,train_cats_dir)
		os.remove(file)


def split_train_validate_files(source,destination, ratio,remove):
	""" need to specify train path, validation path and ratio """
	if not os.path.exists(destination):
		os.makedirs(destination)
	file_list=glob.glob(source+'/*.*')
	random.shuffle(file_list)
	# select subset of list
	destination_list = file_list[int(len(file_list)*ratio):]
	for file in destination_list:
		shutil.copy2(file,destination)
		if remove:
			os.remove(file)
	
	
		
if __name__ =="__main__":
	main()
	
	