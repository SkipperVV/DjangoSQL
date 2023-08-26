from django.db import models

# Create your models here.
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


class Order(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)  # Not Null ставится автоматически


class ProductOrder(models.Model):
    name = models.CharField(max_length=255)

''' Мы указали, что это строковое поле сейчас должно быть всегда ограничено двумя символами 
(как в переменных соответствующих должностям). Однако присвоить этому полю мы можем значения 
только из кортежей, который состоит из двух элементов. Первый элемент — это наше краткое обозначение 
должности, которое будет храниться в базе данных, а второй элемент — отображаемое значение этого поля 
(как и где оно будет отображаться, рассмотрим позже). По умолчанию мы установили, что должность 
будет — кассир (cashier). Такой подход защищает нас от возможных случайных вставок должностей, 
которых в реальности не существует. Удобно, согласитесь?'''

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
class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    labor_contract = models.IntegerField(default=0)
    position = models.CharField(max_length=2,
                                choices=POSITIONS,
                                default=cashier)


'''Скрипт НЕ ЗАПУСКАТЬ!!!
Не забудь
python manage.py makemigrations
и применить миграцию
python manage.py migrate
'''
