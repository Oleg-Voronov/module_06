from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._coords = [0,0,0]
        self.speed = speed

    def move(self,dx,dy,dz):
        self._coords[0] +=self.speed * dx
        self._coords[1] += self.speed * dy
        z = self._coords[2]+self.speed *dz
        if z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._coords[2]=z

    def get_coords(self):
        print(f'X: {self._coords[0]}, Y: {self._coords[1]}, Z: {self._coords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f"Here are(is) {randint(1,4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self,dz):
        self._coords[2] = abs(self._coords[2] - dz * self.speed // 2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill( PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self,speed):
        super().__init__(speed)
        self.sound = "Click-click-click"

if __name__ == '__main__':
    # print('---Animal---')
    # animal = Animal(5)
    # animal.attack()
    # animal.move(2,2,-1)
    # animal.get_coords()
    # animal.speak()
    # print('---Bird---')
    # bird = Bird(2)
    # bird.sound = 'Карр...'
    # bird.lay_eggs()
    # bird.speak()
    # print('---Aqua----')
    # aq = AquaticAnimal(10)
    # aq.move(10,10,20)
    # aq.get_coords()
    # aq.dive_in(6)
    # aq.get_coords()

    print('---Duckbill___')
    db = Duckbill(10)
    print(db.live)
    print(db.beak)
    db.speak()
    db.attack()
    db.move(1, 2, 3)
    db.get_coords()
    db.dive_in(6)
    db.get_coords()
    db.lay_eggs()
