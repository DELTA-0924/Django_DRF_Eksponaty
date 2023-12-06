from email import contentmanager
from email.policy import default
from django.db import models
from PIL import Image
 
class Category(models.Model):
    id_category=models.AutoField(primary_key=True)
    name_category=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name_category
class Eksponaty(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20);
    info=models.TextField()
    deep_info=models.TextField()
    create_date=models.DateField()
    create_place=models.CharField(max_length=20,default="неизвестно");
    image=models.ImageField(upload_to='media');
    catergory=models.ForeignKey(Category,verbose_name="категории",on_delete=models.PROTECT)
    def __self__(self):
        return self.name
    
class  Comment(models.Model):
    id_author=models.AutoField(primary_key=True)
    author=models.CharField(max_length=20)
    email=models.EmailField()
    title_name=models.CharField(max_length=20)
    content=models.TextField()