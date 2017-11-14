

class Animal(object):
    def run(self):
        print("Animal__runing!!!")


class Dog(Animal):
    def run(self):
        print("Dog__running!!")


class Cat(Animal):
    def run(self):
        print("Cat__running!!")


class IO(Animal):
    def getIO(self):
        return  self

iO=IO()
iO.run()

class PO(object):
    def run(self):
        print("Animal__runing!!!")
op =PO()

print(type(op)==PO)
print(PO)
