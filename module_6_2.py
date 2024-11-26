class Vehicle:
    __COLOR_VARIANTS = ['red','green','blue','black','white','purple','yellow']
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        color = color.lower()
        if color in self.__COLOR_VARIANTS:
            self.__color = color
        else:
            print("Такого цвете нет в списка цветов, белым будешь")
            self.__color = 'white'

    def get_model(self):
        print(f'Модель {self.__model}')
    def get_horsepower(self):
        print(f'Мощность двигателя {self.__engine_power}')
    def get_color(self):
        print(f'Цвет: {self.__color}')
    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец; {self.owner}')

    def set_color(self,color):
        color = color.lower()
        if color in self.__COLOR_VARIANTS:
            self.__color = color
            print(f'Тачку перекрасили в {color}')
        else:
            print(f'Нельзя сменить цвет на {color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

if __name__ == '__main__':
    car1 = Sedan('Кодер Вася','ВАЗ 2104','white',70)
    car1.print_info()
    print('---')
    car1.set_color('YelloW')
    car1.set_color('pink')
    car1.owner = 'Маньяк Петя'
    car1.print_info()
    print('---')
    car1.model = 'Волга' # попытка изменить значение из-вне
    car1.print_info()

# # проверочки
# # Текущие цвета __COLOR_VARIANTS = ['red','green','blue','black','white','purple','yellow']
#     vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# # Изначальные свойства
#     vehicle1.print_info()
# # Меняем свойства (в т.ч. вызывая методы)
#     vehicle1.set_color('Pink')
#     vehicle1.set_color('BLACK')
#     vehicle1.owner = 'Vasyok'
# # Проверяем что поменялось
#     vehicle1.print_info()
