from django.db import models

class SupportStaff(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
