from django.http import HttpResponse
from django.template import loader

from assessment.utils import run_python_script_with_input, save_code_file

from .models import Question, Assessment, Submission

def detail(request, assessment_id):
    try:
        assessment = Assessment.objects.get(pk=assessment_id)
    
        latest_question_list = Question.objects.filter(assessment_id=assessment_id).order_by("created_at")
        
         # include status from is_approved method
        for question in latest_question_list:
            question.is_approved = question.is_approved()
        
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
        
        if q.is_approved():
            template = loader.get_template("success_page.html")
            context = {
                "success": {
                    "title": "Resposta correta!",
                    "message": "Parabéns! Sua resposta está correta!",
                    "redirect": "/assessment/{}".format(assessment_id),
                }
            }
            return HttpResponse(template.render(context, request))
        
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

def submit(request, assessment_id, question_id):
    try:
        answer = request.POST.get("answer")
        q = Question.objects.get(pk=question_id, assessment_id=assessment_id)
        
        file_path = 'uploads/code/{}-{}.py'.format(assessment_id, question_id)
        
        save_code_file(answer, file_path)
        
        code_result = run_python_script_with_input(file_path, q.input_text)
        is_correct = q.check_answer(code_result)
        
        Submission.objects.create(
            question=q,
            code_path=file_path,
            approved=is_correct,
        )
    
        if is_correct:
            success_template = loader.get_template("success_page.html")
            context = {
                "success": {
                    "title": "Resposta correta!",
                    "message": "Parabéns! Sua resposta está correta!",
                    "redirect": "/assessment/{}".format(assessment_id),
                }
            }
            return HttpResponse(success_template.render(context, request))
        else:
            error_template = loader.get_template("error_page.html")
            context = {
                "error": {
                    "title": "Resposta incorreta",
                    "message": "Sua resposta está incorreta. Tente novamente.",
                }
            }
            return HttpResponse(error_template.render(context, request))
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
    except Exception as e:
        template = loader.get_template("error_page.html")
        context = {
            "error": {
                "code": 500,
                "title": "Internal server error",
                "message": str(e),
            }
        }
        return HttpResponse(template.render(context, request))
