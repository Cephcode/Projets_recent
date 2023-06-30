from django.db import models
from authentication.models import User

# Create your models here.
class Todo(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    completed=models.BooleanField(default=False)
    created=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    