class Human:
    def __init__(self, super_f_n, s_n, ph='+38xxxxxxxxxx'):
        self.__first_name = super_f_n
        self.__second_name = s_n
        self.__phone = ph

    def __str__(self):
        return f"{self.__first_name} {self.__second_name}, mob.{self.__phone}"

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_second_name(self, second_name):
        self.__second_name = second_name

    def set_phone(self, phone):
        self.__phone = phone

    def get_first_name(self):
        return self.__first_name

    def get_second_name(self):
        return self.__second_name

    def get_phone(self):
        return  self.__phone


class Student(Human):
    def __init__(self, f_n, s_n, age, ph='+38xxxxxxxxxx'):
        super().__init__(f_n, s_n, ph)
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


class Parent(Human):
    def __init__(self, f_n, s_n, t, ph='+38xxxxxxxxxx'):
        super().__init__(f_n, s_n, ph)
        self.__type = t

    def set_type(self, type):
        self.__type = type

    def get_type(self):
        return self.__type


class Teacher(Human):
    def __init__(self, f_n, s_n, age, covid, ph='+38xxxxxxxxxx'):
        super().__init__(f_n, s_n, ph)
        self.__age = age
        self.__covid = covid

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_covid(self, covid):
        self.__covid = covid

    def get_covid(self):
        return self.__covid


s1 = Student("Dafydd", "Idontknowenko", 6)
print(s1)
p1 = Parent("Joe", "Baiden", "mother", "+03812345678")
print(p1)
t1 = Teacher("Nil", "Armstrong", 45, "red")
print(t1)
