from rest_framework import serializers

from .models import Worker, Exercises, Work_tables

class WorkerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class ExercisesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = '__all__'

class Work_tablesserializers(serializers.ModelSerializer):
    class Meta:
        model = Work_tables
        fields = '__all__'