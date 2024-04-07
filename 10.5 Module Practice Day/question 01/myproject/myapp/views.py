import datetime
from django.shortcuts import render

# Create your views here.


def home(request):

    dic = {'val': [1, 2, 4, 5], "birth": datetime.datetime.now(), "val": "Hello",
           "List": [
        {'name': 'zed', 'age': 19},
        {'name': 'amy', 'age': 22},
        {'name': 'joe', 'age': 31},
    ],
        "List1": 8,
       "list2":['a','b','c'],
    }
    return render(request, "myapp/home.html", dic)
