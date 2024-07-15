from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponse

# Create your views here.

@login_required
@login_required
def chat_view(request, chatroom_name='public-chat'):
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    chat_messages = chat_group.chat_messages.all().order_by("created")[:30]
    form = ChatmessageCreateForm()




    if request.method == "POST":
        form = ChatmessageCreateForm(request.POST)

        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            
            context = {
                "message" : message,
                "user" : request.user    
            }
                        
            return render(request=request,template_name="partials/chat_message_p.html", context=context)



    return render(request,"a_rtchat/chat.html", {"chat_messages":chat_messages, "form":form})