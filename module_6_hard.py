from math import pi,sqrt

class Figure:
    sides_count = 0
    _sides = []
    _color = [0,0,0]
    filled = False
    def __init__(self,*args):
        if self.sides_count > 0:
            args = list(args)
            colors = args.pop(0)
            self.set_color(colors)
            self.set_sides(*args)

    def get_color(self):
        return self._color
    def set_color(self,*colors):
        if self.__if_valid_color(*colors):
            self._color = colors
    def __if_valid_color(self, *colors): #bool
        k = len(colors)
        ch_ = False
        if k == 3:
            ch_ = True
            for t in colors:
                if t < 0 or t>255: ch_ = False
        return ch_

    def get_sides(self):
        return self._sides
    def set_sides(self,*new_sides):
        if self.__is_valid_sides(*new_sides):
            self._sides = new_sides
        else:
            self._sides = list([])
            for i in range(0,self.sides_count):
                self._sides.append(1)

    def __is_valid_sides(self,*new_sides): #bool
        ch_=True
        if len(new_sides) == self.sides_count:
            for i in new_sides:
                if i <= 0 or not type(int(i)):
                    return False
        else: return False
        return ch_

    def __len__(self):
        return sum(self._sides)

class Circle(Figure):
    sides_count = 1
    __radius = 0
    def __init__(self,*args):
        super().__init__(*args)
        self.__radius = self._sides[0]/2/pi
    def get_square(self):
        return pi*self.__radius**2

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        p = 0.5*(self._sides[0]+self._sides[1]+self._sides[2])
        return sqrt(p*(p-self._sides[0])*(p-self._sides[1])*(p-self._sides[2]))

class Cube(Figure):
    sides_count = 12
    def __init__(self,colors,*L_):
        self.set_color(colors)
        self.set_sides(*L_)

    def set_sides(self,*L_):
        if len(L_) == 1 and L_[0] > 0 and type(L_[0]) == int :
            self._sides = []
            for i in range(0,12):
                self._sides.append(*L_)
        else:
            if self._sides == []:
                for i in range(0,12):
                    self._sides.append(1)

    def get_square(self):
        return 6*self._sides[0]**2

    def get_volume(self):
        return self._sides[0] ** 3


if __name__ == '__main__':
    # fig = Figure()
    # print(fig.get_color())
    # fig.set_color(200,23,200)
    # print(fig.get_color())
    # print(len(fig))
    print('------------')
    # circle1 = Circle((200, 200, 100), 10)
    # print(circle1.get_sides())
    # print(circle1.get_color())
    # circle1.set_color(20,20,20)
    # print(circle1.get_color())
    # circle1.set_sides(5,5,5)
    # print(circle1.get_sides())
    # print(circle1.get_square())
    # circle1.set_sides(5)
    # print(circle1.get_sides())
    print('------------')
    # triangle = Triangle((200,100,100),3,4,5)
    # triangle.set_color(26,25,25)
    # print(triangle.get_sides())
    # print(triangle.get_color())
    # print(triangle.get_square())
    # triangle.set_sides(5,5,5)
    # print(triangle.get_sides())
    # print(triangle.get_square())
    print('-----------------')
    cube = Cube((200,100,100),3)
    print(cube.get_color())
    print(cube.get_sides())
    print(cube.get_volume())
    print('-')
    cube.set_color(10,10,10)
    print(cube.get_color())
    cube.set_sides(5)
    print(cube.get_sides())
    print(cube.get_volume())
    print('-')
    cube.set_color(-5, 10, 10)
    print(cube.get_color())
    cube.set_sides(7,2,3)
    print(cube.get_sides())
    print(cube.get_volume())
