'''units: what units are used? Constant values such as
initial value or rate of decay or wind speed are all dependent
on what units are being discussed.

distance: meter
time: second
pollutant concentration: some number of particles per cubic meter?

The physical location of the element, and relationships such
as which elements are neighboring other elements, will be
tracked by the element array, not the individual elements themselves.

'''
import math



class element(object):
    
    def _correct_neg(self):
        '''a private helper function to enforce nonnegative
values. If the value of pollutant goes negative, it just sets
it to zero. Could produce some weird non-realistic activity,
but the non-realism should be a negligible level for most
situations I can imagine.'''
        if(self.p<0.):
            self.p=0. #that's all.
        pass


    def __init__(self, p=0., p_prime=0.):
        self.p = p #the value of the amount of pollutant in this element's volume.
        self.p_prime = p_prime #derivative of p over time.
        self._correct_neg()

    def __str__(self):
        output = "(" + str(self.p)
        if(self.p_prime != 0.):
            output += ("," + str(self.p_prime))
        output += ")"
        return output

    def modify_p_prime(self, changeval):
        self.p_prime += changeval

    def modify_p(self, changeval):
        '''this method instantly adds (or subtracts) pollution from
the element. should probably be used sparingly.'''
        self.p += changeval
        self._correct_neg()

    def update(self, time=1.):
        self.p += self.p_prime*time
        self.p_prime = 0.
        self._correct_neg()
        



class elementarray(object):
    '''This class is important but it's simpler than it seems. Much
of this code could be compressed if we create a class representing
location points in 3d space, that would replace three lines with one
in many places.


elementarray represents a three-dimensional group of many element objects. Its primary
way of existing is to interact with pollutantupdater objects: the
pollutantupdater will be able to "query" the elementarray to find
the value of pollution at certain points, and change the value at
certain points.

Elements are set up relative to a reference point which is designated
0,0,0. A pollutant updater can act on every element, or act
specifically on a certain element. There can also be actions that
behave differently based on the location of the element.

Elements have a physical size that is constant and set by the
elementarray. Elements can be accessed by physical position or
index in the elementarray. Element 0,0,0 has the physical location
from the origin point to sizex, sizey, sizez.


syntax for making a numpy ndarray
>>> testlist = [[[el.element() for z in range(7)] for y in range(6)] for x in range(5)]
>>> testtype = np.dtype(el.element, copy=True)
>>> testa = np.array(testlist, testt

'''

    default_originx = 0.
    default_originy = 0.
    default_originz = 0.

    default_sizex = 1.
    default_sizey = 1.
    default_sizez = 1.

    def __init__(self, width, breadth, height,
                 originx=default_originx, originy=default_originy, originz=default_originz,
                 sizex=default_sizex, sizey=default_sizey, sizez=default_sizez):
        self.originx = originx
        self.originy = originy
        self.originz = originz

        self.sizex = sizex
        self.sizey = sizey
        self.sizez = sizez

        self.width = width
        self.breadth = breadth
        self.height = height

        self.elements = [[[element() for k in range(height)] for j in range(breadth)] for i in range(width)]

    def _index_from_loc(self, loctuple):
        '''returns the integer tuple of the index of the element at that location'''
        delx = loctuple[0] - self.originx
        dely = loctuple[1] - self.originy
        delz = loctuple[2] - self.originz

        indexx = math.floor(delx/self.sizex)
        indexy = math.floor(dely/self.sizey)
        indexz = math.floor(delz/self.sizez)

        return (indexx, indexy, indexz)

    def _loc_from_index(self, indextuple):
        '''helper function, returns the corner of the location of this element closest to the origin'''
        locx = self.originx + indextuple[0]*self.sizex
        locy = self.originy + indextuple[1]*self.sizey
        locz = self.originz + indextuple[2]*self.sizez
        return (locx,locy,locz)

    def _center_loc_from_index(self, indextuple):
        '''helper function, returns the location of the center of this element'''
        locx = self.originx + (indextuple[0]+0.5)*self.sizex
        locy = self.originy + (indextuple[1]+0.5)*self.sizey
        locz = self.originz + (indextuple[2]+0.5)*self.sizez
        return (locx,locy,locz)

##    def pollutantupdateall(self, pu):
##        for z_layer in elements:
##            for y_row in z_layer:
##                for x_col in y_row:
                    
        



