from rest_framework import serializers
from modules.cms.models import Complaint, ComplaintAttachment, ComplaintProgress

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'

class ComplaintCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'

class ComplaintAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintAttachment
        fields = '__all__'

class ComplaintProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintProgress
        fields = '__all__'