import time
from os import listdir, stat
from shutil import copyfile
from stat import ST_MTIME

files_in_a = []
files_in_b = []


def check_path(p):
	if p == '':
		raise Exception('Path can`t be empty')
	return p

def push_file(dir_list, files_list):
	for file in dir_list:
		files_list.append(file)

def compare(files_in_a, files_in_b, variant, path_a, path_b, path_log):
	if variant == 1:
		f_1, f_2 = files_in_a, files_in_b
	else:
		f_1, f_2 = files_in_b, files_in_a
		path_a, path_b = path_b, path_a
	for file in f_1:
		if file in f_2:
			path_a_f = path_a+'/'+f_1[f_1.index(file)]
			path_b_f = path_b+'/'+f_2[f_2.index(file)]
			time_a = time.asctime(time.localtime(stat(path_a_f)[ST_MTIME]))
			time_b = time.asctime(time.localtime(stat(path_b_f)[ST_MTIME]))

			if time_a > time_b:
				f_l = open(path_log, 'a')
				copyfile(path_a_f, path_b_f)
				text = 'Modified: ' + path_a_f + ' -> ' + path_b_f + '\n'
				f_l.write(text)
				f_l.close()
			else:
				f_l = open(path_log, 'a')
				copyfile(path_b_f, path_a_f)
				text = 'Modified: ' + path_b_f + ' -> ' + path_a_f + '\n'
				f_l.write(text)
				f_l.close()
		else:
			path_a_f = path_a+'/'+f_1[f_1.index(file)]
			path_b_create = path_b+'/'+f_1[f_1.index(file)]
			f_l = open(path_log, 'a')
			copyfile(path_a_f, path_b_create)
			text = 'Created: ' + path_a_f + ' in ' + path_b_create + '\n'
			f_l.write(text)
			f_l.close()

path_a = input('Input path folder A: ')
path_a = check_path(path_a)
path_b = input('Input path folder B: ')
path_b = check_path(path_b)
variant = int(input('From A to B(1) or from B to A(2). Input number: '))
path_log = input('Input path for log-file: ')
path_log = check_path(path_log)


path_log += '/log.txt'
f = open(path_log, 'w')
f.write('')
f.close()

dir_list_a = listdir(path_a)
dir_list_b = listdir(path_b)

push_file(dir_list_a, files_in_a)
push_file(dir_list_b, files_in_b)

compare(files_in_a, files_in_b, variant, path_a, path_b, path_log)
