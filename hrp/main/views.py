from django.shortcuts import render, redirect
from .forms import RegisterForm, hrform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from datetime import datetime
from .models import Post
from django.http import JsonResponse
from .serializers import HR, LoginSerializer, RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from transformers import BertTokenizer, TFBertForSequenceClassification
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import os
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token

# Create your views here.


tokenizer = BertTokenizer.from_pretrained('C:/Users/DELL/Documents/task_internship/tokenizer')
model = TFBertForSequenceClassification.from_pretrained('C:/Users/DELL/Documents/task_internship/hr_newsline_classifier')

dataset_path = os.path.join(settings.BASE_DIR, 'data', 'hr_newsline_dataset.csv')

df = pd.read_csv(dataset_path)

label_encoder = LabelEncoder()
label_encoder.fit(df['Category'])

def predict_category(announcement):
    encoding = tokenizer(
        announcement,
        truncation=True,
        padding=True,
        max_length=64,
        return_tensors='tf'
    )
    logits = model(encoding).logits
    predicted_class_id = np.argmax(logits, axis=1)[0]
    predicted_category = label_encoder.inverse_transform([predicted_class_id])[0]
    return predicted_category


@api_view(['GET', 'POST'])
def hr_list(request, format=None):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = HR(posts, many=True)
        return JsonResponse({"posts": serializer.data})

    if request.method == 'POST':
        serializer = HR(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def hr_detail(request, id, format=None):
    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer = HR(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HR(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# API view for user registration
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })






# def home(request):
#     posts = Post.objects.all()
#
#     #categorize existing announceme
@login_required
def home(request):
    posts = Post.objects.all()

    categorized_posts = [
        {
            'id': post.id,
            'hr_newsline': post.hr_newsline,
            'category': post.predicted_category,  # Use the value from the database
            'user_name': post.user_name,
            'datetime': post.datetime
        }
        for post in posts
    ]

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.user_name == request.user:
            post.delete()

    return render(request, 'main/home.html', {'posts': categorized_posts})

@login_required
def create_hrnews(request):
    if request.method == 'POST':
        form = hrform(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.datetime = datetime.now()
            post.user_name = request.user
            post.hr_newsline = form.cleaned_data['hr_newsline']


            predicted_category = predict_category(post.hr_newsline)
            post.predicted_category = predicted_category
            post.save()

        return redirect("/home")

    else:
        form = hrform()

    return render(request, 'main/create_hrnews.html', {"form": form})


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("User authenticated and logged in")
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')






