Создать новое приложение:
python manage.py startapp Mc_Donalds
Открыть setting.py и добавить приложение в
INSTALLED_APPS = [
    ........
    'Mc_Donalds',
    ]
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

class <Имя_таблицы>(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField(default=0.0) # Not Null ставится автоматически

Чтобы активировать таблицу:
python manage.py makemigrations