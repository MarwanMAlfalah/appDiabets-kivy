"""----------------------------------
Load Library for Design Main Iterface
----------------------------------"""
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

"""--------------------------------------------
Load ML Library to using a train and a test set
--------------------------------------------"""
import pandas as pd
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pandas import set_option,DataFrame

"""--------------------------------------
Detach the DATA to a train and a test set
--------------------------------------"""
filename = r'diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names, delimiter=';')
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size,random_state=seed)
model = LogisticRegression()
model.fit(X_train, Y_train)
result = model.score(X_test, Y_test)

"""-----------------------------------
Receive data user input & formatting it
-----------------------------------"""
def user_report(preg,plas,pres,skin,test,mass,pedi,age):
     pregnancies = float(preg)
     glucose = float(plas)
     bp = float(pres)
     skinthickness = float(skin)
     insulin = float(test)
     bmi = float(mass)
     dpf = float(pedi)
     age = float(age)
  
     user_report_data = {
        'pregnancies':pregnancies,
        'glucose':glucose,
        'bp':bp,
    	'skinthickness':skinthickness,
    	'insulin':insulin,
    	'bmi':bmi,
    	'dpf':dpf,
    	'age':age
	 }
     report_data = pd.DataFrame(user_report_data, index=[0])
     return report_data

"""----------------------------------
Class for call properties's interface
----------------------------------"""
class Main(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Main(name='main'))

"""------------------------------
Class main for execute our system
------------------------------"""
class MainApp(MDApp):
    def build(self):
        self.help_string = Builder.load_file('main.kv')
        return self.help_string

    def predict(self):
        input_1 = self.help_string.get_screen('main').ids.input_1.text
        input_2 = self.help_string.get_screen('main').ids.input_2.text
        input_3 = self.help_string.get_screen('main').ids.input_3.text
        input_4 = self.help_string.get_screen('main').ids.input_4.text
        input_5 = self.help_string.get_screen('main').ids.input_5.text
        input_6 = self.help_string.get_screen('main').ids.input_6.text
        input_7 = self.help_string.get_screen('main').ids.input_7.text
        input_8 = self.help_string.get_screen('main').ids.input_8.text
        
        user_result_input = user_report(input_1,input_2,input_3,input_4,
                                        input_5,input_6,input_7,input_8)
        
        user_result_model = model.predict(user_result_input)
        
        output=''
        self.help_string.get_screen('main').ids.output_text_not.text = ''
        self.help_string.get_screen('main').ids.output_text_sick.text = ''
        
        if user_result_model[0]==0:
            output = 'You are not Diabetic (Not Sick ^_^)'
            self.help_string.get_screen('main').ids.output_text_not.text = output
            
        else:
            output = 'You are Diabetic (Is Sick -_-)'
            self.help_string.get_screen('main').ids.output_text_sick.text = output
        # ^_-
"""------------------------------
Run the programm
------------------------------"""   
MainApp().run()