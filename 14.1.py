import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.williamshakespeare.net/poems.jsp")
f = open('C:/Users/Ira/Desktop/Університет/ВКН/Лаб14/text.txt','wt')

print(r.status_code)
if r.status_code==200:
    r1 = BeautifulSoup(r.text,'html.parser')
    rem = r1.findAll('li')
    print(rem)

rem1 = str(rem)
rem2 = ' '.join(rem1)
f.write(rem2)    
f.close