from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.contrib.auth.models import User, Group


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email,
        )


@receiver(post_save, sender=User)
def update_customer(sender, instance, created, **kwargs):
    if not created:
        instance.customer.save()
        print('customer updated')
