from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos' : todos}
    return render(request, 'My_Todo_App/index.html', content)        # html 파일을 user에게 보여주기 위하여 render 함수 사용


def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("Create Todo! =>" + user_input_str)                     # user에게 해당 메시지를 출력해줌.

def doneTodo(request):
    done_Todo_id = request.GET['todoNum']
    print("완료한 todo의 id -> ", done_Todo_id)
    todo = Todo.objects.get(id = done_Todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))