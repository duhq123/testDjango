

class testClass:
    def __init__(self):
        self.name = None
        self.code = None

    def get_name(self, test):
        global name
        self.name = test['name']
        return self.name

    def get_code(self, data):
        global code, name
        self.name = data['name']
        self.code = data['code']
        return self.name, self.code

    def __str__(self):
        return self.name, self.code


if __name__ == '__main__':
    t = testClass()
    print(t.__str__())
    test= {'name': 'test1'}
    print(t.get_name(test))
    print(t.__str__())
