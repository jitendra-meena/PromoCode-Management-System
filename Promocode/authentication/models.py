from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

gender_choicee = (('MALE', 'MALE'),('FEMALE', "FEMALE"))
class Promo(models.Model):
    
    code_type = models.CharField(max_length = 10,  choices = gender_choicee, default = 'MALE')
    code_name = models.CharField(max_length = 15)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def save(self, *args, **kwargs):
        self.code_name = self.code_type + self.code_name.upper()
        return super().save(*args, **kwargs)
    def  __str__(self):
        return self.code_name 




class UsersPromocode(models.Model):
    PromoCodeStatus = (('Active', 'Active'),('Expired','Expired'))

    user = models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    codes = models.ForeignKey(Promo,related_name='user_code',  on_delete=models.CASCADE)
    birthday = models.DateField()
    gender = models.CharField(max_length = 10,default='MALE',choices = gender_choicee)
    order_amount = models.IntegerField(validators=[MaxValueValidator(1500000),MinValueValidator(100)], blank = True)
    promo_code_status = models.CharField(max_length = 30, choices = PromoCodeStatus,default = 'Active')

    
    


