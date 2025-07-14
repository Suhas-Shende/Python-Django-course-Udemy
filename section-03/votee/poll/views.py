from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from poll.models import *
# Create your views here.
# def index(request):
#     # top_five_questions=Questions.objects.all()
#     top_two_questions=Questions.objects.order_by('-pub_date')[:2]  #THis will order the query result
  
#     return HttpResponse("-".join([str(question.text) for question in top_two_questions]))  



def index(request):
    # top_five_questions=Questions.objects.all()
    top_two_questions=Questions.objects.order_by('-pub_date')[:5]  #THis will order the query result
    template=loader.get_template('poll/index.html')
    context={'latest_poll':top_two_questions}
    return HttpResponse(template.render(context,request))  

def detail(request, question_id):
    # try:
    #    question=Questions.objects.get(pk=question_id)
    # except Questions.DoesNotExist:
    #     raise Http404("404 Page not found")
    question=get_object_or_404(Questions,pk=question_id)
    context={"question":question}
    return render(request,'poll/detail.html',context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)