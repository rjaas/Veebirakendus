from django.db import models


class raamatud(models.Model):
    pealkiri = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    kirjastus = models.CharField(max_length=30)
    ilmumisaasta = models.IntegerField
    lehekülgi = models.IntegerField
    keel = models.CharField(max_length=10)


class likes(models.Model):
    user_id = models.IntegerField
    book_id = models.IntegerField
    comment = models.CharField(max_length=300)


class owned(models.Model):
    usr = models.IntegerField(primary_key=True, default=0)
    book = models.ForeignKey(raamatud, to_field='id', on_delete=models.CASCADE, default=0)
    comment = models.CharField(max_length=300)
