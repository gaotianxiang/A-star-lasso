import re
import os
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

path = r'C:\Users\gtx97\Google Drive\2019-2020_2_UNC_DATA\acflow\AstarLasso\networks'
with open(os.path.join(path, 'getDAGgalaxy.m'), 'r') as file:
    data = file.readlines()

string = ''.join(data)

pattern = r'\(\d+\,\d+\)'

res = re.findall(pattern, string)

res = [x[1:-1].split(',') for x in res]
res = [[int(a) - 1 for a in x] for x in res]

adj_matrix = np.zeros((20, 20))

print(res)
res = np.array(res)
print(res.shape)
rows, cols = np.split(res, indices_or_sections=2, axis=1)

# adj_matrix[res] = 1
# print(adj_matrix)

# adj_matrix[[0, 1], [2, 3]] = 1
adj_matrix[rows, cols] = 1
print(adj_matrix)

sns.heatmap(adj_matrix)
plt.show()
