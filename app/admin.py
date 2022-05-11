from django.contrib import admin
from .models import Worker, Exercises, Work_tables
# Register your models here.

class WorkerAdmin(admin.ModelAdmin):
    list_display = ['worker_id','name','position','birth_date']
    search_fields = ['name','position','birth_date']
    list_per_page = 4

admin.site.register(Worker,WorkerAdmin)


class ExercisesAdmin(admin.ModelAdmin):
    list_display = ['exercise_id','title','start_date','dedline','status']
    search_fields = ['exercise_id', 'title', 'start_date','dedline','status']
    list_per_page = 4

admin.site.register(Exercises, ExercisesAdmin)

class Work_tableAdmin(admin.ModelAdmin):
    list_display = ['worker_id','name_id','title']
    search_fields = ['worker_id', 'name_id', 'title']
    list_per_page = 4

admin.site.register(Work_tables,Work_tableAdmin)


