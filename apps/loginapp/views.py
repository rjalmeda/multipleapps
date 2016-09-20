from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users


# Create your views here.
def index(request):
    return render(request, 'loginapp/index.html')

def register(request):
    if request.method == 'POST':
#        first_name = request.POST['first_name']
#        last_name =  request.POST['last_name']
#        email = request.POST['email']
#        password = request.POST['password']
#        confirmpw = request.POST['confirmpw']
#        user = Users.userManager.register(first_name, last_name, email, password, confirmpw)
#        if user == 1:
#            print 'Failed to register'
#            messages.add_message(request, messages.ERROR, 'Email is blank')
#            return redirect('/')
#        elif user == 2:
#            print 'Failed to register'
#            messages.add_message(request, messages.ERROR, 'Email is not valid')
#            return redirect('/')
#        elif user == 3:
#            print 'Failed to register'
#            messages.add_message(request, messages.ERROR, 'First name is empty')
#            return redirect('/')
#        elif user == 4:
#            print 'Failed to register'
#            messages.add_message(request, messages.ERROR, 'Last name is empty')
#            return redirect('/')
#        elif user == 5:
#            print 'Failed to register'
#            messages.add_message(request, messages.ERROR, 'Password is empty')
#            return redirect('/')
#        elif user == 6:
#            print 'Failed to register'
#            messages.add_message(request, messages.ERROR, 'Password does not match')
#            return redirect('/')
#        elif user == 7:
#            print 'Failed to register'
#            messages.add_message(request, messages.ERROR, 'Duplicate email found')
#            return redirect('/')
#        elif user == True:
#            print 'Success'
#            messages.add_message(request, messages.SUCCESS, 'User successfully registered')
#            request.session['first_name'] = first_name
#            request.session['user'] = email
#            return redirect('/success')
#    else:
#        return render(request, 'index.html')

        user = Users.userManager.register(request.POST)
        print user
        if user['success']:
            request.session['user'] = request.POST['first_name']
            for message in user['success']:
                messages.add_message(request,messages.SUCCESS,message)
            return redirect('/success')
        
        else: 
            for message in user['errors']:
                messages.add_message(request,messages.ERROR, message)
            return redirect('/')
    else:
        return redirect('/')
def login(request):
    if request.method == 'POST':
        login = Users.userManager.login(request.POST)
        print login
        if login['success']:
            request.session['user'] = Users.userManager.get(email=request.POST['email']).first_name
            for message in login['success']:
                messages.add_message(request,messages.SUCCESS,message)
            return redirect('/success')
        else:
            for message in login['errors']:
                messages.add_message(request,messages.ERROR, message)
            return redirect('/')
    else:
        return redirect('/')

def success(request):
    context = {}
    allusers = Users.userManager.all()
    context['allusers'] = allusers
    return render(request, 'loginapp/success.html', context)