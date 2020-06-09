import elementarray as el
import pollutantupdater as pol

earray = el.elementarray(100,100,100)
pollist = []
pollist.append(blur_pollutantupdater())


#here's the main loop
numloops = 100
for x in range(numloops):

    for pol in pollist:
        earray.pollutantupdateall(pol)

    earray.elementupdateall()

#end main loop
    
#visualize or check for interesting behavior
