from django.shortcuts import render, get_object_or_404
from .models import UserMessage

def home_view(request):
    custom_hash = request.GET.get('hash')
    context = {}
    
    if custom_hash:
        try:
            user_message = UserMessage.objects.get(custom_hash=custom_hash)
            context['name'] = user_message.name
            context['message'] = user_message.message
        except UserMessage.DoesNotExist:
            context['name'] = None
            context['message'] = None
    
    return render(request, 'home.html', context)
