# os allows OS-level changes
import os
from datetime import date

# list of programs available
programs = ["1. After Hours", "2. Alternative Content", "3. Essentials,", "4. Family Day on Aragon", "5. Main Features", "6. National Theatre Live"]
print programs
selected_program = raw_input("Select a program: ")

if selected_program == "1":
	prog_dir = programs[0]
elif selected_program == "2":
	prog_dir = programs[1]
elif selected_program == "3":
	prog_dir = programs[2]
elif selected_program == "4":
	prog_dir = programs[3]
elif selected_program == "5":
	prog_dir = programs[4]
elif selected_program == "6":
	prog_dir = programs[5]
else:
	print("Please choose a program.")

#get current year for directory
year_dir = str(date.today().year)

# prompt user for movie directory
mov_dir = raw_input("Select a movie: ")

#prompt user for folder containing photos
photo_dir = raw_input("Location of photos: ")

# prompt user for desired filename
d_name = raw_input("Enter desired filename: ")

# counter used for file number suffix, e.g., file_1, file_2, etc.
num_suffix = 1

# variable containing final path to files; the first argument will never change as this is the highest-level common directory.
# Coral Gables Art Cinema/Programming/Main Features/Top Five
base_path = os.path.join("M:/Coral Gables Art Cinema/Programming/", prog_dir[3:], year_dir, mov_dir, photo_dir)

# renaming occurs here
for photo in os.listdir(base_path):
	if photo.endswith('.jpg', '.jpeg', '.png')
	f_name = d_name + '_' + str(num_suffix) + '.jpg'
	os.rename(os.path.join(base_path, photo), os.path.join(base_path, f_name))
	num_suffix = num_suffix + 1