from django.urls import path
from . import views

urlpatterns = [
    # Define a URL pattern for the '' URL that maps to the 'analyze_sentiment_text' view function
    path('', views.analyze_sentiment_text, name='analyze_sentiment_text'),
    # Define a URL pattern for the 'analyze_file/' URL that maps to the 'analyze_sentiment_file' view function
    path('analyze_file/', views.analyze_sentiment_file, name='analyze_sentiment_file'),
]
