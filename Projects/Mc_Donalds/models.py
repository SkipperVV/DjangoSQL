from datetime import datetime

# from Mc_Donalds.resources import *
from django.db import models

'''
class Staff(models.Model):
    director = 'DI'
    admin = 'AD'
    cook = 'CO'
    cashier = 'CA'
    cleaner = 'CL'

    POSITIONS = [
        (director, 'Директор'),
        (admin, 'Администратор'),
        (cook, 'Повар'),
        (cashier, 'Кассир'),
        (cleaner, 'Уборщик')
    ]
    full_name = models.CharField(max_length=255)
    labor_contract = models.IntegerField(default=0)
    position = models.CharField(max_length=2,
                                choices=POSITIONS,
                                default=cashier)

    def get_last_name(self):
        return self.full_name.split()[0]
'''

'''
Открыть models.py, где создать новую модель (таблицу) с помощью django
аналогичную с:

CREATE TABLE products (
	id BIGSERIAL PRIMARY KEY,
	name TEXT NOT NULL UNIQUE,
	price FLOAT CHECK (price > 0),
	vendor_id BIGINT REFERENCES vendors(id),
	manufacturers_id BIGINT REFERENCES manufacturers(id)
'''
''' Мы указали, что это строковое поле сейчас должно быть всегда ограничено двумя символами
(как в переменных соответствующих должностям). Однако присвоить этому полю мы можем значения
только из кортежей, который состоит из двух элементов. Первый элемент — это наше краткое обозначение
должности, которое будет храниться в базе данных, а второй элемент — отображаемое значение этого поля
(как и где оно будет отображаться, рассмотрим позже). По умолчанию мы установили, что должность
будет — кассир (cashier). Такой подход защищает нас от возможных случайных вставок должностей,
которых в реальности не существует. Удобно, согласитесь?'''


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)  # Not Null ставится автоматически

    def __str__(self):
        return self.name + ' Цена: ' + str(self.price)


class Order(models.Model):
    name = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0)
    take_away = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    # staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    products = models.ManyToManyField(Product, through='ProductOrder')

    # для ManyToMany требуется отдельная таблица ProductOrder
    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    def get_duration(self):
        if self.complete:
            return (self.time_out - self.time_in).total_seconds() // 60
        else:
            return (datetime.now() - self.time_in).total_seconds() // 60


'''В первую очередь мы изменили название поля на _amount (добавили нижнее подчёркивание). 
Это необходимо, чтобы создание свойства не переписало объект IntegerField, который хранится в amount. 
Однако, чтобы не возникло конфликтов в базе данных, и не пришлось делать миграцию, мы оставили название 
колонки в базе данных тем же самым — amount, задав его явно.'''


class ProductOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)  # Если на Order ссылаются раньше его объявления-
    # в кавычки 'Order' или перенести в конец
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # amount = models.IntegerField(default = 1)
    _amount = models.IntegerField(default=1, db_column='amount')

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0
        self.save()

    def product_sum(self):
        return self.product.price * self.amount


'''
После изменения кода в models.py удалить записи миграции проекта из "migrations" и удалить все таблицы в DBeaver
Скрипт models.py НЕ ЗАПУСКАТЬ!!!
Конвертнуть код в SQL с помощью Django:
python manage.py makemigrations
и применить полученный код SQL к базе:
python manage.py migrate
'''
# from Mc_Donalds.models import Staff
