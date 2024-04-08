#  <p align ="center" height="40px" width="40px"> Skin Disease AI </p>
##  <p align ="center" height="40px" width="40px"> Skin Lesion Diagnosis using Machine Learning </p>


### <p align ="center"> Implemented using: </p>
<p align ="center">
<a href="https://www.python.org/" target="_blank" rel="noreferrer">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" width="32" height="32" /></a>
<a href="https://opencv.org/" target="_blank" rel="noreferrer">   <img src="https://opencv.org/wp-content/uploads/2022/05/logo.png" width="32" height="32" /></a>  
<a href="https://keras.io/" target="_blank" rel="noreferrer">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keras_logo.svg/1200px-Keras_logo.svg.png" width="32" height="32" /></a> 
<a href="https://www.tensorflow.org/" target="_blank" rel="noreferrer">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Tensorflow_logo.svg/115px-Tensorflow_logo.svg.png?20170429160244" width="32" height="32" /></a> 
<a href="https://scikit-learn.org/stable/" target="_blank" rel="noreferrer">   <img src="https://e7.pngegg.com/pngimages/309/384/png-clipart-scikit-learn-python-computer-icons-scikit-machine-learning-learning-text-orange.png" width="32" height="32" /></a>  
<a href="https://numpy.org/" target="_blank" rel="noreferrer">   <img src="https://numpy.org/images/logo.svg" width="32" height="32" /></a>  
<a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer">   <img src="https://seaborn.pydata.org/_images/logo-tall-lightbg.svg" width="32" height="32" /></a> 
<a href="https://streamlit.io/" target="_blank" rel="noreferrer">   <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width="32" height="32" /></a> 
<a href="https://matplotlib.org/" target="_blank" rel="noreferrer">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/2048px-Created_with_Matplotlib-logo.svg.png" width="32" height="32" /></a> 
</p>

<br><br>
### <p align ="center"> Do remember to star ⭐ the repository if you like what you see!</p>
<p align="center">
  <img src="https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99" alt="Star Badge"/> 
  <a href="https://github.com/NadavIs56/Skin_Disease_AI/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/NadavIs56/Skin_Disease_AI"></a>
</p>
<br><br>
           
###     <p align = "center"> You can access the web version at https://teledermatologis-ai.streamlit.app/ </p>
###     <p align = "center"> Check out the project paper at https://ieeexplore.ieee.org/abstract/document/10402645 </p>
####     <p align = "center"> I would appreciate hearing your thoughts on it. Thank you! </p>

<br>

#### <p align = "center"> Welcome to Skin Disease AI, an advanced system designed to recognize and diagnose skin diseases using machine learning and image processing techniques. This project offers an AI solution that can significantly assist in the diagnostic process of six different types of skin lesions.</p>

<br>

##     <p align = "left"> 🎯 Introduction </p>

Skin conditions are a common reason for clinic visits, with an accurate diagnosis being crucial for effective treatment. This project presents a robust machine learning system that analyzes images to identify and diagnose different types of skin lesions.

<br>

##     <p align = "left"> 📚 Dataset </p>
The dataset for this project consists of a total of 1,657 images. These images represent 6 types of skin lesion classes and 1 non-skin lesion class, gathered from public dermatologist datasets and self-collected sources.

<br>

##     <p align = "left"> 🤖 Model </p>
We utilized the Xception architecture to create our skin lesion diagnosis model. Trained on the complete dataset, we enhanced our training with data augmentation for classes with fewer images. Our model achieved an impressive 92% accuracy on the test set. In addition, we assessed our model using various metrics, including the confusion matrix, accuracy and loss histograms, and a comprehensive classification report.

<br>

##     <p align = "left"> 📂 Repository Structure </p>
 -  'preprocessing.py': This code loads the entire dataset, perform the required image preprocessing, and splits the images into train, validation and test sets.

 -  'sets_visualization.py': This code used to show the distribution of the different skin lesions' types through the train, validation and test sets.

 -  'augmentation.py': Code for adding augmented images to our dataset for classes with a lack of images.

 -  'model.py': The code we used to build our Xception model for skin lesion diagnosis.

 -  'evaluate.py': Code for evaluating our model for fine-tuning and better understanding. It shows the confusion matrix, accuracy and loss histograms, and classification  report.

 -  'predict.py': Code for prediction a batch of images from a directory, using our model. 

<br>

### <p align ="center"> Do remember to star ⭐ the repository if you like what you see!</p>

---


<div align="center">
  Made with ❤️ by <a href="https://github.com/NadavIs56">Nadav Ishai</a>
</div>
