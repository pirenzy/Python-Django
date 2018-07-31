class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Workmate(Human):
    def __init__(self, name, age, gender, grade):
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = grade

person1 = Human("홍길동", "25", "남자")
mate1 = Workmate("김철수", "30", "남자", "대리")
print(person1.name)
print(mate1.age)
