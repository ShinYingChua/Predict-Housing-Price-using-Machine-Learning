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
