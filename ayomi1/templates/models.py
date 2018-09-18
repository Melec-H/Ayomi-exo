from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser
	)
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


#je laisse ça dans le code sans raison
#post_save.connect(modidy_profile, sender=User)
# def modify_profile(sender, **kwargs):
#	if kwargs[]
