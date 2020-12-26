<h1 align='center'> Classification of Handwritten Digits and GUI for Testing </h1>

## Summary

Using a SVC to classify handwritten digits to a 98.2% accuracy, this model was then deployed and used in an interactive GUI which can be seen here: https://www.youtube.com/watch?v=lJp8DtptZk4

## Project Motivation

Often information about people is collected using forms which require the user to manually fill in questions and contact information. This information is then manually entered into a system to allow for the full use of the data provided. This is a long an tedious task which cost businesses, and ensure consistent boredom for their employees. 

One step in solving this problem is to create a system that can automatically read these characters, is to develop a system capable of readin digits. Perhaps in the future I will also look at including alphabetical classification.

By using computer vision techniques combined with machine learning it has been possible to predict these digits to a 98% accuracy!


## Data Source 

Using data from Kaggle: https://www.kaggle.com/c/digit-recognizer


## Approach and Results

The first steps for this project was to analyze the data and get a feeling for important features. This was done by simple count plots to see which pixels were frequently black and which were frequently white for each digit. For this problem it is important to mention that the classes were balances.

The machine learning section looked at first developing a bench mark model which achieved an accuracy of 10%. I then tested 4 different default models to get a general understanding of performace. Both the SVC and MLP model showed promise so these were taken forwards and parameter tuning was carried out. 

The SVC with tuned parameters and five fold cross validation managed to achieve a accuracy score of 98.2% where the MLP only 96.2%.

## GUI

Once the model had been developed it was pickled and a simple GUI was built to enable users to draw digits and watch the model predict them. The model showed a 98.2% accuracy in the jupyter notebook, however, in the GUI the model accuracy is much lower, around 70-80%. I don't think the model is unable to generalize well as its variance in cross validation was small (+/-0.5%). The models reduced performace could be because the method to draw digits onto the frame doesnt represent actual handwritten digits very well.

## Model Robustness

Testing Robustness for "2":
<p align="center">
  <img src="https://github.com/RamonJWS/Classification-of-Digits-With-GUI/blob/main/Images%20for%20Robustness/2_1.PNG" width=100>
</p>


