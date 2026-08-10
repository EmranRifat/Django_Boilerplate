from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer
from users.serializers import SignupSerializer


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    "message": "User created successfully.",
                    "user": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# ----------------------------------------------------
            # User Login function 
# ----------------------------------------------------

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(
            data=request.data,
            context={"request": request},
        )

        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "message": "Login successful.",
                "data": serializer.validated_data,
            },
            status=status.HTTP_200_OK,
        )



# ----------------------------------------------------
            # User LogOut function 
# ----------------------------------------------------
class UserLogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        return Response(
            {
                "message": "Logout endpoint working."
            },
            status=status.HTTP_200_OK,
        )