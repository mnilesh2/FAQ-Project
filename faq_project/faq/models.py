from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG support for answers
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    # def get_translated_question(self, lang='en'):
    #     """
    #     Returns the translated question based on the selected language.
    #     Defaults to English if translation is not available.
    #     """
    #     translations = {
    #         'hi': self.question_hi,
    #         'bn': self.question_bn
    #     }
    #     return translations.get(lang, self.question)
    
    def get_translated_question(self, lang='en'):
        cache_key = f"faq_question_{self.id}_{lang}"
        cached_value = cache.get(cache_key)
        if cached_value:
            return cached_value

        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn
        }
        translated_question = translations.get(lang, self.question)
        cache.set(cache_key, translated_question, timeout=60 * 15)  # Cache for 15 minutes
        return translated_question
    
    def translate_fields(self):
        translator = Translator()
        self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text
        self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text
        self.save()

    def save(self, *args, **kwargs):
        # Automatically translate on creation
        if not self.pk:  # Translate only when creating a new FAQ
            self.translate_fields()
        super().save(*args, **kwargs)

    def get_translated_answer(self, lang='en'):
        """
        Returns the translated answer based on the selected language.
        Defaults to English if translation is not available.
        """
        translations = {
            'hi': self.answer_hi,
            'bn': self.answer_bn
        }
        return translations.get(lang, self.answer)

    def __str__(self):
        return self.question

# from django.core.cache import cache

# class FAQ(models.Model):
#     # Existing fields

#     def get_translated_question(self, lang='en'):
#         cache_key = f"faq_question_{self.id}_{lang}"
#         cached_value = cache.get(cache_key)
#         if cached_value:
#             return cached_value

#         translations = {
#             'hi': self.question_hi,
#             'bn': self.question_bn
#         }
#         translated_question = translations.get(lang, self.question)
#         cache.set(cache_key, translated_question, timeout=60 * 15)  # Cache for 15 minutes
#         return translated_question
