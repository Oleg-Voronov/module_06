class Animal:
    alive = True
    fed = False

    def __str__(self):
        s = ''
        if self.alive:
            s = f'{self.name} живой'
            if self.fed:
                s = s + ' и сытый'
            else:
                s = s + ' но голодный'
        else:
            s=f'{self.name} мёртв'
        return s


    def eat(self,food):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Plant:
    edible = False
    def __str__(self):
        s =''
        if self.edible:
            s =f'Я съедобный {self.name}'
        else:
            s= f'Я НЕ съедобный {self.name}'
        return s

class Mammal(Animal):
    def __init__(self,name):
        self.name = name
class Predator(Animal):
    def __init__(self,name):
        self.name = name
class Flower(Plant):
    def __init__(self,name):
        self.name = name
class Fruit(Plant):
   def __init__(self, name):
       self.name = name
       self.edible = True

if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')
    print(a1.name)
    print(p1.name)
    print(a1.alive)
    print(a2.fed)

    print(a1)
    print(a2,'\n')
    print(p1)
    print(p2,'\n')

    a1.eat(p1)
    a2.eat(p2)

    print(a1.alive)
    print(a2.fed)

    print(a1)
    print(a2)
