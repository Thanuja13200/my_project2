class Father:
    def showFather(self):
        print("This is Father")

class Mother:
    def showMother(self):
        print("This is Mother")

class Child(Father, Mother):
    pass

c = Child()
c.showFather()
c.showMother()