# Extramarital affair prediction

## Installation Guide
1. Clone or Fork the Project
2. Create a Virtual Enviroment
3. go to same virtual enviroment and write below cmd
4. pip install -r requirements.txt


### 1. Project Description
#### A. Problem Statement
The dataset I chose is the affairs dataset that comes with Stats models. It was derived from a survey of women in 1974 by Red book magazine, in which married women were asked about their participation in extramarital affairs.I decided to treat this as a classification problem by creating a new binary variable affair (did the woman have at least one affair?) and trying to predict the classification for each woman.

#### B. Tools and Libraries
Tools<br><br>
a.Python<br>
b.Jupyter Notebook<br>
c. Flask<br>
d. HTML<br>
e. Render<br>
f. GitHub

Libraries<br><br>
a.Pandas<br>
b.Scikit Learn<br>
c.Numpy<br>
d.Seaborn<br>
e.Matpoltlib<br>

### 2. Data Collection

The dataset contains 6366 observations of 9 variables:<br>
rate_marriage: woman rating of her marriage (1 = very poor, 5 = very good)<br>
age: woman age<br>
yrs_married: number of years married<br>
children: number of children<br>
religious: woman rating of how religious she is (1 = not religious,4 =strongly religious)<br>
educ: level of education (9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 17 = some graduate school, 20 = advanced degree)<br>
occupation: woman occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = white collar, 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree) <br>
occupation_husb: husband occupation (same coding as above) <br>
affairs: time spent in extra-marital affairs

### 3. EDA
#### A.Data Cleaning
We have 13 columns and no column contain any null values<br>
All columns are numerical also
Dependent Variable is time spent in extra-marital affairs since it is Classification problem we convert it to 1 or 0

#### B. Feature Engineering
No outliers are present in the data

#### C. Data Normalization
Normalization (min-max Normalization)<br>
In this approach we scale down the feature in between 0 to 1

we have numerical column where we can apply min-max Normalization.<br>

### 4. Choosing Best ML Model
List of the model that we can use for our problem<br>
a. Logistic Regression model<br>

### 5. Model Creation
So,using a Logistic Regresssion we got good accuracy of 73%, we can Hyperparameter tuning for best accuracy.

Algorithm that can be used for Hyperparameter tuning are :-

a. GridSearchCV<br>
b. RandomizedSearchCV<br>

Main parameters used by Logistic Regression Algorithm are :-

a. alpha ---> Alpha is a positive constant that multiplies the regularization terms. It controls the overall strength of regularization applied to the model.
b. l1_ratio ---> l1_ratio is the mixing parameter that controls the balance between L1 (Lasso) and L2 (Ridge) penalties in Elastic Net regularization.

### 6. Model Deployment
After creating model ,we integrate that model with beautiful UI. for the UI part we used HTML and Flask. We have added extra validation check also so that user doesn't enter Incorrect data. Then the model is deployed on render

### 7. Model Conclusion

Model predict 73% accurately on test data.

### 8. Project Innovation
a. Easy to use<br>
b. Open source<br>
c. Best accuracy<br>
d. GUI Based Application

### 9. Limitation And Next Step
Limitation are :-<br>
a. Mobile Application<br>
b. Accuracy can be improved more<br>
d. Feature is limited

Next Step are :-<br>
a. we can work on mobile application<br>

## Deployable Link
https://machine-learning-practical-02.onrender.com/predict