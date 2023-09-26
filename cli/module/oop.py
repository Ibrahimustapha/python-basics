#OOP = object oriented programming
#Where going to be talking about class, object and inheritance
def email_generator(Firstname ,Last_name):
    email = f"{Firstname},{Last_name}@gmail.com".lower()
    return email
print(email_generator("Ibrahim","Ibrahim"))

class Car:
    global colour
    global price
    global speed
    global brand
    def __init__(self,colour,price,speed,brand):
        self.colour=colour
        self.price=price
        self.speed=speed
        self.brand=brand
    
    def car_detail(car_name):
        return f"Car colour is {colour}, Car price is {price}, Car speed is {speed}, Car brand is {brand}"


car1 = Car("Blue","N1,000,000","50mph","Toyota")
print(car1.car_detail("Toyota supra"))