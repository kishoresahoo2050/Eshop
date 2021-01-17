from django.db import models
from .category import Category

class Products(models.Model):
    category    = models.ForeignKey(Category,on_delete=models.CASCADE)
    name        = models.CharField(max_length=60)
    price       = models.DecimalField(max_digits=15,decimal_places=2)
    decription  = models.TextField(null=True)
    img         = models.ImageField(upload_to='uploads/products_img/',default='')
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_category_by_products(cate_id):
        if cate_id:
            return Products.objects.filter(category_id=cate_id)
        else:
            return Products.get_all_products()


    
