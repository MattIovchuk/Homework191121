class Sort:
    def __init__(self, a):
        self.a = a

    def bubble(self):
        for i in range(len(self.a) - 1):
            for j in range(len(self.a) - i - 1):
                if self.a[j] > self.a[j + 1]:
                    self.a[j], self.a[j + 1] = self.a[j + 1], self.a[j]
        return print(self.a)


my_list = Sort([5, 3, 4, 1, 2])
my_list.bubble()
input("Press Enter to exit...")
