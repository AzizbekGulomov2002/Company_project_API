from django.db import models




class Worker(models.Model):
    worker_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

status=[
    ('active','Active'),
    ('accepted','Accepted'),
    ('completed','Completed'),
    ('cancel','Cancel')
]

class Exercises(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    title = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    dedline = models.DateField()
    status = models.CharField(max_length=50, choices=status,default='active')

    def __str__(self):
        return self.title


class Work_tables(models.Model):
    worker_id = models.AutoField(primary_key=True)
    name_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    title = models.TextField(null=True,blank=True)


    def __str__(self):
        return str(self.worker_id)
