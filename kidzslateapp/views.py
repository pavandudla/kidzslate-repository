#
#
# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework import status, generics
# from django.contrib.auth.models import User
# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework.serializers import ModelSerializer  # Import ModelSerializer
#
# # login
# from django.contrib.auth import authenticate
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import LoginSerializer
#
# from rest_framework_simplejwt.tokens import RefreshToken
#
# # To get student data
# @api_view(["GET"])
# def Readstudent(request):
#     student_obj = Student.objects.all()
#     serializer = StudentSerializer(student_obj, many=True)
#     return Response({"status": 200, "payload": serializer.data})
#
#
# @api_view(["POST"])
# def Addstudentdata(request):
#     student_obj = Student.objects.all()
#     serializer = StudentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response({"status": 200, "payload": serializer.data})
#
#
#
#
#
#
# # login the user
# from django.contrib.auth import authenticate
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import LoginSerializer
# from .emails import *
#
#
#
#
# @api_view(['POST'])
# def register(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     if username and password:
#         user = User.objects.create_user(username=username, password=password)
#         return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
#     return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class LoginApi(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#             user = authenticate(username=username, password=password)
#             if user is None:
#                 # Authentication failed
#                 return Response({
#                     "status": 400,
#                     "message": "Username or password is incorrect",
#                     "data": {}
#                 })
#             else:
#                 # Authentication successful
#                 refresh = RefreshToken.for_user(user)
#                 return Response({
#                     "status": 200,
#                     "message": "Login successful",
#                     "data": {
#                         'refresh': str(refresh),
#                         'access': str(refresh.access_token),
#                     }
#                 })
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# # A protected view example
# class ProtectedView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         return Response({"message": "This is a protected view"}, status=status.HTTP_200_OK)
#
#
#
#
#
#
# # from rest_framework.permissions import IsAuthenticated
# # from rest_framework.decorators import api_view, permission_classes
# # from rest_framework.response import Response
# #
# # @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# # def profile(request):
# #     user = request.user
# #     user_data = {
# #         "username": user.username,
# #         "email": user.email,
# #         # Add other user fields as needed
# #     }
# #     return Response(user_data)
#
#
#
#
#
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from django.contrib.auth.models import User
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def profile(request):
#     user = request.user
#     student_profile = user.student_profile
#     user_data = {
#         "username": user.username,
#         "email": user.email,
#         "student_details": {
#             "student_img": student_profile.student_img.url if student_profile.student_img else None,
#             "Admission_number": student_profile.Admission_number,
#             "Roll_no": student_profile.Roll_no,
#             "Name": student_profile.Name,
#             "Age": student_profile.Age,
#             "Father_name": student_profile.Father_name,
#             "Father_phone_Number": student_profile.Father_phone_Number,
#             "Mother_phone_Number": student_profile.Mother_phone_Number,
#             "class_name": student_profile.class_name,
#             "Address": student_profile.Address,
#             "Total_fees": student_profile.Total_fees,
#             "First_term_fee": student_profile.First_term_fee,
#             "Second_term_fee": student_profile.Second_term_fee,
#             "Third_term_fee": student_profile.Third_term_fee,
#         }
#     }
#     return Response(user_data)
#
#
#








from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Student
from .serializers import StudentSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.views import APIView
from .serializers import LoginSerializer
from django.contrib.auth import authenticate

# ----------------------- get method ----------------------------------------
@api_view(["GET"])
def Readstudent(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj, many=True)
    return Response({"status": 200, "payload": serializer.data})
# ----------------------- get method end ----------------------------------------

# ----------------------- post method start ----------------------------------------
@api_view(["POST"])
def Addstudentdata(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": 200, "payload": serializer.data})
    return Response({"status": 400, "errors": serializer.errors})
# ----------------------- post method end ----------------------------------------

# ----------------------- register the account start ----------------------------------------
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)
# ----------------------- register the account end ----------------------------------------

# ----------------------- login the account start ----------------------------------------
class LoginApi(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        print("serializer:" , serializer)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                return Response({
                    "status": 400,
                    "message": "Invalid Username or password ",
                    "data": {}
                })
            refresh = RefreshToken.for_user(user)
            return Response({
                "status": 200,
                "message": "Login successful",
                "data": {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ----------------------- login the account end ----------------------------------------
# class ProtectedView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         return Response({"message": "This is a protected view"}, status=status.HTTP_200_OK)








# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from rest_framework import status
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def profile(request):
#     user = request.user
#     print("the student details :", user)
#
#     user_data = {
#         "username": user.username,
#         "email": user.email,
#         "student_details": {
#             "username": user.username,
#             "email": user.email,
#             "student_img": "media/student_images/WhatsApp_Image_2024-07-16_at_11.40.09_AM.jpeg",
#             "Admission_number": "12345",
#             "Roll_no": "10",
#             "Name": "ramu",
#             "Age": 15,
#             "Father_name": "Mr.somu",
#             "Father_phone_Number": "1234567890",
#             "Mother_phone_Number": "0987654321",
#             "class_name": "ukg",
#             "Address": "123 Street, City",
#             "Total_fees": 50000,
#             "First_term_fee": 20000,
#             "Second_term_fee": 15000,
#             "Third_term_fee": 15000
#         }
#     }
#
#     return Response(user_data, status=status.HTTP_200_OK)










from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from kidzslateapp.models import Student  # Import the Student model
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user

    try:
        # Fetch the student profile matching the username
        student_profile = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"error": "Student profile not found"}, status=status.HTTP_404_NOT_FOUND)

    user_data = {
        "username": user.username,
        "email": user.email,
        "student_details": {
            "student_img": student_profile.student_img.url if student_profile.student_img else None,
            "Admission_number": student_profile.Admission_number,
            "Roll_no": student_profile.Roll_no,
            "Name": student_profile.Name,
            "Age": student_profile.Age,
            "Father_name": student_profile.Father_name,
            "Father_phone_Number": student_profile.Father_phone_Number,
            "Mother_phone_Number": student_profile.Mother_phone_Number,
            "class_name": student_profile.class_name,
            "Address": student_profile.Address,
            "Total_fees": student_profile.Total_fees,
            "First_term_fee": student_profile.First_term_fee,
            "Second_term_fee": student_profile.Second_term_fee,
            "Third_term_fee": student_profile.Third_term_fee,
        }
    }

    return Response(user_data, status=status.HTTP_200_OK)
