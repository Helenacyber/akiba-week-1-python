#BMI Health Information
class convertor:
    def __init__(self,name:str,weight: float,height:float):
        self.height =height
        self.weight = weight
        self.name= name

    def BMI_calculator(self):
        BMI = self.weight/(self.height **2)
        return f'{BMI:.2f}'