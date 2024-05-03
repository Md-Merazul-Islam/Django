from django.shortcuts import render
from datetime import datetime ,timedelta 
from django.http import HttpResponse

# Create your views here.

def home(request):
    response = render(request,'home.html')
    response.set_cookie('name','Meraz')
    response.set_cookie('name','karim',expires=datetime.utcnow()+timedelta(days=8))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request,'get_cookie.html', {'name':name})

def del_cookie(request):
    response = render(request,'del.html')
    response.delete_cookie('name')
    return 

# def set_session(request):
#     data={
#         'name': 'rahim',
#         'age':20,
#         'language':'Bangla'
#     }
#     request.session.update(data)
#     return render (request,'home.html')

def set_session(request):
    data = {
        'name': 'rahim',
        'age': 20,
        'language': 'Bangla'
    }
    request.session['my_data'] = data
    return render(request, 'home.html')

    
def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name','Guest')
        request.session.modified = True
        return render(request,'get_cookie.html', {'name':name})
    else:
        return HttpResponse('You session has been expired. Login again.')


def delete_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request,'del.html')