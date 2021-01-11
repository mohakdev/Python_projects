import random

# Disclaimer:
# The code you're about to see is 
# is from a work-in-progress version of the code.
# Everything you see is potentially subject to change. 
class teacher:
    bonus= 2000
    def __init__(self,pay,fname,lname):
        self.pay=pay
        self.fname=fname
        self.lname=lname
    def full_name(self):
        return '{} {} '.format (self.fname , self.lname)
    def apply_bonus(self):
        self.pay = int(self.pay + self.bonus)

class cordinators(teacher):
    bonus = 3000
    def __init__(self,pay,fname,lname,area):
        super().__init__(pay,fname,lname)
        self.area=area

t1=cordinators(70000,'Sushma','sharma' , 'Floor 1')
t2=cordinators(90000,'Rohan' , 'mehta', 'Floor 3')
print(t1.area)
# print(t1.fname)
# print(t1.pay)
# t1.apply_bonus()
# print(t1.pay)