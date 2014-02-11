#coding=utf-
#coding=utf-8

class Room(object):
    """docstring for Room"""

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def area(self):
        return self.length * self.width

    def volume(self):
        return self.length * self.width * self.height

    def function(self):
        print " room's purpose "


class goldroom(Room):
    def __init__(self, length, width, height, stores):
        super(goldroom, self).__init__(length, width, height)
        self.stores = stores


    def function(self):
        print "goldroom stores many goods!!!!"


a = goldroom(4, 5, 6, "golds")

print a.stores
print a.area()
print a.volume()
print a.function()
