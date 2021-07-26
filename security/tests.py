from django.test import TestCase
from .models import neighbourhood,healthservices
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Ruaka = neighbourhood(neighbourhood='Ruaka')

    def test_instance(self):
        self.assertTrue(isinstance(self.Ruaka,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Ruaka.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Ruaka.delete_neighbourhood('Ruaka')
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

class healthservicesTestClass(TestCase):
    def setUp(self):
        self.Psychology = healthservices(healthservices='Psychology')

    def test_instance(self):
        self.assertTrue(isinstance(self.Psychology,healthservices))

    def tearDown(self):
        healthservices.objects.all().delete()

    def test_save_method(self):
        self.Psychology.save_healthservices()
        health = healthservices.objects.all()
        self.assertTrue(len(health)>0)

    def test_delete_method(self):
        self.Psychology.delete_healthservices('Psychology')
        health = healthservices.objects.all()
        self.assertTrue(len(health)==0)
