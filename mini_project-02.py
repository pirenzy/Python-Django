class School:
    def __init__(self, name, year, address):
        self.name = name
        self.year = year
        self.address = address

schinfo = School(input("학교의 이름은? "), input("설립 연도는? "), input("학교의 주소는? "))
print(schinfo.name)
print(schinfo.year)
print(schinfo.address)
