from django.db import models

class Add_Rainfall(models.Model):
    '''
    class that defines the structure of each profile object
    '''
    amount = models.IntegerField()
    record_date = models.DateTimeField(auto_now_add=True, null= True)
    city = models.CharField(max_length = 30, blank = True)
    
    def __str__(self):
        return self.city

    def save_rainfall(self):
        self.save()
    
    def delete_rainfall(self):
        self.delete()


class City(models.Model):
    '''
    Class that defines the structure of a City object
    '''
    name = models.CharField(max_length = 30 , blank = True)
    country = models.CharField(max_length = 30 , blank = True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    '''
    Class that defines profile objects of the objects
    '''
    pass