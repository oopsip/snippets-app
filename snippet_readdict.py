import csv
with open('snippets.csv') as f:
		reader = csv.DictReader(f, delimiter=',')
		for line in reader:
			print line