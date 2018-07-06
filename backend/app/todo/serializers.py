from rest_framework import serializers   

from app.todo import models  
   
    
class TodoModelSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = models.Note  
        fields = ('id', 'task', 'color', 'done', 'is_archived', 'timestamp')  