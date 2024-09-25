from rest_framework import serializers
from .models import AdminCMS

class AdminCMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminCMS
        fields = ['id','account_type', 'currency_type','icon']

    def validate(self, data):
        # Ensure at least one field is provided
        if not data.get('account_type') and not data.get('currency_type'):
            raise serializers.ValidationError('At least one of account_type or currency_type must be provided.')
        
        # If you want to enforce mutually exclusive fields, retain the logic below
        if data.get('account_type') and data.get('currency_type'):
            raise serializers.ValidationError('Only one of account_type or currency_type can be provided at a time.')
        
        return data
