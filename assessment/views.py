from django.http import HttpResponse
from django.template import loader

from assessment.utils import run_python_script_with_input, save_code_file

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
        template = loader.get_template("error_page.html")
        context = {
            "error": {
                "code": 404,
                "title": "Assessment not found",
                "message": "Assessment does not exist",
            }
        }
        return HttpResponse(template.render(context, request))

def question(request, assessment_id, question_id):
    try:
        q = Question.objects.get(pk=question_id, assessment_id=assessment_id)
        template = loader.get_template("question/index.html")
        context = {
            "question": q,
        }
        return HttpResponse(template.render(context, request))
    except Question.DoesNotExist:
        template = loader.get_template("error_page.html")
        context = {
            "error": {
                "code": 404,
                "title": "Question not found",
                "message": "Question does not exist",
            }
        }
        return HttpResponse(template.render(context, request))

def result(request, assessment_id):
    template = loader.get_template("assessment/result/index.html")
    context = {
        "assessment_id": assessment_id,
    }
    return HttpResponse(template.render(context, request))

def submit(request, assessment_id, question_id):
    answer = request.POST.get("answer")
    q = Question.objects.get(pk=question_id, assessment_id=assessment_id)
    
    file_path = 'tmp/code/{}-{}.py'.format(assessment_id, question_id)
    
    save_code_file(answer, file_path)
    
    code_result = run_python_script_with_input(file_path, q.input_text)
    
    print(code_result)
   
    if q.check_answer(code_result):
        return HttpResponse("Correct answer!")
    else:
        return HttpResponse("Incorrect answer!")
