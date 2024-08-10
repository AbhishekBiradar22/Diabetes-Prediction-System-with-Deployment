import os,sys
import pandas as pd
import numpy as np
from scipy import stats
# Importing all the packages
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
print(os.getcwd())

df=pd.read_csv(r'C:\Users\Abhishek Biradar\Deployment\Saving_model\new_die.csv')

df['Dummy']='A'
print(df.head())
## Seperating Dependent and Independent Variables 
x=df.drop('Is_Diabetic',axis=1)
y=df['Is_Diabetic']

y=y.map({'NO':0,'YES':1})
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y)

# To build a numerical pipeline 
numerical_processor = Pipeline(steps=[('Imputer',SimpleImputer(strategy='mean')),
                                      ('Scaler',StandardScaler())                                      
                                     ])


# To build a Categorical pipeline 
categorical_processor = Pipeline(steps=[('Imputer',SimpleImputer(strategy='most_frequent')),
                                       ('Encoding',OneHotEncoder()
                                        )])

# To find list of numerical and Categorical Variables 
df_num=x.select_dtypes(include='number')
df_cat=x.select_dtypes(include='object')


final_preprocessor = ColumnTransformer(transformers=[('numerical',numerical_processor,[' No.of_times_pregnant', 'glucose_conc', 'blood_pressure',
       'skin_fold_thickness', '2-Hour_serum_insulin', 'BMI',
       'Diabetes_pedigree_fn', 'Age']), ('categorical',categorical_processor,['Dummy'])
                                                 ])


final_pipeline = make_pipeline(final_preprocessor,LogisticRegression())

final_pipeline
final_pipeline.fit(x_train,y_train)

print('info')

#joblib or pickle
#saving the model
import joblib
joblib.dump(final_pipeline,'model_save_j.pkl')
print('info')

import pickle
pickle.dump(final_pipeline,open('model_save_p.pkl',))
print('info)')