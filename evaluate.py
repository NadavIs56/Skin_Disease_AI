"""
    This file used to evaluate our model for fine-tuning and better understanding.
    It shows the cunfusion matrix, accuracy & loss histogram and classification report.
"""

import numpy as np
import tensorflow.keras as K
import pickle
from sklearn.metrics import (ConfusionMatrixDisplay, confusion_matrix, classification_report)
import matplotlib.pyplot as plt


x_test = pickle.load(open('train_val_test_sets6/x_test', 'rb'))
y_test = pickle.load(open('train_val_test_sets6/y_test', 'rb'))

with open('hist_dir..', "rb") as file_pi:
    hist = pickle.load(file_pi)

model = K.models.load_model("model_dir..")

predictions = model.predict(x_test)
test_pred = np.argmax(predictions, axis=1)

types = ['acne', 'carcinoma', 'eczema', 'keratosis', 'mila', 'rosacea']

cm = confusion_matrix(y_test, test_pred)                    # confusion matrix
print("Confusion Matrix\n", cm)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=types)
fig, ax = plt.subplots(figsize=(15, 15))
disp.plot(ax=ax, cmap=plt.cm.Blues)
plt.show()

acc_arr, val_acc_arr = [0.0], [0.0]
for i in hist['accuracy']:
    acc_arr.append(i)
for i in hist['val_accuracy']:
    val_acc_arr.append(i)
plt.plot(acc_arr)                               # plot accuracy vs epoch
plt.plot(val_acc_arr)
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.ylim(bottom=0)
plt.xlim(left=0)
plt.xticks(np.arange(0, 25, 2))
plt.grid()
plt.show()

loss_arr, val_loss_arr = [0.0], [0.0]
for i in hist['loss']:
    loss_arr.append(i)
for i in hist['val_loss']:
    val_loss_arr.append(i)
plt.plot(loss_arr)                              # Plot loss values vs epoch
plt.plot(val_loss_arr)
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.ylim(bottom=0)
plt.xlim(left=0)
plt.xticks(np.arange(0, 25, 2))
plt.grid()
plt.show()

for i in range(6):
    print(f'{types[i]} - {((cm[i][i] / sum(cm[i])) * 100):.2f}%')

print("\nclassification_report: \n" + str(classification_report(y_test, test_pred)))

