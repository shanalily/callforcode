import numpy as np
import os
import csv

all_counts = 0
IDS = set()

class Data:

	def __init__(self):

		self.data = {}

	def inputData(self, header, data):

		for i in range(len(header)):

			if data[i] == "":
				continue

			elif header[i] == "EPISODE_NARRATIVE" or header[i] == "EVENT_NARRATIVE":
				continue

			else:
				self.data[header[i]] = data[i]

	def merge(self, other):

		for item in other.data.keys():
			self.data[item] = other.data[item]



class DataContainer:

	def __init__(self):

		self.titles = set()
		self.dataList = {}

	def addData(self, header, dataObj, ID):

		headerSet = set(header)

		if ID in self.dataList.keys():
			#print("Merging")
			self.dataList[ID].merge(dataObj)

		else:
			self.dataList[ID] = dataObj

		for item in headerSet:
			self.titles.add(item)


	def outputData(self):

		outputfil = open("output.csv", "w")
		headerString = ""
		for item in self.titles:
			headerString += item + ","

		headerString.rstrip(",")
		outputfil.write(headerString+"\n")

		for item in self.dataList:

			line = ""
			for title in self.titles:
				if title in self.dataList[item].data.keys():
					line += self.dataList[item].data[title].strip()

				line += ","

			line.rstrip(",")
			outputfil.write(line+"\n")

		outputfil.close()

if __name__ == "__main__":

	counter = 0
	all_data = DataContainer()

	for file in os.listdir("."):

		if file == "output.csv":
			continue

		first_line = None
		i = -1
		j = -1
		if file.split(".")[-1] == "csv":

			with open(file) as csvfil:
				csvreader = csv.reader(csvfil, delimiter = ",", quotechar="\"")
				#print(csvreader)
				#first_line = None
				for line in csvreader:
					all_counts += 1
					#print(line)
					if first_line == None:
						#print(line)
						first_line = line

					else:

						try:
							i = first_line.index("EVENT_TYPE")
						except ValueError:
							i = -1

						try:
							j = first_line.index("EPISODE_ID")
						except ValueError:
							j = -1

						IDS.add(line[j])
						if i == -1 or j == -1:
							break
						else:

							if line[i].lower().strip() == "hurricane (typhoon)":
								one_line = Data()
								one_line.inputData(first_line, line)
								all_data.addData(first_line, one_line, line[j])

								counter += 1
								if counter % 10000 == 0:
									print(counter)

	all_data.outputData()
	print(all_counts, len(list(IDS)))
	print(counter)