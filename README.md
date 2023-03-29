#  <p align ="center" height="40px" width="40px"> Skin Lesion Diagnosis using Machine Learning </p>
##     <p align = "left"> Introduction </p>

Dermatological issues are increasingly common in family clinic visits, and accurate diagnosis is essential for successful treatment outcomes. Our project aims to create a system utilizing machine learning and image processing analysis to automatically diagnose six different types of skin lesions.

##     <p align = "left"> Dataset </p>
We created a large image dataset for six skin lesion types by combining public dermatologist datasets with images that we collected ourselves. Our dataset contains a total of 1,952 images.

##     <p align = "left"> Model </p>
We used the Xception architecture to build our skin lesion diagnosis model. Our model was trained on the entire dataset, and we used data augmentation to generate additional images for classes with a lack of images.
Our best model achieved an accuracy of 87% on the test set. We also evaluated our model using various metrics, including the confusion matrix, accuracy and loss histograms, and classification report.

Usage
Our project consists of the following files:
•	augmentation.py: Code for adding augmented images to our dataset for classes with a lack of images.
•	evaluate.py: Code for evaluating our model for fine-tuning and better understanding. It shows the confusion matrix, accuracy and loss histograms, and classification report.
•	model.py: The code we used to build our Xception model for skin lesion diagnosis.
•	predict.py: Code for prediction a batch of images from a directory, using our model. 
•	preprocessing.py: This code loads the entire dataset, perform the required image preprocessing, and splits the images into train, validation and test sets
