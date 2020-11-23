from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('dnas/', views.DNASequencerView.as_view(), name='dna_sequence'),
    path('dnas/submit-sequence/', views.DNASequencerView.as_view(), name='submit-sequence'),
]