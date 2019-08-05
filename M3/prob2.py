"""2.	Make a class called Car. The __init__() method for Car should store the following four attributes: car_model, no_of_gears, is_started, is_stopped. Make a method describe_car() that prints these four bits of information, and with the following methods:
a.	start_car(): if Car is already started, it should print the message “Car already started”, 
otherwise the message should be “Car started”.
b.	stop_car(): if Car is already stopped, it should print the message “Car already stopped”, 
otherwise the message should be “Cart stopped”.
c.	change_gear():  If Car has reached the maximum gear, it should print the message 
“Car is already in top gear”, otherwise it should increment the gear by one and the following message should be displayed “Car is moving at {#gear} gear”.

Create 3 instances representing Car and test each of the 3 methods."""
class Car:
    def __init__(self,regno,no_gears):
        self.regno = regno
        self.no_gears = no_gears
    def start(self):
        if self.is_started:
            print(f"car with regno {self.regno} is already started")
        else:
            print(f"car with reg no{self.regno} started")
    def stop(self):
        if self.is_stopped:
            print(f"car with reg no {self.regno} is already stopped")
        else:
            print(f"car with reg no{self.regno} stopped")
        
    def change_gear(self):
        if self.is_started:
            if self.c_gear<self.no_gears:
                self.c_gear+=1
                
        print(f"car with reg no{self.regno} changed gear")
        
    

    