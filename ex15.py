#imports the argv module
from sys import argv

#assigns variables to the arguments in argv
# script, filename = argv
# print "The script running this is named %r." % script

#assigns the open file to the variable 'txt'
# txt = open(filename)

# prints the filename of the text file
# print "Here's your file %r:" % filename
# prints the contents of the file
# print txt.read()

print "Type the filename again:"
#gets the file info from the user this time while the program is running
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.close()

