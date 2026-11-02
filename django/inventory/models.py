from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name="Marka")
    model = models.CharField(max_length=50, verbose_name="Model")
    year = models.IntegerField(verbose_name="İl")
    price = models.IntegerField(verbose_name="Qiymət (AZN)")
    mileage = models.IntegerField(verbose_name="Yürüş (km)")
    city = models.CharField(max_length=50, verbose_name="Şəhər")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    description = models.TextField(blank=True, verbose_name="Təsvir")
    image = models.ImageField(upload_to='cars/', blank=True, null=True, verbose_name="Şəkil")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"