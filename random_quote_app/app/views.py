from django.shortcuts import render
import requests
# Create your views here.


def load():
    data=requests.get("http://127.0.0.1/").json()
    list=[data["quoteText"],data["quoteAuthor"],data["id"]]
    return list
print(load())
def quote(request):
    data=load()
    return render(request,"index.html",{"quoteText":data[0],"quoteAuthor":data[1],"id":data[2]})
