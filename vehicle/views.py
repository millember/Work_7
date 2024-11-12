from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from vehicle.models import Car, Moto, Milage
from vehicle.paginators import VehiclePaginator
from vehicle.permissions import IsOwnerOrStaff
from vehicle.serializers import CarSerializers, MotoSerializers, MilageSerializers, MotoMilageSerializers, \
    MotoCreateSerializer
from vehicle.task import check_milage


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializers
    queryset = Car.objects.all()
    permission_classes = [AllowAny]


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_moto = serializer.save()
        new_moto.owner = self.request.user
        new_moto.save()


class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializers
    queryset = Moto.objects.all()
    pagination_class = VehiclePaginator


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializers
    queryset = Moto.objects.all()


class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializers
    queryset = Moto.objects.all()
    permission_classes = [IsOwnerOrStaff]


class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()


class MilageCreateApiView(generics.CreateAPIView):
    serializer_class = MilageSerializers

    def perform_create(self, serializer):
        new_milage = serializer.save()
        if new_milage.car:
            check_milage.delay(new_milage.car_id, 'Car')
        else:
            check_milage.delay(new_milage.moto_id, 'Moto')


class MilageListApiView(generics.ListAPIView):
    serializer_class = MilageSerializers
    queryset = Milage.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('car', 'moto')
    ordering_fields = ('year',)


class MotoMilageListApiView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializers
