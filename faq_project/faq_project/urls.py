from django.urls import path
from faq.views import FAQListView

urlpatterns = [
    path('faqs/', FAQListView.as_view(), name='faq-list'),
]
