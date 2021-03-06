""" 
core.serializers

"""

from rest_framework import serializers
from .models import PandaJob
from .columns_config import COLUMNS

class SerializerPandaJob1(serializers.Serializer):
#    class Meta:
#        model = PandaJob
##        fields = tuple([x.lower() for x in CUSTOM_DB_FIELDS['jobListByProdUser']['jobparam']])
##        print fields
##        fields = tuple(['pandaid'] + [x.lower() for x in CUSTOM_DB_FIELDS['jobListByProdUser']['jobparam']])
#        fields = ('pandaid',)
    pandaid = serializers.IntegerField()
    jobstatus = serializers.CharField()
    cpuconsumptiontime = serializers.IntegerField()
    creationtime = serializers.DateTimeField()
    starttime = serializers.DateTimeField()
    endtime = serializers.DateTimeField()
    modificationhost = serializers.CharField()
    computingsite = serializers.CharField()
    produsername = serializers.CharField()


class SerializerPandaJob(serializers.ModelSerializer):
    class Meta:
        model = PandaJob
        compulsory_fields = ['pandaid']

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(SerializerPandaJob, self).__init__(*args, **kwargs)

    def validate(self, attrs):
        """
            Check that the self.Meta.compulsory_fields are present.
        
        """
        for field in self.Meta.compulsory_fields:
            try:
                if not len(attrs[field]) > 0:
                    raise serializers.ValidationError("%s must not be empty!" % field)
            except KeyError:
                raise serializers.ValidationError("%s must be filled!" % field)
            return attrs


class SerializerPandaJobReprocessing(serializers.Serializer):
#    class Meta:
#        model = PandaJob
##        fields = tuple(COLUMNS['api-reprocessing-jobs-in-task-smry'])
#        fields = ('pandaid', 'jobstatus', 'jobname', 'attemptnr', 'workinggroup', \
#        'jeditaskid', 'modificationtime',)
    pandaid = serializers.IntegerField()
    jobstatus = serializers.CharField()
    jobname = serializers.CharField()
    attemptnr = serializers.IntegerField()
    workinggroup = serializers.CharField()
    jeditaskid = serializers.IntegerField()
    modificationtime = serializers.DateTimeField()


