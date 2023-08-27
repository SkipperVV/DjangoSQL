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


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)  # Not Null ставится автоматически


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


class Order(models.Model):
    name = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0)
    take_away = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    products = models.ManyToManyField(Product, through='ProductOrder')
    # для ManyToMany требуется отдельная таблица ProductOrder


class ProductOrder(models.Model):
    amount = models.IntegerField(default=1)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)  # Если на Order ссылаются раньше его объявления-
    # в кавычки 'Order' или перенести в конец
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def product_sum(self):
        product_price=self.product.price
        return product_price*self.amount



'''
После изменения кода в models.py удалить записи миграции проекта из "migrations" и удалить все таблицы в DBeaver
Скрипт models.py НЕ ЗАПУСКАТЬ!!!
Конвертнуть код в SQL с помощью Django:
python manage.py makemigrations
и применить полученный код SQL к базе:
python manage.py migrate
'''
