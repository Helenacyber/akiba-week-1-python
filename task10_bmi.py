#BMI Health Information
class convertor:
    def __init__(self,name:str,weight: float,height:float):
        self.height =height
        self.weight = weight
        self.name= name

    def BMI_calculator(self):
        BMI = self.weight/(self.height **2)
        return f'{BMI:.2f}'


    def __str__(self):
        print('=' *40)
        print('      BMI REPORT')
        print('=' *40)
        print(f'Name: {self.name}')
        print(f'Weight: {self.weight} m')
        print(f'Height: {self.height} kg')
        print(f'BMI: {self.BMI_calculator()} ETB')   
        print('=' *40)


name =input('Enter Your Name: ')
weight = float(input('Enter Your weight in kg: '))
height = float(input('Enter Your height in m: '))
person_1 = convertor(name , weight , height)
print(person_1.__str__())