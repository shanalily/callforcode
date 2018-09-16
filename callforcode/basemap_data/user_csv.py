import csv
import psycopg2

if __name__ == "__main__":
	conn = psycopg2.connect(host="localhost", database="callforcode", user="shanalily", password="frogandtoad")
	cur = conn.cursor()
	cur.execute("SELECT * FROM users;")
	rows = cur.fetchall()
	# print(rows)

	with open('users.csv', 'w') as csvfile:
		fieldnames = ['first_name', 'last_name', 'city', 'state']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()
		for row in rows:
			writer.writerow({'first_name': row[3], 'last_name': row[4], 'city': row[7], 'state': row[8]})