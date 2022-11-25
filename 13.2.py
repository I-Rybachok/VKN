spysok1=[]
class telephone():
    name='Nokia'
    model='3310'
    spysok = list(spysok1)
    def init(self,n,m,s):
        self.name=str(n)
        self.model=str(m)
        self.spysok=str(s)
    def set_name(self,n):
        self.name=str(n)
    def set_model(self,m):
        self.model=str(m)
    def set_spysok(self,s):
        self.spysok = str(s)
tel=telephone()
num = 1
while num != 0 :
    t = tel.set_spysok(input('Введіть вхідний номер та користувача: '))
    spysok1.append(t)
    ask = input('Чи бажаєте ви продовжити?')
    if ask == 'Ні':
        break
print(tel.name, tel.model, sep = ',')
print(tel.spysok, end = '')