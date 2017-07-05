import os
import datetime
import re
import shutil

#current date
a = datetime.datetime(2017,1,1)
#destination folder
dest = r"E:\User\NUS\Year 4\SEM2"
#list each file in directory
source = os.listdir(r"E:\User\Downloads")
#prefix for later on
paths = r"E:\User\Downloads\\"
for each in source:
	#get the creation time
	c = os.path.getctime(paths+each)
	#convert creation time to string
	x = datetime.datetime.fromtimestamp(c).strftime('%Y-%m-%d %H:%M:%S')
	#convert to datetime
	b = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
	#if creation time after a
	if (b > a):
		#check regex match Tutorial_x
		regex = 'Tutorial_(.+?)'
		if(re.match(regex, each)) or (re.match('Lecture_(.+?)', each)):
			print(each)
			shutil.move(paths + each, dest + r"\CS2105")

		regex2 = '2017_tutorial(.+?)'
		if (re.match(regex2, each)):
			print(each)
			shutil.move(paths + each, dest + r"\CS2107")

		regex3 = 'Session(.+?)'
		if (re.match(regex3, each)):
			print(each)
			shutil.move(paths+each, dest + r"\NETWORKS")