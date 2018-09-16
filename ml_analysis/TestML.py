from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
import csv
import random

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def extract_features(all_data):

	final_data = []
	final_data.append(all_data[8])
	final_data.append(all_data[17])
	final_data.append(all_data[22])
	final_data.append(all_data[34])
	final_data.append(all_data[12])
	final_data.append(all_data[14])
	final_data.append(all_data[37])
	final_data.append(all_data[33])
	final_data.append(all_data[28])
	final_data.append(all_data[13])
	final_data.append(all_data[10])
	final_data.append(all_data[11])
	final_data.append(all_data[3])
	final_data.append(all_data[50])

	return np.array(final_data)


def clean_data(final_data):

	final_final_data = []

	for i in range(len(final_data[0])):

		if final_data[0][i].strip() == "":
			continue
		if final_data[1][i].strip() == "":
			final_data[1][i] = 0
		if final_data[2][i].strip() == "":
			final_data[2][i] = 0
		if final_data[3][i].strip() == "":
			final_data[3][i] = 0
		if final_data[4][i].strip() == "":
			final_data[4][i] = 0
		if final_data[5][i].strip() == "":
			final_data[5][i] = 0
		if final_data[6][i].strip() == "":
			final_data[6][i] = 0
		if final_data[7][i].strip() == "":
			continue
		if final_data[8][i].strip() == 0:
			continue #make avg?
		if final_data[9][i].strip() == "":
			continue
		if final_data[10][i].strip() == "":
			continue
		if final_data[11][i].strip() == "":
			continue
		if final_data[12][i].strip() == "":
			continue
		if final_data[13][i].strip() == "":
			continue

		final_data[0][i] = months.index(final_data[0][i])
		final_final_data.append(final_data[:,i])

	for i in range(len(final_final_data)):

		if final_final_data[i][5][-1] == "K":

			if len(final_final_data[i][5]) == 1:
				final_final_data[i][5] = 1000
			else:
				final_final_data[i][5] = float(final_final_data[i][5][:len(final_final_data[i][5])-1]) * 1000

		elif final_final_data[i][5][-1] == "M":
			final_final_data[i][5] = float(final_final_data[i][5][:len(final_final_data[i][5])-1]) * 1e6
		
		elif final_final_data[i][5][-1] == "B":
			final_final_data[i][5] = float(final_final_data[i][5][:len(final_final_data[i][5])-1]) * 1e9

		else:
			final_final_data[i][5] = float(final_final_data[i][5])

		if final_final_data[i][6][-1] == "K":
			final_final_data[i][6] = float(final_final_data[i][6][:len(final_final_data[i][6])-1]) * 1000

		elif final_final_data[i][6][-1] == "M":
			final_final_data[i][6] = float(final_final_data[i][6][:len(final_final_data[i][6])-1]) * 1e6

		elif final_final_data[i][6][-1] == "B":
			final_final_data[i][6] = float(final_final_data[i][5][:len(final_final_data[i][6])-1]) * 1e9

		else:
			final_final_data[i][6] = float(final_final_data[i][6])

	final_final_data = np.array(final_final_data).transpose()
	final_final_data[2] = final_final_data[2].astype(float)
	final_final_data[3] = final_final_data[3].astype(float)
	final_final_data[4] = final_final_data[4].astype(float)
	final_final_data[5] = final_final_data[5].astype(float)
	final_final_data[6] = final_final_data[6].astype(float)
	final_final_data[8] = final_final_data[8].astype(float)
	final_final_data[9] = final_final_data[9].astype(float)
	final_final_data[10] = final_final_data[10].astype(float)
	final_final_data[11] = final_final_data[11].astype(float)
	final_final_data[12] = final_final_data[12].astype(float)
	final_final_data[13] = final_final_data[13].astype(float)
	"""
	final_final_data[10] = np.zeros(len(final_final_data[10]))
	final_final_data[11] = np.zeros(len(final_final_data[10]))
	final_final_data[12] = np.zeros(len(final_final_data[10]))
	final_final_data[13] = np.zeros(len(final_final_data[10]))
	"""
	return np.array(final_final_data).transpose()


def clean_targets(data):

	data = data.transpose()

	
	for i in range(len(data[7])):

		if len(data[7][i]) == 2:

			if data[7][i] == "F3":
				data[7][i] = "EF4"

			elif data[7][i] == "F4" or data[7][i] == "F5":
				data[7][i] = "EF5"

			else:
				data[7][i] = "E" + data[7][i]

	targets = None
	final_data = []
	for i in range(len(data)):

		if i == 7:
			targets = data[i]
		else:
			final_data.append(np.array(data[i]).astype(float))

	return np.array(final_data).transpose(), targets.transpose()


def concurrent_shuffle(data, targets):

	combined = list(zip(data,targets))
	random.shuffle(combined)

	data[:], targets[:] = zip(*combined)
	return data, targets

def random_forest(data, targets):

	data, targets = concurrent_shuffle(data, targets)
	x_train, x_test, y_train, y_test = train_test_split(data, targets, test_size=0.1)
	
	print(x_train)
	print(set(y_train))
	print("train_size: {}\ntest_size: {}".format(len(x_train), len(x_test)))
	clf = RandomForestClassifier(n_estimators=50)
	clf.fit(x_train, y_train)

	test_output = clf.predict(x_test)
	print(accuracy_score(y_test, test_output))
	print(confusion_matrix(y_test, test_output))


if __name__ == "__main__":

	fil = open("output.csv")
	cs = csv.reader(fil, delimiter=",", quotechar="\"")

	all_data = []

	first = True
	for l in cs:

		if first:
			first = False
			continue
		try:
			assert(len(l) == 52)
		except AssertionError:
			continue

		all_data.append(np.array(l))

	all_data = np.array(all_data)

	print(all_data.shape)
	all_data = all_data.transpose()
	print(all_data.shape)

	final_data = extract_features(all_data)
	print(final_data.shape)
	final_final_data = clean_data(final_data)
	print(final_final_data.shape)
	final_final_data, targets = clean_targets(final_final_data)
	print(final_final_data.shape)

	random_forest(final_final_data, targets)