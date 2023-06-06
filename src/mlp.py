# import libraries
import pandas as pd

# import sklearn libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

def LinearRegressionModel(X_train, X_test, y_train, y_test):
    model_LR = LinearRegression()
    model_LR.fit(X_train, y_train)
    y_pred = model_LR.predict(X_test)
    print("Linear Regression mean abs % error: ",
          mean_absolute_percentage_error(y_test, y_pred))
    
def RandomForestRegressionModel(X_train, X_test, y_train, y_test):
    model_RFR = RandomForestRegressor(n_estimators=10)
    model_RFR.fit(X_train, y_train)
    y_pred = model_RFR.predict(X_test)
    print("Random Forest Regression mean abs % error: ",
          mean_absolute_percentage_error(y_test, y_pred))
    
def main():
    dataset = pd.read_excel("HousePricePrediction.xlsx")

    # Data Cleaning
    dataset.drop(['Id'], axis=1, inplace=True)
    dataset['SalePrice'] = dataset['SalePrice'].fillna(
        dataset['SalePrice'].mean())
    new_dataset = dataset.dropna()

    # Convert categorical data into binary vectors
    df = pd.DataFrame(new_dataset)
    le = LabelEncoder()
    df['MSZoning'] = le.fit_transform(df['MSZoning'])
    df['LotConfig'] = le.fit_transform(df['LotConfig'])
    df['BldgType'] = le.fit_transform(df['BldgType'])
    df['Exterior1st'] = le.fit_transform(df['Exterior1st'])

    # Train-Test Split
    X = df.drop(["SalePrice"], axis=1)
    y = df["SalePrice"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0)

    # ML Models
    LinearRegressionModel(X_train, X_test, y_train, y_test)
    RandomForestRegressionModel(X_train, X_test, y_train, y_test)

if __name__ == '__main__':
    main()
