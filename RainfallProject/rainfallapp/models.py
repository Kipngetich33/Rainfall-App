from django.db import models

class Add_Rainfall(models.Model):
    '''
    class that defines the structure of each profile object
    '''
    amount = models.IntegerField()
    city = models.CharField(max_length = 30, blank = True)
    
    def __str__(self):
        return self.city
