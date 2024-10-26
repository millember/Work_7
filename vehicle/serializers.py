from rest_framework import serializers
from vehicle.models import Car, Moto, Milage


class MilageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = '__all__'


class CarSerializers(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(source='milage_set.all.first.milage')
    milage = MilageSerializers(source='milage_set', many=True)

    class Meta:
        model = Car
        fields = '__all__'


class MotoSerializers(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_milage(self, instance):
        if instance.milage_set.all().first():
            return instance.milage_set.all().first().milage
        return 0


class MotoMilageSerializers(serializers.ModelSerializer):
    moto = MotoSerializers()

    class Meta:
        model = Milage
        fields = ('milage','year', 'moto',)
