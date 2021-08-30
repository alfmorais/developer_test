from rest_framework import serializers
from .models import (Survey,
                     SurveyQuestion,
                     SurveyQuestionAlternative,
                     SurveyUserAnswer)


# Define serializers class from our models.
class SurveyUserAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyUserAnswer
        fields = "__all__"


class SurveyQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyQuestion
        fields = "__all__"


class SurveySerializer(serializers.ModelSerializer):
    question = SurveyQuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Survey
        fields = (
            'survey_id',
            'survey_name',
            'question',
        )


class SurveyQuestionAlternativeSerializer(serializers.ModelSerializer):
    question = SurveySerializer(read_only=True, many=True)
    user_answer = SurveyUserAnswerSerializer(read_only=True, many=True)

    class Meta:
        model = SurveyQuestionAlternative
        fields = (
            'survey_question',
            'first_alternative',
            'second_alternative',
            'third_alternative',
            'user_answer',
            'question'
        )
