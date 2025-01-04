## HR  Newsline Classifier 
The HR Headlines Classifier is a RESTful API service for classifying the HR headlines into pre-defined categories such as alert, money,career and data privacy.It uses the Django Rest Framework (DRF) and the BERT Transformer model (using bert-tensorflow library) for text classification.
## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Overview](#overview)
- [Endpoints](#endpoints)
- [Contact](#contact)
## Features
- RESTful API: Implemented the backend using Django Rest Framework.
- TF BERT Text Classification: Uses TF BERT model for classifying news articles into predefined categories.
- Django AuthToken Authentication: Secure your API with Django-restframework-authtoken.
## Requirements
- Python 3.7+
- Django 3.2+
- Django Rest Framework 3.12+
- bert-tensorflow 1.0.1
- TensorFlow 2.4+
## Installation

### Clone the repository
```bash
git clone https://github.com/Shreya-StagAI/hr-newsline-classifier.git
cd hr-newsline-classifier
```
### Create a virtual environment 
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```
### Install the dependencies
```bash
pip install -r requirements.txt
```
### Apply migrations
```bash
python manage.py migrate
```
### Create a superuser
```bash
python manage.py createsuperuser
```
### Run the server
```bash
python manage.py runserver
```
## Usage 
To facilitate the deployment process, leverage the existing Docker image on the Docker Hub repository.
### Clone the repository
### Pull the docker image:
 ```bash
  docker pull shreyaagarg/mydjangoapp
  ```
### Run the docker container:
  ```bash
  docker run -p 8000:8000 shreyaagarg/mydjangoapp
  ```
### Access the application at http://localhost:8000


## Overview
### Login Page
![image](https://github.com/Shreya-StagAI/django-hrnewsline-classification/assets/171024676/60b65c6d-2d9b-4c30-8e24-2d566955fb5a)

### Registration Page
![image](https://github.com/Shreya-StagAI/django-hrnewsline-classification/assets/171024676/6ef21140-5cb3-42c4-ac15-c3934d497dd4)

![image](https://github.com/Shreya-StagAI/django-hrnewsline-classification/assets/171024676/ec33280a-bf09-429b-b4ab-0c4ba0aac90f)


### Home page
![image](https://github.com/Shreya-StagAI/django-hrnewsline-classification/assets/171024676/6dc756c2-06e4-4168-8850-1a279a3c9cde)

### Enter HR Newsline Page
![image](https://github.com/Shreya-StagAI/django-hrnewsline-classification/assets/171024676/d1877b8c-8727-4186-bf49-00a8d91348ab)

### Results with Predicted category on the Home page 
![image](https://github.com/Shreya-StagAI/django-hrnewsline-classification/assets/171024676/e2d96dec-443c-457f-b021-f3673138dd75)
## Endpoints

### Authentication
- `POST /api/login/`: Login with username and password to obtain a token.
- `POST /api/register/`: Register a new user.

### Example Requests

#### Register a New User
```bash
POST /api/register/
Content-Type: application/json

{
    "username": "newuser",
    "password": "newpassword",
    "email": "newuser@example.com"
}
```
### Login
```bash
POST /api/login/
Content-Type: application/json

{
    "username": "newuser",
    "password": "newpassword"
}
```

## Contact
For any questions or inquiries, please contact the project maintainer:
- Name: Shreya Garg
- Email: shreyagarg754@gmail.com
- GitHub: Itsshreyagarg

