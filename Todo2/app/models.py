from django.db import models

# Create your models here.
# class Days(models.Model):
#     day = models.CharField(max_length=100, verbose_name='day')
#
#     def __str__(self):
#         return self.day

class Tasks(models.Model):
    title = models.CharField(verbose_name='Task Name', max_length=300)
    done = models.BooleanField(verbose_name='Done', default=False)
    # day = models.ForeignKey(Days, on_delete=models.CASCADE)
    # user = models.F

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __sts__(self):
        return self.title

