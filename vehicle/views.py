from rest_framework import viewsets, generics

from vehicle.models import Car, Moto, Milage
from vehicle.serializers import CarSerializers, MotoSerializers, MilageSerializers, MotoMilageSerializers, \
    MotoCreateSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializers
    queryset = Car.objects.all()


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer


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


class MotoMilageListApiView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class =MotoMilageSerializers
