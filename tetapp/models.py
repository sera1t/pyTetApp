from django.db import models
from django.urls import reverse


# class users(models.Model):
#     login_user = models.CharField(max_length=255)
#     first_name_user = models.CharField(max_length=255)
#     last_name_user = models.CharField(max_length=255)
#     password_user =
#     date_create_user = models.DateField(auto_now_add=True)
#     photo_profile_user = models.ImageField(upload_to="photos/%Y/%m/%d/")
#     email_user = models.EmailField(max_length=255)
#
#     def __str__(self):
#         return self.login_user
#
#     def get_absolute_url(self):
#         return reverse('user', kwargs={'user_id': self.pk})

class posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title