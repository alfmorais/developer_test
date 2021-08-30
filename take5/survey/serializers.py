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

    class Meta:
        model = Survey
        fields = "__all__"


class SurveyQuestionAlternativeSerializer(serializers.ModelSerializer):
    question = SurveyQuestionSerializer(many=True, read_only=True)
    survey_name = SurveySerializer(many=True, read_only=True)

    class Meta:
        model = SurveyQuestionAlternative
        fields = [
            'survey_question',
            'first_alternative',
            'second_alternative',
            'third_alternative',
            'question',
            'survey_name',
        ]
