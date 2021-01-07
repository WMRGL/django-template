from celery import shared_task


@shared_task
def test(x):
    print(x)
    return x