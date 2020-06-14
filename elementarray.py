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

    def __init__(self, cols, rows, layers,
                 originx=default_originx, originy=default_originy, originz=default_originz,
                 sizex=default_sizex, sizey=default_sizey, sizez=default_sizez):
        self.originx = originx
        self.originy = originy
        self.originz = originz

        self.sizex = sizex
        self.sizey = sizey
        self.sizez = sizez

        self.cols = cols #the number of columns in the array, x
        self.rows = rows #the number of rows in the array, y
        self.layers = layers #the number of layers in the array, z

        self.elements = [[[element() for i in range(cols)] for j in range(rows)] for k in range(layers)]

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

    def _ele_from_index(self, indextuple):
        return self.elements[indextuple[0]][indextuple[1]][indextuple[2]]

    def _ele_from_index_if_valid(self, indextuple):
        if (self._is_valid_index(indextuple)):
            return self._ele_from_index(indextuple)
        else:
            return False

    def _is_valid_index(self, indextuple):

        return (indextuple[0]>=0 and indextuple[0]<self.rows and
                indextuple[1]>=0 and indextuple[1]<self.cols and
                indextuple[2]>=0 and indextuple[2]<self.layers)

##alternate _is_valid_index:
##        validflag = True
##        try:
##            throwaway = self.elements[indextuple[0]][indextuple[1]][indextuple[2]]
##        except IndexError as error:
##            validflag = False
##        return validflag





##oops, I think I need to use the non-pythonic C index idiom because
##of the weird way I set up the elements in the elementarray. The way
##they are now, an element object has no method to find its own index
##in the elementarray. I need to pass an index tuple to the pollutantupdater,
##not an element object.
    def pollutantupdateall(self, pu):
        for k in range(self.layers):
            for j in range(self.rows):
                for i in range(self.cols):
                    pu.actonelement((i,j,k), self)



#this function could use similar code to the pullutantupdateall above, but
#it can also use this code because every element is updated independently of position.
    def elementupdateall(self, time):
        for z_layer in self.elements:
            for y_row in z_layer:
                for x_element in y_row:
                    x_element.update(time)  





    '''
    #************ C idiom:

    C generally uses arrays, python generally uses lists (or sometimes
    tuples). They are used in very similar ways.

    #the humble for loop, C:
        for(int i=0; i<numElementsInList; i++) {
            #do something for each element, accessed by elements[i]
        }

    #the triple-nested for loop, C:
        for(int i=0; i<numCols; i++) {
            for(int j=0; j<numRows; j++) {
                for(int k=0; k<numLayers; k++) {
                    #do something for each element, accessed by self.elements[i][j][k]
                    pu.actonelement(self.elements[i][j][k], self.elements);
                }
            }
        }


    **** Python idiom:
     #lists can automatically be changed into "iterators" that break themselves
     down. No index ints like i,j,k are needed!

     for x in ElementList:
         # do something for each element x in the list
         x.something()

     If you really want to use a separate index, you can make something with range():
     for i in range(0, numElements):
         elementArray[i].something()

     a triple-nested list is a list of lists of lists. When a "for" statement tries to
     turn it into an iterator, it sees a list of "x", and the "x" turns out to be double-lists.
     The iterator will return a sequence of double-lists. When another "for" statement
     turns that into an iterator, it sees a list of lists, so it will return a sequence
     of lists. Then a third "for" statement can turn that into an iterator of element
     objects. You can see this breakdown in the triple for-loop above.

     update: I changed it to use the c-style indexers.
        '''
            
        

    def getallneighbors(self, indextuple):
        '''returns a list of all 26 elements neighboring this
element. Checks that the elements exist in the array before
trying to access them. The elements are expected to be accessed
for both reading and writing, and they are not removed or moved
in the original 3d list of elements in this elementarray.
indextuple could be outside the array's indexes, which could
be usefull when the intention is to act on elements on the edge'''
        pass #not implemented yet. It's important to figure out
             #a loop for this so we don't need to copy out 26 lines of code.

    def getfaceneighbors(self, ind):
        '''ind is a tuple representing the index of the element we are
looking at. the function returns a list of the 6 elements that share a face with
the element given by ind. ind could possibly be
outside the exisiting indexes of the elementarray, but only
existing elements will be returned in the output of this function.'''
        #I can think of a few ways to organize this function to cut down on
        #repetition. I'll use a helper function _append_if_valid
        #I changed indextuple to ind just to avoid some typing.
        outputlist = []
        
##        querytuple = (indextuple[0]+1, indextuple[1], indextuple[2])
##        query = self._ele_from_index_if_valid(querytuple)
##        if (type(query)==element):
##            outputlist.append(query)
##
##        querytuple = (indextuple[0]-1, indextuple[1], indextuple[2])
##        query = self._ele_from_index_if_valid(querytuple)
##        if (type(query)==element):
##            outputlist.append(query)

        ##we could repeat that block of four lines 6 times, but copying has two
        ##big problems: It's easy to make a mistake changing the copied text, and
        ##changing the code or updating later is far more work and far more
        ##likely to introduce errors.


        #this still includes a lot of copying! but the copying is limited to a reasonable level.
        self._append_if_valid(ind[0]+1, ind[1], ind[2], outputlist)
        self._append_if_valid(ind[0]-1, ind[1], ind[2], outputlist)
        self._append_if_valid(ind[0], ind[1]+1, ind[2], outputlist)
        self._append_if_valid(ind[0], ind[1]-1, ind[2], outputlist)
        self._append_if_valid(ind[0], ind[1], ind[2]+1, outputlist)
        self._append_if_valid(ind[0], ind[1], ind[2]-1, outputlist)

        return outputlist

    def _append_if_valid(self, x,y,z, outputlist):
        querytuple = (x,y,z)
        query = self._ele_from_index_if_valid(querytuple)
        if (type(query)==element):
            outputlist.append(query)
            
