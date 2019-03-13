from rest_framework import serializers
from afexapp.models import Tasks, User



class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tasks
        fields = ('id','task','description','date' )
