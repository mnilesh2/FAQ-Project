from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_hi', 'question_bn', 'answer_hi', 'answer_bn']

    def to_representation(self, instance):
        lang = self.context.get('lang', 'en')
        data = super().to_representation(instance)
        data['question'] = instance.get_translated_question(lang)
        data['answer'] = instance.get_translated_answer(lang)
        return data
