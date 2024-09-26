from rest_framework import serializers
from .models import AdminCMS

class AdminCMSSerializer(serializers.ModelSerializer):
    icon = serializers.ImageField(required=False, allow_null=True) 

    class Meta:
        model = AdminCMS
        fields = ['id', 'account_type', 'currency_type', 'icon']

    # Ensure to return the validated data
    def validate(self, data):
        # Ensure at least one field is provided
        if not data.get('account_type') and not data.get('currency_type'):
            raise serializers.ValidationError('At least one of account_type or currency_type must be provided.')

        # Optionally, check for mutual exclusivity of account_type and currency_type
        if data.get('account_type') and data.get('currency_type'):
            raise serializers.ValidationError('Only one of account_type or currency_type can be provided at a time.')

        return data  # This line was missing previously!

    # Get the icon URL from CloudinaryResource object
    def get_icon(self, obj):
        if obj.icon:  # Check if the icon exists
            return obj.icon.url  # Return the URL for frontend use
        return None  # Return None if no icon is provided
