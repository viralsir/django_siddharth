from django import forms
from django.shortcuts import render

tasks=["check email","paid bill","check bank balance"]


class NewTaskForm(forms.Form):
    task=forms.CharField(label="new Task ")
    priority=forms.IntegerField(label="Priority :",min_value=2,max_value=10)
    

# Create your views here.
def index(request):
    return render(request,"task/index.html",{
        'tasks':tasks
    })

def add(request):
    return render(request,"task/add.html",{
        "form":NewTaskForm()
    })