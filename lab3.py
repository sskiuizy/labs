class Book:
    title = ""
    author = ""
    year = ""
    def get_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")
book = Book()
book.title = "Евгений Онегин"
book.author = "Александр Сергеевич Пушкин"
book.year = "1831"
book.get_info()



class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, radius2):
        self.radius = radius2
circle =Circle(2)
circle.set_radius(10)
radius2 = circle.get_radius()
print(f"Radius: {radius2}")



