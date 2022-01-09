from django.core.mail import send_mail
from rest_framework import filters, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .permissions import IsAdmin
from .serializers import TokenSerializer, UserSerializer


class GetRefreshTokens(TokenObtainPairView):
    serializer_class = TokenSerializer
    permission_classes = []


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    lookup_field = 'username'
    permission_classes = [IsAdmin]

    @action(
        detail=False,
        methods=['GET', 'PATCH'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        if request.method == 'PATCH':
            serializer = self.get_serializer(
                request.user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        else:
            serializer = self.get_serializer(request.user)

        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def send_confirmation_code(request):
    if request.method != 'POST':
        return Response(
            data={'error': 'Only POST method allowed'},
            status=status.HTTP_400_BAD_REQUEST
        )
    email = request.data.get('email', '')
    if not email:
        return Response(
            data={'error': f'No valid email found, got :{email} '},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.get(email=email)

    success = send_mail(
        'Confirmation code for Yamdb',
        f'Here is your code: {user.confirmation_code}',
        ['admin@example.com'],
        [email]
    )
    if success:
        return Response(
            data={'message': (f'Successfully sent '
                              f'confirmation code to {email}')},
            status=status.HTTP_200_OK
        )
    return Response(
        data={'error': 'Failed to send sent confirmation code'},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
