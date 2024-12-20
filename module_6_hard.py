from math import pi,sqrt

class Figure:
    sides_count = 0
    def __init__(self,colors,*sides,filled = False):
        self.filled = filled
        sides = list(sides)
        if isinstance(sides[len(sides)-1], bool): sides.pop(len(sides)-1)
        self.set_color(colors)
        self.set_sides(sides)

    def get_color(self):
        return self._color
    def set_color(self,*colors):
        if isinstance(colors[0], int):
            colors = list(colors)
        else:
            colors = list(*colors)
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
        if isinstance(new_sides[0], int):
            new_sides = list(new_sides)
        else:
            new_sides = list(*new_sides)

        if self.__is_valid_sides(*new_sides):
            self._sides = list(new_sides)
        else:
            self._sides = [1]*self.sides_count

    def __is_valid_sides(self,*new_sides): #bool
        ch_=True
        if len(new_sides) == self.sides_count:
            for i in new_sides:
                if i <= 0 or not isinstance(i, int):
                    return False
        else: return False
        return ch_

    def __len__(self):
        return sum(self._sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self,colors,sides,filled = False):
        super().__init__(colors,sides,filled)
        self.__radius = self._sides[0]/(2*pi)
    def get_square(self):
        return pi*self.__radius**2

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        p = 0.5*(self._sides[0]+self._sides[1]+self._sides[2])
        return sqrt(p*(p-self._sides[0])*(p-self._sides[1])*(p-self._sides[2]))

class Cube(Figure):
    sides_count = 12

    def set_sides(self,*L_):
        if isinstance(L_[0], int):
            L_ = list(L_)
        else:
            L_ = list(*L_)
        if len(L_) == 1 and L_[0] > 0 and type(L_[0]) == int :
            self._sides = [L_[0]]*12
        else:
            if self._sides == []:
                self._sides = [1]*12

    def get_square(self):
        return 6*self._sides[0]**2

    def get_volume(self):
        return self._sides[0] ** 3

if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)
    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())
    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())
    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))
    # Проверка объёма (куба):
    print(cube1.get_volume())   
