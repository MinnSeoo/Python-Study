from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'My_Todo_App/index.html')        # html 파일을 user에게 보여주기 위하여 render 함수 사용
