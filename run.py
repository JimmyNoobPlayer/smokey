import elementarray as el
import pollutantupdater as pol

earray = el.elementarray(10,10,10)
pollist = []

#ptest = pol.source_pollutantupdater()

pollist.append(pol.blur_pollutantupdater(3.0))
pollist.append(pol.source_pollutantupdater())


#here's the main loop
numloops = 1000
frametime = 0.1
for x in range(numloops):

    for pol in pollist:
        earray.pollutantupdateall(pol)

    earray.elementupdateall(frametime)

#end main loop
    
#visualize or check for interesting behavior
