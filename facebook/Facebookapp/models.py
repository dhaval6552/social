from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify
# Create your models here.
#    return "%s/%s" %(new_id, filename)

# class Profile(models.Model):
#
#   #  first_name=models.CharField(max_length=100)

class Profile_final(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    profile_image = models.FileField(null=True, blank=True)

    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse("profile", kwargs={"id": self.id })