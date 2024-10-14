from rest_framework import serializers
from .models import Todo
import re
from django.template.defaultfilters import slugify


class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    class meta:
        model=Todo
        #fields=['__all__']
        fields = ['todo_title','slug','todo_desc','is_done','uid']
   
    def get_slug(self, obj):

        return slugify(obj.todo_title)
    
    def validate_todo_title(self,data):
        if data.get('todo_title'):
            todo_title = data.get('todo_title')
            regex=re.compile('[@_!#$%^&*()<>?/|}{~:]')
            if len(todo_title) < 3:
                raise serializers.ValidationError('title length should be greater than 3 characters')
            if regex.search(todo_title) is not None:
                raise serializers.ValidationError('title cannot contain special characters')

        return data