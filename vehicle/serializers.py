from symtable import Class

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from vehicle import validators
from vehicle.models import Car, Moto, Milage
from vehicle.validators import TitleValidator


class MilageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = '__all__'


class CarSerializers(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(source='milage.all.first.milage')
    milage = MilageSerializers(many=True)

    class Meta:
        model = Car
        fields = '__all__'


class MotoSerializers(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_milage(self, instance):
        if instance.milage.all().first():
            return instance.milage.all().first().milage
        return 0


class MotoMilageSerializers(serializers.ModelSerializer):
    moto = MotoSerializers()

    class Meta:
        model = Milage
        fields = ('milage', 'year', 'moto',)


class MotoCreateSerializer(serializers.ModelSerializer):
    milage = MilageSerializers(many=True)

    class Meta:
        model = Moto
        fields = '__all__'
        validators = [TitleValidator(field='title'),
                      serializers.UniqueTogetherValidator(fields=['title', 'description'], queryset=Moto.objects.all())
                      ]

    def create(self, validated_data):
        milage = validated_data.pop('milage')

        moto_item = Moto.objects.create(**validated_data)

        for m in milage:
            Milage.objects.create(**m, moto=moto_item)

        return moto_item
