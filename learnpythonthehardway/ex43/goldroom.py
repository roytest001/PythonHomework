import room

class goldroom(Room):
	def __init__(self, length, width, height, stores):
		super(goldroom, self).__init__(stores)
		self.stores = stores
    

    #def volume(self):
    	#super(goldroom, self).volume()


    #def function(self):
    
    #	pass

a = goldroom(4, 5, 6, "golds")

print a.stores





