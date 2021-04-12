# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:39:36 2021

@author: Robertson
"""

import numpy as np
from sklearn.linear_model import LogisticRegressionCV

data = np.loadtxt("data.csv", delimiter=',', skiprows=1)
np.random.shuffle(data)
features, targets = data[:,1:], data[:,0]

"""
Use regularized logistic regression with stratified 10-fold cross-validation
Evaluate model using F1 score with balanced class weight since there are more '0' samples
"""

# Fit model to training data, choose regularization from 1e4 to 1e-4 from CV set
# Find optimal regularization parameter using f1 score
logreg = LogisticRegressionCV(Cs=50, cv=10, scoring='f1', class_weight="balanced", random_state=0).fit(features, targets)

# Determine probability of "0" or "1" (prob_attrite) for each example 
probs = logreg.predict_proba(features)
prob_attrite = probs[:,1]

# Predict using the model (returns label with higher probability from probs)
predicted = logreg.predict(features)

# Return f1 score
score = logreg.score(features, targets)