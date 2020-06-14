


##
##class pollutantupdater(object):
##    
##    def actonelement(elementindex, array):
##        '''Element is the element to be acted on, while
##array is the elementarray holding the element. Passing the
##array to this function is necessary because the pollution
##change will often depend on other elements and change other
##elements, which can be accesssed through this elementarray.'''
##        pass


class blur_pollutantupdater(object):
    '''this pollutantupdater is meant to represent the tendency of
pollutants to gradually spread out. It decreases the pollutant in
the target element, and slightly increases the pollutant in
neighboring elements (only the face-neighboring elements). For
elements on the edge of the area, pollutants will leak away and
not be replaced.

When this pollutantupdater is called on an element, every face-neighboring
element will increase in pollution by "blur" amount, and the
element itself will decrease by 6*blur.

blur should be a positive float. '''
    
    default_blur = 0.01
    
    def __init__(self, blur=default_blur):
        self.blur = blur

    def actonelement(self, elementindex, array):
        center_ele = array._ele_from_index_if_valid(elementindex)
        center_ele.modify_p_prime(-6.*self.blur)
        for e in array.getfaceneighbors(elementindex):
            e.modify_p_prime(self.blur)
    
class source_pollutantupdater(object):
    '''this pollutantupdater represents a source of pollutants like a
smokestack. In a certain given location, the pollution at that element
will gradually increase constantly.

The source is a ball with a given radius at a given location in 3D space.
Any element whose center is within this ball will increase. Any element
outside the ball will not be affected by this pollutantupdater. It's
possible to make the radius too small to include any elements, in
which case the pollutant updater will do nothing but waste computing time.'''
    default_radius = 2.0
    default_x = 5.0
    default_y = 1.0
    default_z = 2.0
    default_pollution = 0.05

    def __init__(self, pollution=default_pollution, x=default_x, y=default_y, z=default_z, rad=default_radius):
        self.x = x
        self.y = y
        self.z = z
        self.radsq = rad*rad #radius squared is stored, because this is the value used to check location.
        self.poll = pollution

    def actonelement(self, elementindex, array):
        #first check this element is within the ball representing the location of the source.
        ele_loc = array._center_loc_from_index(elementindex)
        delx = ele_loc[0]-self.x
        dely = ele_loc[1]-self.y
        delz = ele_loc[2]-self.z
        distance_squared = delx*delx + dely*dely + delz*delz
        #distance_squared is the square distance between the location of this element and the center of the location of this source.

        if(distance_squared > self.radsq):
            pass #outside the ball, so no change in pollution
        else:
            #inside the ball, so pollution increases.
            e = array._ele_from_index(elementindex).modify_p_prime(self.poll)
        
        
        
