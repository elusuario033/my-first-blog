
from django.db import models
from django.utils import timezone

class Estudiantes(models.Model):
        estudiante = models.ForeignKey('auth.User')
        programa = models.CharField(max_length=200)
        concepto = models.TextField()
        fecha_de_nacimiento = models.DateTimeField(
                default=timezone.now)
        fecha_de_registro = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title
