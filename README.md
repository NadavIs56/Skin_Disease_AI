#  <p align ="center" height="40px" width="40px"> Skin Disease AI </p>
##  <p align ="center" height="40px" width="40px"> Skin Lesion Diagnosis using Machine Learning </p>

<p align ="center">
<a href="https://www.python.org/" target="_blank" rel="noreferrer">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" width="32" height="32" /></a>
<a href="https://opencv.org/" target="_blank" rel="noreferrer">   <img src="https://opencv.org/wp-content/uploads/2022/05/logo.png" width="32" height="32" /></a>  
<a href="https://keras.io/" target="_blank" rel="noreferrer">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keras_logo.svg/1200px-Keras_logo.svg.png" width="32" height="32" /></a> 
<a href="https://www.tensorflow.org/" target="_blank" rel="noreferrer">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Tensorflow_logo.svg/115px-Tensorflow_logo.svg.png?20170429160244" width="32" height="32" /></a> 
<a href="https://scikit-learn.org/stable/" target="_blank" rel="noreferrer">   <img src="https://e7.pngegg.com/pngimages/309/384/png-clipart-scikit-learn-python-computer-icons-scikit-machine-learning-learning-text-orange.png" width="32" height="32" /></a>  
<a href="https://numpy.org/" target="_blank" rel="noreferrer">   <img src="https://numpy.org/images/logo.svg" width="32" height="32" /></a>  
<a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer">   <img src="https://seaborn.pydata.org/_images/logo-tall-lightbg.svg" width="32" height="32" /></a> 
</p>
	

##     <p align = "left"> Introduction </p>

Dermatological issues are increasingly common in family clinic visits, and accurate diagnosis is essential for successful treatment outcomes. Our project aims to create a system utilizing machine learning and image processing analysis to automatically diagnose six different types of skin lesions.

##     <p align = "left"> Dataset </p>
We created a large image dataset for six skin lesion types by combining public dermatologist datasets with images that we collected ourselves. Our dataset contains a total of 1,952 images.

##     <p align = "left"> Model </p>
We used the Xception architecture to build our skin lesion diagnosis model. Our model was trained on the entire dataset, and we used data augmentation to generate additional images for classes with a lack of images.
Our best model achieved an accuracy of 87% on the test set. We also evaluated our model using various metrics, including the confusion matrix, accuracy and loss histograms, and classification report.


##     <p align = "left"> Our project consists of the following files: </p>
•	preprocessing.py: This code loads the entire dataset, perform the required image preprocessing, and splits the images into train, validation and test sets.

•	sets_visualization.py: This code used to show the distribution of the different skin lesions' types through the train, validation and test sets.

•	augmentation.py: Code for adding augmented images to our dataset for classes with a lack of images.

•	model.py: The code we used to build our Xception model for skin lesion diagnosis.

•	evaluate.py: Code for evaluating our model for fine-tuning and better understanding. It shows the confusion matrix, accuracy and loss histograms, and classification  report.

•	predict.py: Code for prediction a batch of images from a directory, using our model. 



