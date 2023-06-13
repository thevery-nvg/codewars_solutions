
'''https://www.codewars.com/kata/55b75fcf67e558d3750000a3/train/python'''


class Block:
    def __init__(self,sizes):
        self.w,self.l,self.h =sizes
    def get_width(self):
        return self.w
    def get_length(self):
        return self.l
    def get_height(self):
        return self.h
    def get_volume(self):
        return self.w*self.h*self.l
    def get_surface_area(self):
        return 2*(self.w*self.l+self.w*self.h+self.l*self.h)