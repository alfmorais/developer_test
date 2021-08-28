from django.contrib import admin
from .models import (Survey,
                     SurveyQuestion,
                     SurveyQuestionAlternative,
                     SurveyUserAnswer)


# Register your models here.
@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    """
    That class provide for admin interface a good reference
    from database Survey.
    """
    list_display = ('survey_id',
                    'survey_name')


@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    """
    That class provide for admin interface a good reference
    from database Survey Question.
    """
    list_display = ('survey',
                    'question_id',
                    'question')


@admin.register(SurveyQuestionAlternative)
class SurveyQuestionAlternativeAdmin(admin.ModelAdmin):
    """
    That class provide for admin interface a good reference
    from database Survey Question Alternative.
    """
    list_display = ('survey_question',
                    'first_alternative',
                    'second_alternative',
                    'third_alternative')


@admin.register(SurveyUserAnswer)
class SurveyUserAnswerAdmin(admin.ModelAdmin):
    """
    That class provide for admin interface a good reference
    from database Survey User Answer
    """
    list_display = ('user_answer',
                    'user_choice')
