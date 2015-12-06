# os allows OS-level changes
import os

# prompt user for desired filename
d_name = raw_input("Enter desired filename: ")

# counter used for file number suffix, e.g., file_1, file_2, etc.
num_suffix = 1

# variable containing final path to files; the first argument will never change as this is the highest-level common directory.
base_path = os.path.join("/home/javier/Coding Projects/Rename-Photos/test photos")

# renaming occurs here
for photo in os.listdir(base_path):
	if photo.endswith('.jpg', '.jpeg', '.png'):
		f_name = d_name + '_' + str(num_suffix) + '.jpg'
		os.rename(os.path.join(base_path, photo), os.path.join(base_path, f_name))
		num_suffix = num_suffix + 1
	else:
		print "Can't run."