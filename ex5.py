name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180.0 # lbs
weight_in_kilos = weight/2.2
height_in_centimeters = height*2.54
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
phrase = 'That\'s the way the cookie crumbles.'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print ''
print "I said %s" % phrase
print "I really said %r" % phrase
print "By the by, my weight in kilos is %f." % weight_in_kilos
print "and my height in cm is %d." % height_in_centimeters

print ''
#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
