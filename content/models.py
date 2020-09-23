from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    profilepic=models.ImageField(default='logo.png',null=True,blank=True)
    phone=models.CharField(max_length=200,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    CATEGORY={
        ('OUTDOOR','OUTDOOR'),
        ('INDOOR', 'INDOOR'),

    }



    name=models.CharField(max_length=200,null=True)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    tag=models.ManyToManyField(Tag,max_length=200,null=True)
    price=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.name
class Order(models.Model):
    STATUS={
        ('DELIVERED', 'DELIVERED'),
        ('OUT OF DELIVERED', 'OUT OF DELIVERED'),
        ('PENDING', 'PENDING'),
    }
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    status=models.CharField(max_length=200,choices=STATUS)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.product.name

