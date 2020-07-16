from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == "POST":
        #get form values
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        #check values
        
        if User.objects.filter(username=username).exists():
                messages.error(request, 'Username unavailable') 
                return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                   messages.error(request, 'Email already exist') 
                   return redirect('register')
            else:
                if len(password) < 8: 
                        messages.error(request, 'Password need to be atleast 8 characters') 
                        return redirect('register')
                else:
                    if password != password2: 
                        messages.error(request, 'Passwords do not match') 
                        return redirect('register')
                    else:
                        #create user
                        user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email) 
                        user.save()
                        messages.success(request, 'Account successfully created') 
                        return redirect('login')
                        #login after register
                        # auth.login(request, user)
                        # messages.success(request, 'You are now logged in')
                        # return redirect('index')
                
    else:
        return render(request, "accounts/register.html")    
    
def login(request):
    if request.method == "POST":
        #get form values
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials') 
            return redirect('login')   
    else:
        return render(request, "accounts/login.html")
    
def logout(request):
    if request.method=="POST":
        auth.logout(request)
        messages.success(request, 'Logged out successfully')
        return redirect('index')
def dashboard(request):
    user_inquiries=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
   
    context={
        'inquiries': user_inquiries
    }
    return render(request, "accounts/dashboard.html", context)

