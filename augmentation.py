"""
    This file used to add augmented images to our dataset for classes with lack of images according to the output of the "sets_visualization".
"""
import pickle
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from skimage.transform import rotate

x_train = pickle.load(open('train_val_test_sets6/after_aug/x_train', 'rb'))
y_train = pickle.load(open('train_val_test_sets6/after_aug/y_train', 'rb'))
x_val = pickle.load(open('train_val_test_sets6/x_val', 'rb'))
y_val = pickle.load(open('train_val_test_sets6/y_val', 'rb'))
x_test = pickle.load(open('train_val_test_sets6/x_test', 'rb'))
y_test = pickle.load(open('train_val_test_sets6/y_test', 'rb'))

x_t = len(x_train)
x_copy = x_train.copy()
count = 0
ecz, ker, ros = 0, 0, 0
for i in tqdm(range(x_t)):
    if y_train[i] == 0:
        x_train = np.append(x_train, [rotate(x_copy[i], angle=45, mode='wrap')], axis=0)
        y_train = np.append(y_train, 0)

    elif y_train[i] == 2:
        if ecz % 3 == 0:
            x_train = np.append(x_train, [rotate(x_copy[i], angle=45, mode='wrap')], axis=0)
            x_train = np.append(x_train, [np.flipud(x_copy[i])], axis=0)
            for j in range(2):
                y_train = np.append(y_train, 2)
        ecz += 1

    elif y_train[i] == 3:
        if ker % 6 == 0:
            x_train = np.append(x_train, [rotate(x_copy[i], angle=45, mode='wrap')], axis=0)
            x_train = np.append(x_train, [np.flipud(x_copy[i])], axis=0)
            for j in range(2):
                y_train = np.append(y_train, 3)
        ker += 1

    elif y_train[i] == 4:
        x_train = np.append(x_train, [rotate(x_copy[i], angle=45, mode='wrap')], axis=0)
        x_train = np.append(x_train, [np.flipud(x_copy[i])], axis=0)
        x_train = np.append(x_train, [np.fliplr(x_copy[i])], axis=0)
        x_train = np.append(x_train, [rotate(np.fliplr(x_copy[i]), angle=270, mode='wrap')], axis=0)
        for j in range(4):
            y_train = np.append(y_train, 4)

    elif y_train[i] == 5:
        if ros % 9 == 0:
            x_train = np.append(x_train, [rotate(x_copy[i], angle=45, mode='wrap')], axis=0)
            x_train = np.append(x_train, [np.flipud(x_copy[i])], axis=0)
            for j in range(2):
                y_train = np.append(y_train, 5)
        ros += 1

indices = np.random.permutation(len(x_train))
x_train = x_train[indices]
y_train = y_train[indices]

f = open("dir../after_aug/x_train", "wb")
pickle.dump(x_train, f)
f.close()
f = open("dir../after_aug/y_train", "wb")
pickle.dump(y_train, f)
f.close()

f = open("dir../after_aug/x_val", "wb")
pickle.dump(x_val, f)
f.close()
f = open("dir../after_aug/y_val", "wb")
pickle.dump(y_val, f)
f.close()

f = open("dir../after_aug/x_test", "wb")
pickle.dump(x_test, f)
f.close()
f = open("dir../after_aug/y_test", "wb")
pickle.dump(y_test, f)
f.close()
