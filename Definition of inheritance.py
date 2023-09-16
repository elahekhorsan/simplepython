class Animal :
    def __int__(self,name,kind,color):
        self.name: name
        self.kind: kind
        self.color: color
class Dog (animal) :
    def __int__(self,name,kind,color,eye_color):
        super().__init__(name,kind,color)
        self.eye_color: eye_color

class Cat (Animal) :
    def __int__(self,name,kind,color,age):
        super().__int__(name,kind,color)
        self.age: age