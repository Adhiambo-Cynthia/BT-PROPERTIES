from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

def contact(request):
    if request.method=="POST":
        #get values
        listing=request.POST['listing']
        listing_id=request.POST['listing_id']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']

        if not email:
            messages.error(request, 'All fields required') 
            return redirect('/listings/'+ listing_id)
        else:
            if not message:
                messages.error(request, 'All fields required') 
                return redirect('/listings/'+ listing_id)
            else: 
                #check if user already made an inquiry
                if request.user.is_authenticated:
                    user_id=request.user.id
                    has_contacted=Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
                    if has_contacted:
                        messages.error(request, 'You already submitted an inquiry for this property, a realtor will get back to you!')
                        return redirect('/listings/'+ listing_id)
                    
    
#logic here is that an if statement must return, for the case of user logged in but not contacted,
#the if stmt, meets a dead end, so it chucks and executes the saving out of if stmt.
                
                contact=Contact(listing=listing, listing_id=listing_id,name=name, email=email, phone=phone, user_id=user_id, message=message)   
                contact.save()

                send_mail(
                    'BT Properties Listing Inquiry',
                    'There has been an inquiry for' + listing + '. Sign into the admin panel for more info',
                    'cinadhiambo22@gmail.com',
                    ['nderituanne0@gmail.com'],
                    fail_silently=False
                    )
                messages.success(request, 'Inquiry submitted, a realtor will get to you soon') 
                return redirect('/listings/'+ listing_id)

                
    





                

            


