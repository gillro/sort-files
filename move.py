import shutil
import os

source = os.listdir(r"C:\Users\user\Desktop")
dest = r"E:\User\NUS\Year 4\SEM2"

for files in source: 
	if ("2103" in files) or ("addressbook" in files):
		shutil.move(r"C:\Users\user\Desktop\\" + files, dest + r"\CS2103")
	if ("2107" in files) or ("ssl" in files.lower()):
		shutil.move(r"C:\Users\user\Desktop\\" + files, dest + r"\CS2107")
	if ("2105" in files):
		shutil.move(r"C:\Users\user\Desktop\\" + files, dest + r"\CS2105")
	if ("yakuza" in files.lower()):
		shutil.move(r"C:\Users\user\Desktop\\" + files, dest + r"\NETWORKS")

sources = os.listdir(r"E:\User\Downloads")

for files2 in sources:
	if ("2103" in files2) or ("addressbook" in files2) or ("whatsleft" in files2.lower()):
		shutil.move(r"E:\User\Downloads\\" + files2, dest + r"\CS2103")
	if ("2107" in files2) or ("ssl" in files.lower()):
		shutil.move(r"E:\User\Downloads\\" + files2, dest + r"\CS2107")
	if ("2105" in files2):
		shutil.move(r"E:\User\Downloads\\" + files2, dest + r"\CS2105")
	if ("yakuza" in files2.lower()):
		shutil.move(r"E:\User\Downloads\\" + files2, dest + r"\NETWORKS")
