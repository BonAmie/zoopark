class Lion:

    def __init__(self, name, age):
        self.Name=name
        self.Age=age
        self.IndexPushistosti=100

    def DoRfav(self, number):
        for i in range(number):
            print(self.Name, "Rfaaavv")

    def Griva(self):
        self.IndexDlinigrivi-=10
