def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a prty!"
    print "Get a blanket. \n"

def the_guit_function():
    print "Who is your favorite guitar player?\n"
    answer1 = raw_input("Favorite #1: ")
    print "Who is your second favorite guitar player?\n"
    answer2 = raw_input("Second Favorite: ")
    print "So you like %s best and %s second best.  Cool." % (answer1, answer2)
    
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print"OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "Calling guit"
the_guit_function()