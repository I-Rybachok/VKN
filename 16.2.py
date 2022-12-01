import pylab
import numpy as np
import collections

with open('text 16.2.txt', 'r') as f:
    text = f.read()
    c=collections.Counter(text)
    counter1 = '\n'.join('{} = {}'.format(tup[0] if tup[0] != "\n" else "\\n", tup[1]) for tup in c.most_common())
    print(counter1)

x=np.array([1,28])
y=np.array([counter1])
pylab.bar(x, y)
pylab.show()