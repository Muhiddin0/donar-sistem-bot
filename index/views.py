import io
import json
import mimetypes
import asyncio
from django.shortcuts import render
from threading import Thread
from .tasks import send_message
from django.contrib import messages
from bot.models import User

# Create your views here.
def index(request):
    '''
        Main mage
        path('',)
    '''
    user_count = User.objects.all().count()
    if request.method == 'GET':
        return render(request, 'layouts/main.html', {'user_count':user_count})



def get_file_mime_type(file):
    file_name = file.name
    mime_type, _ =  mimetypes.guess_type(file_name)
    mime_type = mime_type.split("/")[0]
    return mime_type

def async_callback(**kwargs):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_message(**kwargs))
    loop.close()

def xabr_yuborish(request):
    if request.method == "GET":
        return render(request, 'components/xabar_yuborish.html')
    elif request.method == "POST":
        text = request.POST.get('text')
        btns = json.loads(request.POST.get('buttons'))
        content = request.FILES.get("content", None)

        if content is None:
            send_message_task = Thread(target=async_callback, kwargs={'text':text, 'btns':btns, 'content':content, 'content-type':'text'})
            send_message_task.start()
            messages.info(request, 'Xabar yuborilmoqda...')
            return render(request, 'components/xabar_yuborish.html')
            
        file = io.BytesIO(content.read())
        content_type = get_file_mime_type(content)
        if not (content_type in ['image', 'video', 'audio']):
            messages.error(request, "Siz faqatgina Rasim, Video, Audio jo'nata olasiz")
            return render(request, 'components/xabar_yuborish.html')

        send_message_task = Thread(target=async_callback, kwargs={'text':text, 'btns':btns, 'file':file, 'file-name':content.name, 'content-type':content_type})
        send_message_task.start()
        messages.info(request, 'Xabar yuborilmoqda...')
        return render(request, 'layouts/xabar_yuborish.html')