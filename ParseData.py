import os

for file in os.listdir("."):

	if file.split(".")[-1] == "gz":

		print(file)
		os.system("gunzip {}".format(file))