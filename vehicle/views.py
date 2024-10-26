from rest_framework import viewsets, generics

from vehicle.models import Car, Moto
from vehicle.serializers import CarSerializers, MotoSerializers, MilageSerializers


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializers
    queryset = Car.objects.all()


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoSerializers


class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializers
    queryset = Moto.objects.all()


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializers
    queryset = Moto.objects.all()


class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializers
    queryset = Moto.objects.all()


class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()


class MilageCreateApiView(generics.CreateAPIView):
    serializer_class = MilageSerializers
