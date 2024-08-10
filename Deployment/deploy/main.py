from flask import Flask,render_template,request
import joblib,os
import pandas as pd
app=Flask(__name__)

model=joblib.load(r'C:\Users\Abhishek Biradar\Deployment\Saving_model\model_save_j.pkl')


@app.route('/')
def home():
   # return 'Welcome to my page'
   return render_template('home.html')

@app.route('/demo')
def demo():
    return 'Welcome to Demo'


@app.route('/predict',methods=['post'])
def predict():
    val1=float(request.form.get('preg'))
    val2=float(request.form.get('glucose'))
    val3=float(request.form.get('BP'))
    val4=float(request.form.get('thickness'))
    val5=float(request.form.get('Insulin'))
    val6=float(request.form.get('BMI'))
    val7=float(request.form.get('dbfun'))
    val8=float(request.form.get('age'))
    val9=request.form.get('dummy')
    #print(val1)
    #return 'PLEASE WAIT'
    val=[{' No.of_times_pregnant':val1 ,'glucose_conc':val2, 'blood_pressure':val3,'skin_fold_thickness':val4,  
     '2-Hour_serum_insulin':val5, 
      'BMI':val6, 'Diabetes_pedigree_fn':val7, 'Age':val8, 'Dummy':val9}] 
 
    df=pd.DataFrame(val) 
    result=model.predict(df) 
    # if result[0]==0: 
    #     return 'you are not diabetic' 
    # else :
    #     return 'Diabetic' 
    # return render_template ('after.html')
    return render_template('after.html' ,ot=result)


app.run()