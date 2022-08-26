from django.db import models

ACCOUNT_TYPE_CHOICE = (
 ('Current Account', 'Current Account'),
 ('Saving Account', 'Saving Account'),

)
class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    email = models.EmailField()
    age = models.CharField(max_length=2)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    mob = models.CharField(max_length=12)
    dob = models.DateField(null=True, blank=True)
    account = models.CharField(choices=ACCOUNT_TYPE_CHOICE,max_length=100)
    materials = models.CharField(max_length=150)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.name