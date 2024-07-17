from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='uploads/')

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_file = File.objects.get(pk=self.pk).file
                if old_file:
                    old_file.delete(save=False)
            except File.DoesNotExist:
                pass
        super().save(*args, **kwargs)
# Create your models here.
