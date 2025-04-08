from django.db import models
from ckeditor.fields  import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount

class Categories(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Shop(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    price=models.CharField(max_length=50)
    discount_price=models.CharField(max_length=50)  
    categories=models.ForeignKey(Categories, on_delete=models.CASCADE)


#blog-model rasm sarlavha ma'lumot yaratilgan sanasi va vaqtini ko'rsatadi
#shopni category ga qo'yish

class BlogCategories(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Blog(models.Model ,HitCountMixin):
    image=models.ImageField(upload_to='blog/')
    title=models.CharField(max_length=70)
    description=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True)
    categories=models.ForeignKey(BlogCategories, on_delete=models.CASCADE)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    

    def __str__(self):
        return self.title
    
     
    
class Faq(models.Model):
    question=models.CharField(max_length=100)
    answer=RichTextField()
    
class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    
