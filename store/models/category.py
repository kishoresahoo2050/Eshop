from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
    
    def get_all_cate():
        return Category.objects.all().order_by('name')
    