from rest_framework import serializers


class ReportSerializer(serializers.Serializer):
    total_units_ordered = serializers.IntegerField()
    total_ordered_price = serializers.FloatField()






