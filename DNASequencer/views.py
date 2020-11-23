import json

from django.http import HttpResponse
from django.utils import timezone

from DNASequencer.tasks import add_search_request

# Create your views here.
from django.views import View

from django.core import serializers


class DNASequencerView(View):

    def post(self, requests):
        sequence = requests.POST.get('sequence', None)
        user_id = requests.POST.get('user_id', None)
        try:
            add_search_request.delay(sequence, user_id)
        except Exception as e:
            # log proper message and pass proper response message
            HttpResponse(status=500)
        if sequence:
            return HttpResponse('Found ' + sequence)
        return HttpResponse('Not Found')
