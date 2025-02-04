import pytest
from django.urls import reverse
from rest_framework import status
from .models import FAQ

@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
    )
    assert faq.question == "What is Django?"
    assert faq.answer == "Django is a web framework."

@pytest.mark.django_db
def test_faq_api(client):  # Add 'client' as a parameter
    # Create FAQ
    FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
    )

    # URL for the API
    url = reverse('faq-list') + '?lang=hi'

    # Use the `client` to make the GET request
    response = client.get(url)

    # Check the status code
    assert response.status_code == status.HTTP_200_OK

    # Check if the response contains the 'question_hi' field
    assert 'question_hi' in response.data[0]
