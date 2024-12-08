from django.db import models

# Create your models here.
class Pagevists(models.Model):
    # db->table
    # id->primary key (auto increment)
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)