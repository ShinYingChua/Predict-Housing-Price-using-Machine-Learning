# Predict Housing Price using ML
This machine learning model, trained on the housing price prediction dataset, is able to help people to make informed decisions when buying a new house.
The dataset contains 13 features and it is provided by deepakshi_mahajan.

## 1) Overview of the folder structure
    .
    ├── .github                   
    ├── src
         └── mlp.py 
    ├── eda.ipynb                     
    ├── requirements.txt                    
    ├── run.sh                   
    └── README.md
    
## 2) Key findings from EDA
- There are presence of null data
- Types of variables present: Categorical, Integer and Float
- TotalBsmtSF exhibits strong correlation with SalePrice

## 3) Choices made in pipeline based on findings
- Data cleaning is required as the data is dirty

## 4) Choice of ML models
- Linear Regression Model
    - Supervised machine learning algorithm
    - A linear model that quantitatively relates to house prices with variables
- Random Forest Regression Model
    - Supervised machine learning algorithm
    - Combine mutiple decision trees to make decision
    - It can handle a large number of input features and automatically select the most relevant ones
    - It is robust to outliers and noisy data
    - It provides estimates of feature importance, allowing interpretation of the model.

## 5) Evaluation of ML Models
Linear Regression Model gives better accuracy as the mean absolute error is lower.
<img width="551" alt="image" src="https://github.com/ShinYingChua/Predict-Housing-Price-using-Machine-Learning/assets/101923627/37add8fe-10c5-4e9c-90a4-89c5910f2552">



