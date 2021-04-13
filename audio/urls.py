from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import overview, AudioView

urlpatterns = [
    path('audio/<str:audio_file_type>/<int:audio_file_id>', AudioView.as_view()),
    path('audio/<str:audio_file_type>', AudioView.as_view()),
    path('audio/', AudioView.as_view()),
    path('', overview, name="Overview"),
]