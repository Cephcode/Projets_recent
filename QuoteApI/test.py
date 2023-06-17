from PyQt5.QtWidgets import *
import requests
import sys 
from time import *
app=QApplication(sys.argv)
window=QMainWindow()
window.setStyleSheet("background-color:beige")

# points_de_vie=2000
points=[0]
new=[]
def vie(list):
    last=list[len(list)-1]
    last+=1
    list.append(last)
    list==list
    print(list[len(list)-1])
    return list[len(list)-1]
def call():
    data = requests.get("http://127.0.0.1:8000/").json()
    print(data)
    return data["quoteText"],data["quoteAuthor"],vie(points)
text_box=QLabel(window)
text_box.setStyleSheet("color:black;font-size:20px")
btn=QPushButton("click",window)
btn.clicked.connect(call)
text_box.setText(f"{call()}")
text_box.setGeometry(300,250,900,50)
text_box.setWordWrap(True)
window.showMaximized()
window.update(0,0,1000,1000)
app.exec_()