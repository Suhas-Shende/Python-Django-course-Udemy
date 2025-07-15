from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.template import loader
from poll.models import *
from django.views.generic import *
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
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, "poll/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "poll/vote.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("poll:results", args=(question.id,)))


# ------------------------------
class IndexView(ListView):
    template_name = "poll/index.html"
    context_object_name = "latest_poll"

    def get_queryset(self):
        """Return the last five published questions."""
        return Questions.objects.order_by("-pub_date")[:5]


class QDetailView(DetailView):
    model = Questions
    template_name = "poll/detail.html"
    context_object_name = "question"

class ResultsView(DetailView):
    model = Questions
    template_name = "poll/results.html"
    context_object_name = "question"

   

