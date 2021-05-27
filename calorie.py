class CalorieCalculator:
    """Represent amount of calories calculated with
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """

    def __init__(self, weight, height, age, sex, temperature):
        self.sex = sex
        self.temperature = temperature
        self.age = age
        self.height = height
        self.weight = weight

    def calculate(self):
        calorie_amount = 0
        if self.sex == 'M':
            calorie_amount = 10*self.weight + 6.25*self.height - 5*self.age + 5 - 10*float(self.temperature)
        elif self.sex == 'F':
            calorie_amount = 10*self.weight + 6.25*self.height - 5*self.age - 161 - 10*float(self.temperature)
        return calorie_amount
