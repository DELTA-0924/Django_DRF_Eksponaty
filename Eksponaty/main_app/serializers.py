from  rest_framework import serializers
from .models import *
class EksponatySerializer(serializers.ModelSerializer):
    class Meta:
        model=Eksponaty
        fields='__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'