class Person:

    def __init__(self,name, age):
        self.name = name
        # self._age = age #make self._age a private var
        if 20 < age < 80:
            self._age = age
        else:
            raise ValueError("Age must be between 20 and 50")

    def display(self):
        print(self.name, self._age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError("Age must be between 20 and 80")

    def set_age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError("Age must be between 20 and 50")

    def get_age(self):
        return self._age

if __name__=='__main__':
    p = Person("Moses", 40)
    p.display()


"""

>>> p.set_age(25)
>>> p.get_age()
25
>>> p.display()
Moses 25
>>> p.set_age(p.get_age()+1)
>>> p.display()
Moses 26
>>> p1 = Person("Dev",200)
>>> p1.display()
Dev 200

>>> p.age
40
>>> p.age = 60
>>> p.age = 100

"""
