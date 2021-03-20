from django.test import TestCase
from .models import TypeGoods, Goods
# Create your tests here.

class TypeGoodsTestCase(TestCase):
    def setUp(self):
        TypeGoods.objects.create(name='Imovel', description='Qualquer tipo de imovel')

    def test_type_good_can_name(self):
        type_goods = TypeGoods.objects.get(name='Imovel')
        self.assertEqual(type_goods.__str__(), 'Imovel')

class GoodTestCase(TestCase):
    def setUp(self):
        type_goods = TypeGoods.objects.create(name='Imovel', description='Qualquer tipo de imovel')
        Goods.objects.create(name='Casa de praia', description='Uma bela casa de praia', type_good=type_goods)

    def test_good_can_name(self):
        good = Goods.objects.get(name='Casa de praia')
        self.assertEqual(good.__str__(), 'Casa de praia')