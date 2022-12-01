import  numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.5, 12)
y = (x**(1/2))+(x**(1/3))+1.1
plt. plot(x, y, 'b-', label='(x**(1/2))+(x**(1/3)+1,1, x∈[−0,5;12]')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-0.5, 12, 0, 10]) #задання [xmin, xmax, ymin, ymax]
plt.grid(True) #cтворення сітки 
plt.title('Графік функції ')
plt.legend() #вставка легенди(тексту в label)
plt.show()
plt.savefig('image16.png', dpi=400)