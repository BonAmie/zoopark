class Lion:

    def __init__(self, name, age, food):
        self.Name=name
        self.Age=age
        self.vid="Лев"
        self.Biom="Савана"
        self.ploshad="> 20 м кв"
        self.pisha="рыба, мясо"
        self.eda="хищник"
        self.zvyk="Рёв"
        #животное
        self.Name = name
        self.Age = age
        self.Food = food

    def Voice(self, number):
        for i in range(number):
            print(self.Name, "РААААВВВ")

    def Eat(self):
        self.name="Чавк Ном"

    def Play(self):
        self.name="прыг-скок"

class Panda:

    def __init__(self, name, age, food):
        self.Name=name
        self.Age=age
        self.vid="Панда"
        self.Biom="Бамбуковые леса"
        self.ploshad="> 30 м кв"
        self.pisha="бамбуковые"
        self.eda="травоядные"
        self.zvyk="игигиги(звуки заводящегося жигуля( не знаю как это назвать по-другому))"
        #животное
        self.Name = name
        self.Age = age
        self.Food = food

    def Voice(self, number):
        for i in range(number):
            print(self.Name, "иггигиги")

    def Eat(self):
        self.name="хрум-хрум-хрум глык"

    def Play(self):
        self.name="*перекатывается из стороны в сторону"

class Fox:

    def __init__(self, name, age, food):
        self.Name=name
        self.Age=age
        self.vid="Лиса"
        self.Biom="Тундра"
        self.ploshad="> 25 м кв"
        self.pisha="мясо"
        self.eda="курица, грызу"
        self.zvyk="фыр-фыр"
        #животное
        self.Name = name
        self.Age = age
        self.Food = food

    def Voice(self, number):
        for i in range(number):
            print(self.Name, "фыр-фыр-фыр")

    def Eat(self):
        self.name="чавк чвак"

    def Play(self):
        self.name="прыгает и бугает в разные стороны"
