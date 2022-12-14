import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d1 = {
'row1' : [100,200,300,400],
'row2' : [200,300,400,500]
}

z = np.random.normal(170,10,250)

plt.hist(z)
plt.show()
