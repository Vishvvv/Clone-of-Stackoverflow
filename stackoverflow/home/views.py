from django.shortcuts import render,HttpResponse
from . import forms
from . forms import Questionanswer
from . models import Questions # for add data in database or save method so import method class from models 
# Create your views here.

def index(request):
    return render(request, "home/index.html", {})

def question(request):
    data = Questions.objects.all()
    que = {"question_no": data}
    # by above 2 lines we can show data to user from database 
    if request.method == "POST":

        form = forms.Questionanswer(request.POST)
        if form.is_valid():
            print("Validations")
            qes = form.cleaned_data['question']      
            ans = form.cleaned_data['answer']      
            print("Question:- "+ form.cleaned_data['question'])
            print("Answer:- "+ form.cleaned_data['answer'])
            queans = Questions(question = qes, answer = ans)
            # queans = Questions(id =1 , question = qes, answer = ans)  in this we can update data jiski id = 1 hai ya pk = 1 hai
            queans.save()

    return render(request, "home/forms.html", que)
    
def about(request):
    return render(request, "home/about.html",{})    

def new_question(request):
    form = forms.Questionanswer()  # Question form is put into the form variable
    return render(request, "home/new_question.html", {'form': form})    

def old_question(request):
    data = Questions.objects.all()
    que = {"question_no": data}
    return render(request, "home/old_question.html", que)    
    