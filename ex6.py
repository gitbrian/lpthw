#assigns "There are 10 types of people." to x.  %d is base 10 decimal integer
x = "There are %d types of people'." % 10
binary = "binary"
do_not = "don't"
#assigns "Those who know binary and those who don't." to y.  
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r seems interesting - it seems to print the evaluated expression.
print "I said: %r." % x
# to get the quotes here, we had to put the parens around %s
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

hilarious_type = str(type(hilarious))
joke_evaluation_type = str(type(joke_evaluation))
print "hilarious is of the type " + hilarious_type
print "joke_evaluation is of the type " + joke_evaluation_type

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e