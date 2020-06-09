##from abc import ABC



class pollutantupdater(object):
    
    def actonelement(loctuple, inval):
        pass

class blur_pollutantupdater(pollutantupdater):
    '''this pollutantupdater is meant to represent the tendency of
pollutants to gradually spread out. It decreases the pollutant in
the target element, and slightly increases the pollutant in
neighboring elements (only the face-neighboring elements). For
elements on the edge of the area, pollutants will leak away and
not be replaced.

When this pollutantupdater is called on a point, every face-neighboring element will increase in pollution by "blur" amount, and the element itself will decrease by 6*blur.'''
    
    default_blur = 0.01
    def __init__(self, blur=default_blur):
        self.blur = blur

    def actonelement(loctuple, 
        
        
