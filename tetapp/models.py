from django.db import models
from django.urls import reverse


class users(models.Model):
    login_user = models.CharField(max_length=255)
    first_name_user = models.CharField(max_length=255)
    last_name_user = models.CharField(max_length=255)
    date_create_user = models.DateField(auto_now_add=True)
    photo_profile_user = models.ImageField(upload_to="photos/%Y/%m/%d/")
    email_user = models.EmailField(max_length=255)

    def get_absolute_url(self):
        return reverse('user', kwargs={'user_id': self.pk})