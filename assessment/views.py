from django.http import HttpResponse
from django.template import loader

from .models import Question, Assessment

def index(_):
    template = loader.get_template("assessment/index.html")
    return HttpResponse(template.render())

def detail(request, assessment_id):
    try:
        assessment = Assessment.objects.get(pk=assessment_id)
    
        latest_question_list = Question.objects.filter(assessment_id=assessment_id).order_by("created_at")
        
        template = loader.get_template("assessment/detail/index.html")
        context = {
            "latest_question_list": latest_question_list,
            "assessment": assessment,
        }
        return HttpResponse(template.render(context, request))
    except Assessment.DoesNotExist:
        return HttpResponse("Assessment does not exist")

def question(request, assessment_id, question_id):
    q = Question.objects.get(pk=question_id, assessment_id=assessment_id)
    template = loader.get_template("question/index.html")
    context = {
        "question": q,
    }
    return HttpResponse(template.render(context, request))

def result(request, assessment_id):
    template = loader.get_template("assessment/result/index.html")
    context = {
        "assessment_id": assessment_id,
    }
    return HttpResponse(template.render(context, request))
