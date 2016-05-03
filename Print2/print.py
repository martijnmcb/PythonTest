a = "De tafels op een rij, en dit is de tafel van"
b = " Martijn kent deze tafel wel uit zijn hoofd toch?"
for x in xrange(1, 11):
    for y in xrange(1, 11):
        print ("%s %d      %d * %d = %d %s") % (a, x, y, x, x*y, b)
        
        list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for zlist in list_of_lists:
    for x in zlist:
        print (x)
        
        