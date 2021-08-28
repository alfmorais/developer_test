from django.db import models


# Create your models here.
# This class are our database models regarding survey
class Survey(models.Model):
    """
    This class will created a survey name in our database
    """
    survey_id = models.AutoField(primary_key=True)
    survey_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.survey_name)


class SurveyQuestion(models.Model):
    """
    This class will created a survey question in our database
    """
    survey = models.ForeignKey('Survey', on_delete=models.CASCADE)
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255)

    def __str__(self):
        return str(self.question)


class SurveyQuestionAlternative(models.Model):
    """
    This class will created a question alternative for our survey question
    """
    survey_question = models.ForeignKey(
        'SurveyQuestion', on_delete=models.CASCADE
    )
    first_alternative = models.CharField(max_length=255)
    second_alternative = models.CharField(max_length=255)
    third_alternative = models.CharField(max_length=255)

    def __str__(self):
        return str(self.survey_question)


class SurveyUserAnswer(models.Model):
    """
    This class will created a answer for our survey question
    """
    ALTERNATIVE_CHOICES = (
        ("a)", "FIRST ALTERNATIVE"),
        ("b)", "SECOND ALTERNATIVE"),
        ("c)", "THIRD ALTERNATIVE"),

    )
    user_answer = models.ForeignKey(
        'SurveyQuestionAlternative',
        on_delete=models.CASCADE
    )
    user_choice = models.CharField(
        max_length=255,
        choices=ALTERNATIVE_CHOICES,
        blank=False,
        null=False
    )

    def __str__(self):
        return str(self.user_answer)
