from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class router_detail(models.Model):
    sapid= models.CharField(max_length=18)
    hostname=models.CharField(max_length=14)
    loopback=models.GenericIPAddressField(unique=True) 
    mac_addr=models.CharField(max_length=17)
    def __str__(self):
        return self.hostname

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)