import pandas as pd
import joblib
import pickle
import os
# loading the saved model
#os.chdir(r'C:\Users\Abhishek Biradar\Deployment\Saving_model\model_save_j.pkl')
print(os.getcwd())
model=joblib.load(r'C:\Users\Abhishek Biradar\Deployment\Saving_model\model_save_j.pkl')

# val=[{' No.of_times_pregnant':1 ,'glucose_conc':85,'blood_pressure':66,'skin_fold_thickness':29, 
#       '2-Hour_serum_insulin':0,
#        'BMI':26.6,'Diabetes_pedigree_fn':0.351,'Age':31,'Dummy':'A'}]
# df=pd.DataFrame(val)
# print(model.predict(df))  #0/no


# val1=[{' No.of_times_pregnant':6 ,'glucose_conc':148,'blood_pressure':72,'skin_fold_thickness':35, 
#       '2-Hour_serum_insulin':0,
#        'BMI':33.6,'Diabetes_pedigree_fn':0.627,'Age':50,'Dummy':'A'}]
# df=pd.DataFrame(val1)
# print(model.predict(df))   #1/yes

# val2=[{' No.of_times_pregnant':8 ,'glucose_conc':109,'blood_pressure':76,'skin_fold_thickness':39, 
#       '2-Hour_serum_insulin':114,
#        'BMI':27.9,'Diabetes_pedigree_fn':0.64,'Age':31,'Dummy':'A'}]
# df=pd.DataFrame(val2)
# print(model.predict(df)) #0/yes


# val3=[{' No.of_times_pregnant':3 ,'glucose_conc':111,'blood_pressure':62,'skin_fold_thickness':0, 
#       '2-Hour_serum_insulin':0,
#        'BMI':22.6,'Diabetes_pedigree_fn':0.142,'Age':21,'Dummy':'A'}]
# df=pd.DataFrame(val3)
# print(model.predict(df)) #0/no

# val4=[{' No.of_times_pregnant':3 ,'glucose_conc':107,'blood_pressure':62,'skin_fold_thickness':13, 
#       '2-Hour_serum_insulin':48,
#        'BMI':22.9,'Diabetes_pedigree_fn':0.678,'Age':23,'Dummy':'A'}]
# df=pd.DataFrame(val4)
# print(model.predict(df))  #0/yes


# val5=[{' No.of_times_pregnant':4 ,'glucose_conc':109,'blood_pressure':64,'skin_fold_thickness':44, 
#       '2-Hour_serum_insulin':99,
#        'BMI':34.8,'Diabetes_pedigree_fn':0.905,'Age':26,'Dummy':'A'}]
# df=pd.DataFrame(val5)
# print(model.predict(df)) #0/yes

# val6=[{' No.of_times_pregnant':4 ,'glucose_conc':148,'blood_pressure':60,'skin_fold_thickness':27, 
#       '2-Hour_serum_insulin':318,
#        'BMI':30.9,'Diabetes_pedigree_fn':0.15,'Age':29,'Dummy':'A'}]
# df=pd.DataFrame(val6)
# print(model.predict(df))  #0/Yes


# val6=[{' No.of_times_pregnant':7 ,'glucose_conc':179,'blood_pressure':95,'skin_fold_thickness':31, 
#       '2-Hour_serum_insulin':0,
#        'BMI':34.2,'Diabetes_pedigree_fn':0.164,'Age':60,'Dummy':'A'}]
# df=pd.DataFrame(val6)
# print(model.predict(df))  #1/no


# val6=[{' No.of_times_pregnant':0 ,'glucose_conc':147,'blood_pressure':85,'skin_fold_thickness':54, 
#       '2-Hour_serum_insulin':0,
#        'BMI':42.8,'Diabetes_pedigree_fn':0.375,'Age':24,'Dummy':'A'}]
# df=pd.DataFrame(val6)
# print(model.predict(df))  #1/no


# val7=[{' No.of_times_pregnant':5 ,'glucose_conc':11,'blood_pressure':72,'skin_fold_thickness':28, 
#       '2-Hour_serum_insulin':0,
#        'BMI':23.9,'Diabetes_pedigree_fn':0.407,'Age':27,'Dummy':'A'}]
# df=pd.DataFrame(val7)
# print(model.predict(df))  #0/no