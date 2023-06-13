
'''https://www.codewars.com/kata/55c0ac142326fdf18d0000af/train/python'''


class Cube(object):
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    def __init__(self,side=0):
        self.__side = side if side>0 else -side
        
    def get_side(self):
        """Return the side of the Cube"""
        return self.__side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self.__side = new_side if new_side>0 else -new_side