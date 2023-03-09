from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import(
    Message
)
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect

          


# Create your views here.
def Home(request):

    user = request.user
    users = User.objects.exclude(pk=request.user.pk)
    message_counts = []

    if request.user.is_authenticated:
        for reciever in users:
            num_messages = Message.objects.filter(sender=reciever, reciever=user, is_seen=False).count()
            message_counts.append(num_messages)
    
    user_data = zip(users, message_counts)
    context = {
        "users":user_data,
    }
    return render(request, 'home.html', context)






def CreateAcoount(request):


    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.create_user(username,email,password)
            user.save()
            return redirect("/") 
        except:
            return redirect("create_account")         
    else:
        messages.error(request,"The username already exist!")
        return render(request, 'create_account.html')


def Login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            messages.success(request," You can order any Kind of websie you required!")
            return redirect("/")
        else:
            messages.error(request,"You don't have any account,Please create an account!")
            return redirect("/")

    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect("/")



def Messaging(request, pk):
    senderUser = get_object_or_404(User, pk=request.user.pk)
    reciverUser = get_object_or_404(User, pk=pk)

    messages = Message.objects.filter(
        (Q(sender=senderUser) & Q(reciever=reciverUser)) | (Q(sender=reciverUser) & Q(reciever=senderUser))
    ).order_by('date')
  
    for message in messages:
        if message.reciever == senderUser:
            message.is_seen = True
        
        message.save()
 

    context = {
        'sender': senderUser,
        'receiver': reciverUser,
        'messages': messages,
        "messages_count":messages.count()
    }
    return render(request, 'messaging.html', context)



def SendMessage(request, pk):

    print("testing-----------------------------------------------------")
    message = request.POST.get('messages')
    print(message)
    senderUser = get_object_or_404(User, pk=request.user.pk)
    reciverUser = get_object_or_404(User, pk=pk)

    print("=====================================================")
    print(message)

    new_message = Message(value=message, sender=senderUser, reciever=reciverUser)
    new_message.save()
    message_values = Message.objects.all().values()
    message_data = list(message_values)

    context = {
        'status':'Save',
        'message_data':message_data
    }
    return JsonResponse(context)

def GetMessage(request,pk):

    senderUser = get_object_or_404(User, pk=request.user.pk)
    reciverUser = get_object_or_404(User, pk=pk)

    messages = Message.objects.filter(
        (Q(sender=senderUser) & Q(reciever=reciverUser)) | (Q(sender=reciverUser) & Q(reciever=senderUser))
    ).order_by('date')

    messagesList = list(messages.values())
    
    context = {
        "messagesList":messagesList
    }

    return JsonResponse(context)






def GetUser(request):
    user = request.user
    users = User.objects.exclude(pk=request.user.pk)
    message_counts = []
    user_list = []

    for reciever in users:
        num_messages = Message.objects.filter(sender=reciever, reciever=user, is_seen=False).count()
        user_dict = {
            "id": reciever.id,
            "username": reciever.username,
            "message_count": num_messages
        }
        user_list.append(user_dict)
    
    
    context = {
        "users":user_list,
    }
    return JsonResponse(context)