class Car :
    def __init__(self,userbrand,usermodel):
        self.brand = userbrand
        self.model = usermodel 


my_car = Car("Toyota","SUV")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Deepal","Safari")
print(my_new_car.model)
print(my_new_car.brand)