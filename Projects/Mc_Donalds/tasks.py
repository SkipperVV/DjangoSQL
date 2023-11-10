from celery import shared_task
from .models import Order

@shared_task
def complete_order(oid):
    order = Order.objects.get(pk = oid)
    order.complete = True
    order.save()


# @shared_task
# def hello():
#     time.sleep(10)
#     print("Hello, Vladimir, from tasks.py!")
#
#
# @shared_task
# def printer(N):
#     for i in range(N):
#         time.sleep(1)
#         print(f'from task printer:  {i + 1}')