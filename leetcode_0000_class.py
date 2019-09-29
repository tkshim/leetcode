
#!/usr/bin/env python
#coding: utf-8

class newClass():
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.left = None
        self.right = None

    def total(self):
        return self.v1 + self.v2

i = newClass(1,2)
print 'v1 is : ', i.v1
print 'v2 is : ', i.v2
print 'Sum   : ', i.total()

class inhClass(newClass):
    def dummy(self):
        print self

i2 = inhClass(3,4)
print 'v1 is : ', i2.v1
print 'v2 is : ', i2.v2
print 'Sum   : ', i2.total()


print '-----------------------'

class sansyou():
    v1 = 'This is class Hensuu'
    def __init__(self,v2):
        self.v2 = v2
    v3 = newClass(1,2)

i3 = sansyou('This is instance Hensuu')
print 'v1 is : ', i3.v1
print 'v2 is : ', i3.v2
print 'v1 is : ', i3.v3.v1
print 'v2 is : ', i3.v3.v2

