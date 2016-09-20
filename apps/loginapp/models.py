from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, postdata):
        response = {}
        response['errors'] = []
        response['success'] = []
        if not postdata['email']:
            response['errors'].append('Email is blank')
        if not EMAIL_REGEX.match(postdata['email']):
            response['errors'].append('Not a valid email address')
        if not postdata['first_name']:
            response['errors'].append('First name is blank')
        if not postdata['last_name']:
            response['errors'].append('Last name is blank')
        if not postdata['password']:
            response['errors'].append('Password is blank')
        if postdata['password'] != postdata['confirmpw']:
            response['errors'].append('Password does not match')
        if not response['errors']:
            password = postdata['password']
            password = password.encode()
            hashedpw = bcrypt.hashpw(password, bcrypt.gensalt())
            try: 
                newuser = Users.userManager.create(first_name = postdata['first_name'], last_name = postdata['last_name'], email = postdata['email'],password = hashedpw)
                response['success'].append('User Created')
                return response
            except:
                response['errors'].append('Unable to add to DB')
                return response
        else:
            return response
    def login(self, postdata):
        response = {}
        response['errors'] = []
        response['success'] = []
        password = postdata['password']
        password = password.encode()
        try: 
            user = Users.userManager.get(email = postdata['email'])
            print user
            print user.password
        except:
            response['errors'].append('email not found')
            return response

        hashedpw = user.password
        hashedpw = hashedpw.encode()
        if bcrypt.hashpw(password, hashedpw) == hashedpw:
            response['success'].append('login successful')
            return response
        else:
            response['errors'].append('passwords do not match')
            return response
            
# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    userManager = UserManager()