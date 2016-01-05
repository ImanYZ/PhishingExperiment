#!/usr/bin/env python

from django.contrib.auth.models import User
if User.objects.count() == 0:
    admin = User.objects.create(username='Iman')
    admin.set_password('i1111114')
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()