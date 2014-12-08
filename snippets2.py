import logging
import csv
import argparse
import sys
#Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)

def put(name, snippet, filename):
	""" Store a snippet with an associated name in the CSV file """
	logging.info("Writing {!r}:::::{!r} to {!r}".format(name, snippet, filename))
	logging.debug("Openning file")
	with open(filename, "a") as f:
		writer = csv.writer(f)
		logging.debug("Writing snippet to file")
		writer.writerow([name,snippet])
	logging.debug("Write successful")
	return name, snippet

def get(name, filename):
	""" Retrieve a snippet with an associated name in the CSV file """
	#logging.info("Writing {!r}:{!r} to {!r}".format(name, filename))
	logging.debug("Openning file")
	with open(filename) as f:
		reader = csv.DictReader(f, delimiter=',')
		logging.debug("reading snippet from file")
		for line in reader:
		    if name == line['csvname']:
			print line['snippet']       
    #logging.debug("reading succcessful")
	
def make_parser():
	""" Construct the command line parser """
	logging.info("Constructing parser")
	description = "Store and retrieve snippets of text"
	parser = argparse.ArgumentParser(description=description)
	subparsers = parser.add_subparsers(dest="command", help="Available commands")

	# Subparser for the put command
	logging.debug("Constructing put subparser")
	put_parser = subparsers.add_parser("put", help="Store a snippet")
	put_parser.add_argument("name", help="The name of the snippet")
	put_parser.add_argument("snippet", help="The snippet text")
	put_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename")
	#Subparser for the get command
	get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
	get_parser.add_argument("name", help="The name of the snippet")
	get_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename")

	return parser

def main():
	""" Main function """
	logging.info("starting snippets")
	parser = make_parser()
	arguments = parser.parse_args(sys.argv[1:])
	# Convert parsed arguments from Namespace to dictionary
	arguments = vars(arguments)
	command = arguments.pop("command")
	#name = arguments.pop("name")

	if command == "put":
		name, snippet = put(**arguments)
		print "Stored {!r} as {!r}".format(snippet, name)
	elif command == "get":
		name = get(**arguments)
	else:
		print "please put command"

if __name__ == "__main__":
	main()