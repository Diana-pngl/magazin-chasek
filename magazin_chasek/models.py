from django.db import models
from django.contrib.auth.models import AbstractUser
class Tovar(models.Model):
    ima =models.CharField(max_length=20)
    material =models.CharField(max_length=20)
    obiem =models.IntegerField()
    chena =models.DecimalField(max_digits=10, decimal_places=2)
    data_proizvodstva =models.DateField()
    kolichestvo =models.IntegerField()
    image = models.ImageField('Изображение', upload_to='images/', 
            blank=True, null=True, default='images/default.jpg')   
    opisanie = models.TextField(default='')
    
class Polzovatel(AbstractUser):
    nomer =models.CharField(max_length=11)
    adres =models.CharField(max_length=20)

class Karzina(models.Model):
    polzovatel =models.OneToOneField(Polzovatel, on_delete=models.CASCADE, related_name='karzina' )
    tovari =models.ManyToManyField(Tovar, through = 'Karzina_tovar')

class Karzina_tovar(models.Model):
    karzina =models.ForeignKey(Karzina, on_delete=models.CASCADE)
    tovar =models.ForeignKey(Tovar, on_delete=models.CASCADE)
    kolichestvo =models.IntegerField(default=1)