from django.db import models

# Create your models here.
class Todo(models.Model):
    TYPES_PRIORITY = (
        ("MUHIM","MUHIM"),
        ("O'RTACHA","O'RTACHA"),
        ("ODDIY","ODDIY")
    )
    title = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=255, choices=TYPES_PRIORITY,
                        default="ODDIY")
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Tasks'
    