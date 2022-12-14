import matplotlib.pyplot as plt
import numpy as np

data = {'C':20, 'C++':15, 'Java':30,'Python':35}
courses = list(data.keys())
values = list(data.values())
plt.bar(courses,values)

plt.show()

plt.pie(values)

plt.show()

x = [i for i in range(1,100,12)]
y = [i for i in range(1,100,12)]

plt.scatter(x,y)
plt.show()

z = np.random.normal(170,10,250)

plt.hist(z)
plt.show()