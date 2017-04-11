
import pandas as pd
import pylab as pl
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation, svm
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.neighbors import KNeighborsClassifier


df = pd.read_csv("c:/Users/kyungyong/Documents/Python Scripts/SML Project/final_DJIA.csv")
cols_to_keep = ['Class','sentiment_polarity', 'sentiment_subjectivity', 'Positive', 'Negative', 'Neutral']
data = df[cols_to_keep]

train_cols = data.columns[1:6]
print(train_cols)


clf1 = svm.SVC(kernel='rbf')
clf2 = svm.LinearSVC()
clf3 = svm.SVC(kernel='linear')
clf4 = svm.SVC(kernel='poly', degree=2)
clf5 = GaussianNB()
clf6 = BernoulliNB()
clf7 = KNeighborsClassifier(n_neighbors = 5)
clf8 = LogisticRegression()


scores = cross_validation.cross_val_score(clf1,data[train_cols], data['Class'], cv=10)
print("SVM with rbf kernel Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(),scores.std()*2))

scores = cross_validation.cross_val_score(clf2,data[train_cols], data['Class'], cv=10)
print("SVM with LinearSVC Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(),scores.std()*2))

scores = cross_validation.cross_val_score(clf3,data[train_cols], data['Class'], cv=10)
print("SVM with linear kernel Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(),scores.std()*2))

scores = cross_validation.cross_val_score(clf4,data[train_cols], data['Class'], cv=10)
print("SVM with poly kernel with deree 2 Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(),scores.std()*2))

scores = cross_validation.cross_val_score(clf5,data[train_cols], data['Class'], cv=10)
print("GaussianNB Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(),scores.std()*2))

scores = cross_validation.cross_val_score(clf6,data[train_cols], data['Class'], cv=10)
print("BernoulliNB Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(),scores.std()*2))

scores = cross_validation.cross_val_score(clf7,data[train_cols], data['Class'], cv=10)
print("KNeighborsClassifier Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(),scores.std()*2))

scores = cross_validation.cross_val_score(clf8, data[train_cols], data['Class'], cv=10)
print("Logistic Regression Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(),scores.std()*2))
