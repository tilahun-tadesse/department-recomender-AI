from tkinter import *

import tkinter as tk
import  pandas as pd
import os
from sklearn.tree import  DecisionTreeClassifier

from  sklearn import tree
import  joblib
# field=pd.read_csv("Book1.csv")
# field.isnull().sum()
# # print (field)
# X=field.drop(columns=["Department"])
# Y=field['Department']
#
# # my_float = float(persentage.replace(',', '').replace('%', ''))
# # field.insert(column=['Percentage'])
# model=DecisionTreeClassifier()
# model.fit(X,Y)

# def your_department(x,y,z,w):

field=pd.read_csv("Book1.csv")
field.isnull().sum()
X=field.drop(columns=["Department"])
Y=field['Department']
model=DecisionTreeClassifier()
model.fit(X,Y)
#pridict=model.predict([[x,y,z,w]])
    # model=joblib.load('student-field.joblib')
tree.export_graphviz(model,out_file='department-recomender.dot',
                     feature_names=['Entarance Result','CGPA','Overall Percentage','Gender',],
                     class_names=sorted(Y.unique()),label='all',
                     rounded=True,
                     filled=True)
    # return pridict[0]



# parent = tk.Tk()
#
# parent.geometry("600x400")
# enrance=IntVar();
# cgpa=DoubleVar();
# overall_persentage=IntVar();
# gender_input=StringVar();
# Entrance_result = tk.Label(parent, text = "Entrance_result").place(x = 150, y = 50)
# CGPA = tk.Label(parent, text = "CGPA").place(x = 150, y = 90)
# Overall_Percentage =  tk.Label(parent, text = "Overall_percentage").place(x = 150, y = 130)
# gender =  tk.Label(parent, text = "Gender").place(x = 150, y = 170)
# entry1 = tk.Entry(parent,textvariable=enrance ).place(x = 300, y = 50)
# entry2 = tk.Entry(parent,textvariable=cgpa).place(x = 300, y = 90)
#
# entry3 = tk.Entry(parent,textvariable=overall_persentage).place(x = 300, y = 130)
# entry4 = tk.Entry(parent,textvariable=gender_input).place(x = 300, y = 170)
#
# def info():
#     out=""
#     error=0
#     a=enrance.get()
#     b=cgpa.get()
#     c=overall_persentage.get()
#     d=gender_input.get()
#     if d=="male" or d=="MALE" :
#         m=1;
#     elif d=="female" or d=="FEMALE" :
#         m=0;
#     else:
#         m=2;
#     if a<0 or a>700:
#         tk.Label(parent, fg='red', text ="invalid input please enter 0-700"  ).place(x = 300, y = 70)
#         error=1
#     else:
#         tk.Label(parent, fg='#E5E4E2', text ="invalid input please enter 0-700" ).place(x = 300, y = 70)
#     if b<0 or b>4:
#         tk.Label(parent, fg='red', text ="invalid input please enter 0.0-4.0" ).place(x = 300, y = 110)
#         error=1
#     else:
#         tk.Label(parent, fg='#E5E4E2', text ="invalid input please enter 0.0-4.0" ).place(x = 300, y = 110)
#     if c<0 or c>100:
#         tk.Label(parent, fg='red', text ="invalid input please enter 0-100" ).place(x = 300, y = 149)
#         error=1
#     else:
#         tk.Label(parent, fg='#E5E4E2', text ="invalid input please enter 0-100" ).place(x = 300, y = 149)
#     if m>1 or m<0:
#         tk.Label(parent, fg='red', text ="invalid input please enter male or female" ).place(x = 300, y = 190)
#         error=1
#     else:
#         tk.Label(parent, fg='#E5E4E2', text ="invalid input please enter male or female" ).place(x = 300, y = 190)
#
#     if error!=1:
#         out= your_department(a,b,c,m);
#         # tk.Label(parent, text =out ,fg='blue'  ).place(x = 300, y = 300)
#         text=Text(parent, width=20, height=1).place(x = 300, y = 300)
#         text.insert(END, "dfadfsdf")
#         text.pack()
#
#     # elif error==1:
#     #     tk.Label(parent, text =out ,fg='#E5E4E2' ).place(x = 300, y = 300)
#
# sbmitbtn = tk.Button(parent, text = "Submit",command=info, activebackground  = "green", activeforeground = "blue").place(x = 270, y = 250)
#
# Entrance_result = tk.Label(parent, text = "Department:").place(x = 230, y = 300)
#
# parent.mainloop()
#
