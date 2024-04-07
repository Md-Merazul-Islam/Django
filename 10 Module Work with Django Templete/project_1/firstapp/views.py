from django.shortcuts import render

# Create your views here.
import datetime


def home(request):
    # data pass backend to frontend
    dic = {'author': 'Meraz', 'age': 20, 'list': [1, 2, 3, 4, 5, 6, 6],
           'course': [
               {
                   'Name': 'Merazul Islam',
                   'Roll': 35434,
                   'Grp': 'A',
               },
               {
                   'Name': 'Rakib',
                   'Roll': 35434534,
                   'Grp': 'B',
               },
               {
                   'Name': 'Alamin Islam',
                   'Roll': 35434,
                   'Grp': 'A',
               }
    ],
        'list1': ['python', 'is', 'fun'],
        "brith": datetime.datetime.now(),
        "nam": [
        {'name': 'Josh', 'age': 19},
        {'name': 'Dave', 'age': 22},
        {'name': 'Joe', 'age': 31},
    ],
        "somoy": datetime.datetime.now()
    }
    return render(request, "firstapp/home.html", context=dic)
