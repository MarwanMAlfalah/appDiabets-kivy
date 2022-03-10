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
     pregnancies =float(preg)
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

"""------------------------
Kivy properties's interface
------------------------"""
Builder_string = '''
ScreenManager:
    Main:
<Main>:
    name : 'main'
    MDLabel:
        text: 'Smart Predict diabetes'
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H3'
        color: '#5B2160'

    MDLabel:
        text: 'pregnancies'
        pos_hint: {'center_y':0.75, 'center_x':0.75}

    MDTextField:
        id: input_1
        hint_text: '(0 - 17)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.75, 'center_x':0.7}

    MDLabel:
        text: 'glucose'
        pos_hint: {'center_y':0.68, 'center_x':0.75}

    MDTextField:
        id: input_2
        hint_text: '(0 - 200)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.68, 'center_x':0.7}

    MDLabel:
        text: 'bp'
        pos_hint: {'center_y':0.61, 'center_x':0.75}

    MDTextField:
        id: input_3
        hint_text: '(0 - 122)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.61, 'center_x':0.7}

    MDLabel:
        text: 'skinthickness'
        pos_hint: {'center_y':0.54, 'center_x':0.75}

    MDTextField:
        id: input_4
        hint_text: '(0 - 100)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.54, 'center_x':0.7}

    MDLabel:
        text: 'insulin'
        pos_hint: {'center_y':0.47, 'center_x':0.75}

    MDTextField:
        id: input_5
        hint_text: '(0 - 846)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.47, 'center_x':0.7}

    MDLabel:
        text: 'bmi'
        pos_hint: {'center_y':0.40, 'center_x':0.75}

    MDTextField:
        id: input_6
        hint_text: '(0 - 67)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.40, 'center_x':0.7}

    MDLabel:
        text: 'dpf'
        pos_hint: {'center_y':0.33, 'center_x':0.75}

    MDTextField:
        id: input_7
        hint_text: '(0.0 - 2.4)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.33, 'center_x':0.7}

    MDLabel:
        text: 'age'
        pos_hint: {'center_y':0.26, 'center_x':0.75}

    MDTextField:
        id: input_8
        hint_text: '(21 - 88)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.7}

    MDLabel:
        pos_hint: {'center_y':0.2}
        halign: 'center'
        text: ''
        id: output_text_not
        theme_text_color: "Custom"
        text_color: '#3B8BFF'
    MDLabel:
        pos_hint: {'center_y':0.2}
        halign: 'center'
        text: ''
        id: output_text_sick
        theme_text_color: "Custom"
        text_color: '#EF0F0F'
    MDLabel:
        text: "Copyright © MarwanCo. for AI 2022 ^_^"
        pos_hint: {'center_y':0.07}
        font_size: "12sp"
        line_height: .85
        halign: "center"
        color: '#5B2160'
    MDLabel:
        text: "Marwan Al-Falah -  - "
        pos_hint: {'center_y':0.04}
        color: '#5B2160'
        font_size: "11sp"
        line_height: .85
        halign: "center"
    MDLabel:
        text: "malfalah_std@kmsu.edu.ye"
        pos_hint: {'center_y':0.018}
        color: '#5B2160'
        font_size: "11sp"
        line_height: .85
        halign: "center"
    MDRaisedButton:
        pos_hint: {'center_x':0.5, 'center_y':0.13}
        text: 'Predict'
        on_press: app.predict()
'''

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
        self.help_string = Builder.load_string(Builder_string)
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
        

        user_result_marwan = user_report(input_1,input_2,input_3,input_4,
                                         input_5,input_6,input_7,input_8)

        user_result = model.predict(user_result_marwan)

        output=''
        self.help_string.get_screen('main').ids.output_text_not.text = ''
        self.help_string.get_screen('main').ids.output_text_sick.text = ''
        if user_result[0]==0:
            output = 'You are not Diabetic (Not Sick ^_^)'
            self.help_string.get_screen('main').ids.output_text_not.text = output
        else:
            output = 'You are Diabetic (Is Sick -_-)'
            self.help_string.get_screen('main').ids.output_text_sick.text = output
        print(output)
        print("Accuracy:  ",result*100.0)
         # ^_-
    
"""-------------
Run our programm
-------------"""  
MainApp().run()
