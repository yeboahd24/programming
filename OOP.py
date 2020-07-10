from enum import Enum, unique

@unique
class Fruit(Enum):
    """The unique help to prevent double values
    like APPLE = 1 and PEAR = 1 this will cause an error because
    PEAR and APPLE is having the same value
    """
    APPLE = 1
    PEAR = 2
    BANANA = 5
    # ORANGE = 1

# print(Fruit.APPLE.name, Fruit.APPLE.value)


class myColor:
    def __init__(self):
        self.red = 50
        self.green = 70
        self.blue = 100

    def __getattr__(self, attr):
        """So in here the rgbcolor is behaving like instance method"""
        if attr == 'rgbcolor':
            return (
            self.red, self.blue, self.green
            )
        elif attr == 'add':
            return (self.red + self.blue + self.green)
        else:
            raise AttributeError


    def __setattr__(self, name, value):
        if name == 'rgbcolor':
            self.red = value[0]
            self.blue = value[1]
            self.green = value[2]
        else:
            super().__setattr__(name, value)
color = myColor()
# print(color.rgbcolor)
# print(color.add)
#
# color.rgbcolor = (90, 80, 75)
# print(color.rgbcolor)
