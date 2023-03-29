"""
    This file used to show the distribution of the different skin lesions' types through the train, validation and test sets.
"""
import numpy as np
import tensorflow.keras as K
import pickle
import seaborn as sns
from sklearn.metrics import (ConfusionMatrixDisplay, confusion_matrix, classification_report)
import matplotlib.pyplot as plt


x_train = pickle.load(open('dir../x_train', 'rb'))
x_val = pickle.load(open('dir../x_val', 'rb'))
x_test = pickle.load(open('dir../x_test', 'rb'))
y_train = pickle.load(open('dir../y_train', 'rb'))
y_val = pickle.load(open('dir../y_val', 'rb'))
y_test = pickle.load(open('dir../y_test', 'rb'))


data = [len(x_train), len(x_val), len(x_test)]
labels = ['train', 'val', 'test']

colors = sns.color_palette('pastel')[0:5]

plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')           # create pie chart
plt.show()


lbl_train, count_train = np.unique(y_train, return_counts=True)
lbl_val, count_val = np.unique(y_val, return_counts=True)
lbl_test, count_test = np.unique(y_test, return_counts=True)

temp = {0: 'acne', 1: 'carcinoma', 2: 'eczema', 3: 'keratosis', 4: 'millia', 5: 'rosacea'}
train_dict, val_dict, test_dict = {}, {}, {}
for i in range(len(lbl_train)):
    train_dict[temp[lbl_train[i]]] = count_train[i]
for i in range(len(lbl_val)):
    val_dict[temp[lbl_val[i]]] = count_val[i]
for i in range(len(lbl_test)):
    test_dict[temp[lbl_test[i]]] = count_test[i]

lst_lbl, lst_count, lst_type = [], [], []
for k, v in train_dict.items():
    lst_lbl.append(k)
    lst_type.append('train')
    lst_count.append(v)
for k, v in val_dict.items():
    lst_lbl.append(k)
    lst_type.append('validation')
    lst_count.append(v)
for k, v in test_dict.items():
    lst_lbl.append(k)
    lst_type.append('test')
    lst_count.append(v)

sns.set_theme(style="whitegrid")
ax = sns.barplot(x=lst_type, y=lst_count, hue=lst_lbl)
for i in ax.containers:
    ax.bar_label(i,)
plt.show()
