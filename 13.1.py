class book:
    name='Кобзар'
    author='Т.Шевченко'
    house_publication='Видавництво Лева'
    year=2015
    pages=200
    def init(self,n, a, h, y, p):
        self.name=str(n)
        self.author=str(a)
        self.house_publication=str(h)
        self.year=float(y)
        self.pages=float(p)
    def set_name (self,n:str):
        self.name=n
    def set_author(self,a:float):
        self.author=a
    def set_house_publication(self,h:str):
        self.house_publication=h
    def set_year(self,y:float):
        self.year=y
    def set_pages(self,p:float):
        self.pages=p
    def get_name():
        return(self.name)
    def get_author():
        return(self.author)
    def get_house_publication():
        return(self.house_publication)
    def get_year():
        return(self.year)
    def get_pages():
        return(self.pages)

b = book()
print(b.name,b.author,b.house_publication,b.year,b.pages, sep = ',')
b.set_year(input('Введіть рік видіння: '))
b.set_pages(input('Введіть кількість сторінок: '))
print(b.name,b.author,b.house_publication,b.year,b.pages, sep = ',')


num = 1
while num != 0:
    ask = input('Чи бажаєте внести нову книгу?')
    if ask == 'Ні':
        break
    class new_book(book):
        name=input('Введіть назву: ')
        author=input('Введіть автора: ')
        house_publication=input('Введіть видівництво: ')
        year=int(input('Введіть рік: '))
        pages=int(input('Введіть кількість сторінок: '))
        def init(self,n, a, h, y, p):
            self.name=str(n)
            self.author=str(a)
            self.house_publication=str(h)
            self.year=float(y)
            self.pages=float(p)
        def set_name (self,n:str):
            self.name=n
        def set_author(self,a:float):
            self.author=a
        def set_house_publication(self,h:str):
            self.house_publication=h
        def set_year(self,y:float):
            self.year=y
        def set_pages(self,p:float):
            self.pages=p
        def get_name():
            return(self.name)
        def get_author():
            return(self.author)
        def get_house_publication():
            return(self.house_publication)
        def get_year():
            return(self.year)
        def get_pages():
            return(self.pages)
    b1 = new_book()
    print(b1.name,b1.author,b1.house_publication,b1.year,b1.pages, sep = ',')