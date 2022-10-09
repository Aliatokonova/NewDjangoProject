from datetime import datetime


class Smartphone:
    def call(self,number=int):
        print(f"I'm calling to number{number}")


    def where_to_where(self):
        print('you can keep me anywhere')

class Watch:
   
    def see_time(self):
        print(f"it's {datetime.now()} now ")


    def where_to_where(self):
        print('you should wear me on your hand')

class SmartWatch(Watch,Smartphone):
    pass


smartphone = SmartWatch()
print(smartphone.call(number=+9996703200410))
print(smartphone.see_time())
print(smartphone.where_to_where())