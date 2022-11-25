import requests
import random
image1 = requests.get('https://en.wikipedia.org/wiki/Computer')
with open ('1.jpg', 'wb') as f:
    f.write(image1.content)
    f.close
with open ('2.jpg', 'wb') as f:
    f.write(image1.content)
    f.close
with open ('3.jpg', 'wb') as f:
    f.write(image1.content)
    f.close
with open ('4.jpg', 'wb') as f:
    f.write(image1.content)
    f.close
with open ('5.jpg', 'wb') as f:
    f.write(image1.content)
    f.close