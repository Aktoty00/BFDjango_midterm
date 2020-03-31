from rest_framework import viewsets, generics
from rest_framework import mixins

from main.models import MyUser
from main.serializer import MyUserSerializer


class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class RegisterView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

