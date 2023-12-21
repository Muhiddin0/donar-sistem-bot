
import asyncio
import json
from django.shortcuts import render
from threading import Thread
from django.contrib import messages
from user.models import TempUser, User
import datetime


from pyrogram import Client

from config.settings import (
    ADMIN,
    BOT_TOKEN as bot_token,
    API_ID as api_id, API_HASH as api_hash
    )


async def task(**kwargs):
    async with Client('mySession', api_hash=api_hash, api_id=api_id, bot_token=bot_token) as app:
        
        print('-----------------')
        print(kwargs)
        print('-----------------')

        if 'user_pk' in kwargs:
            user = User.objects.filter(id=kwargs['user_pk'])
        elif 'users' in kwargs:
            user = [
                User.objects.get(id=i) for i in kwargs['users']
            ]
            print('men ishladim')
        else:
            user = User.objects.all()

        today = datetime.date.today()

        for i in user:
            file_name = str(today) + "-" + str(i.user_id)
            if kwargs['name'] is not None:
                await app.send_document(
                    i.user_id, document=kwargs['name'],
                    caption=kwargs['message'],
                    file_name=file_name
                )
            elif kwargs["message"] is not None:
                await app.send_message(chat_id=i.user_id, text=kwargs['message'])

def async_callback(**kwargs):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(task(**kwargs))
    loop.close()

# Create your views here.
def index(request):

    if request.method == 'GET':
        users = User.objects.all()

        context = {
            "users":users
        }

        return render(request, 'layouts/main.html', context)

    if request.method == 'POST':
        data = request.POST
        region = data.get('region')
        organizations = data.get('organizations')
        position = data.get('position')
        
        if region and organizations and position:
            users = User.objects.filter(
                region=region,
                organizations=organizations,
                position=position
            )

        elif region and organizations:
            users = User.objects.filter(
                region=region,
                organizations=organizations,
            )
        
        elif region and position:
            users = User.objects.filter(
                region=region,
                position=position
            )

        elif organizations and position:
            users = User.objects.filter(
                region=region,
                organizations=organizations,
            )

        elif organizations:
            users = User.objects.filter(
                organizations=organizations,
            )
        elif position:
            users = User.objects.filter(
                position=position,
            )
        elif region:
            users = User.objects.filter(
                region=region,
            )
        else:
            users = []
        
        context = {
            "users":users,
        }

        return render(request, 'layouts/filter.html', context)
        
def verifay(request):
    if request.method == "GET":
        rusers = TempUser.objects.filter(reject=True)
        tusers = TempUser.objects.filter(reject=False)

        context = {
            "tusers":tusers,
            "rejects":rusers
        }

        print(rusers)

        return render(request, 'layouts/verifay.html', context)

    if request.method == "POST":
        id = request.POST.get('id')
        status = request.POST.get('status')
        
        tuser = TempUser.objects.get(id=id)
        if status == 'accept':
            
            print(tuser.name)
            print(tuser.phone)
            print(tuser.region)
            print(tuser.organizations)
            print(tuser.position)

            User.objects.create(
                name=tuser.name,
                phone=tuser.phone,
                region=tuser.region,
                organizations=tuser.organizations,
                position=tuser.position,
                user_id=tuser.user_id,
            )
            tuser.delete()
        else:
            tuser.reject = True
            tuser.save()

        rusers = TempUser.objects.filter(reject=True)
        tusers = TempUser.objects.filter(reject=False)

        print(rusers)

        context = {
            "tusers":tusers,
            "rejects":rusers
        }

        return render(request, 'layouts/verifay.html', context)

def details(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "GET":
        context = {
            'user':user
        }
        return render(request, 'layouts/details.html', context)
    if request.method == "POST":
        
        file  = request.FILES.get('content')
        message = request.POST.get('text')
        buttons = request.POST.get('buttons')
        name = None
        
        if file is not None:
            name = file.name          
            with open(name, 'wb') as localFile:
                localFile.write(file.read())

        send_message_task = Thread(target=async_callback, kwargs={
            "user_pk":pk,
            "name":name,
            "message":message,
            "buttons":buttons
        })
        send_message_task.start()
            
def xabr_yuborish(request):

    if request.method == "GET":
        return render(request, 'layouts/xabar_yuborish.html')
    
    if request.method == 'POST':
        
        
        file  = request.FILES.get('content')
        message = request.POST.get('text')
        name = None

        if file is not None:
            name = file.name          
            with open(name, 'wb') as localFile:
                localFile.write(file.read())

        send_message_task = Thread(target=async_callback, kwargs={
            "name":name,
            "message":message,
        })
        
        send_message_task.start()
            
        messages.info(request, 'Xabar yuborilmoqda...')
        return render(request, 'layouts/xabar_yuborish.html')

def send_filter(request):

    file  = request.FILES.get('content')
    message = request.POST.get('text')
    users = request.POST.get('users')
    users = json.loads(users)
    name = None

    print(type(users))
    
    for i in users:
        print(i)

    if file is not None:
        name = file.name          
        with open(name, 'wb') as localFile:
            localFile.write(file.read())
    
    send_message_task = Thread(target=async_callback, kwargs={
        "name":name,
        "message":message,
        'users':users
    })
    send_message_task.start()

    messages.success(request, 'Xabar yuborilmoqda...')
    users = User.objects.all()
    context = {
        "users":users
    }
    return render(request, 'layouts/main.html', context)
