class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def work(self):
        return 'I can work!'


class Developer(Employee):
    def __init__(self, name, surname, language):
        super().__init__(name, surname)
        self.__language = language

    def work(self):
        return 'I am coding!'

    def get_language(self):
        return self.__language

    def set_language(self, language):
        self.__language = language


class Tester(Employee):
    def __init__(self, name, surname, language, test_framework):
        super().__init__(name, surname)
        self.language = language
        self.test_framework = test_framework

    def __str__(self):
        return f'{self.name} {self.surname} {self.language} {self.test_framework}'

    def work(self):
        return 'I am testing!'

    def get_language(self):
        return self.language


# employee1 = Employee('Alex', 'Smith')
# print(employee1.name, employee1.surname)
#
dev1 = Developer('Max', 'Frolov', 'Python')
print(dev1.name, dev1.surname, dev1.get_language())
dev1.work()
dev1.__language = 'Java'
print(dev1.get_language())

# tester1 = Tester('Anna', 'Fedotova', 'Java', 'TestNG')
# print(tester1.__str__())
# tester1.work()
# print(isinstance(dev1, Developer))
# print(issubclass(Developer, Employee))
