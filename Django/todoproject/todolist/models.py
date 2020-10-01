from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.TextField()
    #due_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.task_name
#    complete_stat = models.ManyToManyField('Complete_stat',blank="True")

#class Complete_stat(models.Model):
#    comp_stat = models.CharField(max_length=50)
    
    


