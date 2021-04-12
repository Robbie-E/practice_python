# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 23:42:21 2021

@author: Robertson
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = np.loadtxt("data.csv", delimiter=',', skiprows=1)
np.random.shuffle(data)
features, targets = data[:,1:], data[:,0]

# Project to a 2-dimensional subspace for visualization
pca = PCA(n_components=2, svd_solver='full')
# Apply dimensionality reduction on features
Pcomps = pca.fit_transform(features)


# Visualize the 2 components
PCs_df = pd.DataFrame(data=Pcomps, columns = ['PC 1', 'PC 2'])
targets_df = pd.DataFrame(data=targets, columns = ['labels'])
All_df =  pd.concat([PCs_df, targets_df['labels']], axis=1)

fig = plt.figure()
ax = fig.add_subplot(1,1,1) 

target_cats = [0,1]
colors = ['r', 'b']

for target_cat, color in zip(target_cats, colors):
    idx = All_df['labels']==target_cat
    ax.scatter(All_df.loc[idx, 'PC 1'], All_df.loc[idx, 'PC 2'], c = color, s = 50)

ax.legend(target_cats)
ax.set_xlabel('Principal Component 1', fontsize = 10)
ax.set_ylabel('Principal Component 2', fontsize = 10)
ax.set_title('two-component PCA', fontsize = 15)
ax.grid()
    