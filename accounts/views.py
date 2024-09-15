from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def acconts_top(request):
    return HttpResponse('アカウントのTOPページ')