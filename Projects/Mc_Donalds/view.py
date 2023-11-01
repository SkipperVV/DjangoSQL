from Mc_Donalds.models import *

cashier1 = Staff.objects.create(full_name="Иванов Иван Иванович",
                                position= cashier,
                                labor_contract=1754)
cashier2 = Staff.objects.create(full_name="Петров Петр Петрович",
                                position=cashier,
                                labor_contract=4355)
direct = Staff.objects.create(full_name="Максимов Максим Максимович",
                              position=director,
                              labor_contract=1254)

potato_free_standart = Product(name='Картофель фри (станд.)', price=93.0)
potato_free_standart.save()
potato_free_big = Product.objects.create(name="Картофель фри (бол.)", price=106.0)
potato_free_big.save()