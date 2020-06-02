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



class element(object):
    
    def _correct_neg(self):
        '''a private helper function to enforce nonnegative
values. If the value of pollutant goes negative, it just sets
it to zero. Could produce some weird non-realistic activity,
but the non-realism should be a negligible level for most
situations I can imagine.'''
        if(self.p<0.)self.p=0. #that's all.


    def __init__(self, p=0.):
        self.p = p #the value of the amount of pollutant in this element's volume.
        self.p_prime = 0. #derivative of p over time.
        _correct_neg()

    def modify_p_prime(self, changeval):
        self.p_prime += changeval

    def update(self, time=60):
        self.p += p_prime*time
        p_prime = 0.
        _correct_neg()
        


##class elementarray(object)
##not implemented yet