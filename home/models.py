import uuid
from django.db import models


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False, default=uuid.uuid4(),)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Todo(BaseModel):
    todo_title = models.CharField(max_length=100)
    todo_desc = models.CharField(max_length=500)
    is_done = models.BooleanField(default=False)