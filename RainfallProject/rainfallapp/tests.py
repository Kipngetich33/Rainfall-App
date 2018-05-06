from django.test import TestCase
from . models import Add_Rainfall,City,Profile

class Add_RainfallTestClass(TestCase):
    '''
    A class that test the Add_Rainfall class model
    '''

    def setUp(self):
        '''
        method that runs at the begginning of each test
        '''
        self.rainfall = Add_Rainfall(amount = 4,city = 'test_city')

    def test_instance(self):
        '''
        method that test is Add_Rainfall objects are instanciated correctly
        '''
        self.assertTrue(isinstance(self.rainfall,Add_Rainfall)) 

    def test_save_image(self):
        '''
        method that test the saves Add_Rainfall objects
        '''
        self.rainfall.save_rainfall()
        rainfall_objects= Add_Rainfall.objects.all()
        self.assertTrue(len(rainfall_objects)>0)

    def test_delete_images(self):
        '''
        method that tests the delete_images method
        '''
        self.rainfall.save_rainfall()
        new_rainfall_object = Add_Rainfall(amount = 0,city = 'test_city2')
        new_rainfall_object.save_rainfall()
        self.rainfall.delete_rainfall()
        rainfall_objects= Add_Rainfall.objects.all()
        self.assertTrue(len(rainfall_objects)==1)
