from django.db import models
from django import utils

from app.todo import validators


class Note(models.Model):
    """Model for creating todo items"""  
    task = models.CharField(  
        "Task Name",  
        max_length=255  
    )  
    color = models.CharField(  
        "Color Label",  
        max_length=7,  
        default='#ffffff',  
        validators=[  
            validators.HexadecimalValidator,  
        ]  
    )  
    done = models.BooleanField(  
        "Task Status",  
        default=False  
    )  
    is_archived = models.BooleanField(  
        "Archival Status",  
        default=False  
    )  
    timestamp = models.DateTimeField(   
        "Created Time",  
        auto_now = True   
    )  
     
    def archive(self): 
        cat = 2
        assert self is not None
        self.is_archived=True  
        self.save()   
