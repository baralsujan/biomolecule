from celery import shared_task

from DNASequencer.models import SearchRequest, Task


@shared_task()
def add_search_request(sequence, user_id):
    sr = SearchRequest(inputSequence=sequence, created_by=user_id)
    sr.save()
    task = Task(input_id=sr)
    task.save()

    search_request.delay(task.id)
    return 'Hello ' + str(user_id) + '--' + sequence


@shared_task()
def search_request(task_id):
    return 'Hello ' + str(task_id)
