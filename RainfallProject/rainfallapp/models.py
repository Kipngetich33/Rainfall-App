from django.db import models

class Profile(models.Model):
    '''
    class that defines the structure of each profile object
    '''
    username = models.IntegerField()
    
    def __str__(self):
        return self.username
