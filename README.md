Skin Lesion Diagnosis using Machine Learning
Dermatological issues are increasingly common in family clinic visits, and accurate diagnosis is essential for successful treatment outcomes. Our project aims to create a system utilizing machine learning and image processing analysis to automatically diagnose six different types of skin lesions.
Dataset
We created a large image dataset for six skin lesion types by combining public dermatologist datasets with images that we collected ourselves. Our dataset contains a total of X images, with Y images for each of the six classes.
Model
We used the Xception architecture to build our skin lesion diagnosis model. Our model was trained on the entire dataset, and we used data augmentation to generate additional images for classes with a lack of images.
Our best model achieved an accuracy of 87% on the test set. We also evaluated our model using various metrics, including the confusion matrix, accuracy and loss histograms, and classification report.
Usage
Our project consists of the following files:
•	augmentation.py: This file adds augmented images to our dataset for classes with a lack of images.
•	evaluate.py: This file is used to evaluate our model for fine-tuning and better understanding. It shows the confusion matrix, accuracy and loss histograms, and classification report.
•	model.py: This file builds our Xception model for skin lesion diagnosis.
•	predict.py: This file loads our model and predicts a batch of images from a directory.
•	preprocessing.py: This file loads the entire dataset, performs the required preprocessing, and splits the data into train, validation
