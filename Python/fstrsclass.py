class Intro_NoRepr:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

class Intro_NoStr:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def __repr__(self):#best option
        return f"{self.first_name} {self.last_name} is {self.age}. Awesome!"

class Intro:
    def __init__(self, first_name, last_name, age):#constructor
        self.first_name = first_name#"self" is required for orientation
        self.last_name = last_name
        self.age = age
    def __str__(self):#returns class in format of string
        return f"{self.first_name} {self.last_name} is {self.age}."
    def __repr__(self):#official representation -can replace "__str__"
        return f"{self.first_name} {self.last_name} is {self.age}. Awesome!"
        
new_intro= Intro("better","well",25)
new_intro_noStr= Intro_NoStr("better","well",25)
new_intro_noRepr= Intro_NoRepr("better","well",25)
print(f"{new_intro}")
print(f"{new_intro!r}")#grants use of "__repr__" if both available
print(f"{new_intro_noStr}")
print(f"{new_intro_noStr!r}")
print(f"{new_intro_noRepr}")
print(f"{new_intro_noRepr!r}")