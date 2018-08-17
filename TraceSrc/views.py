from django.shortcuts import render, redirect, HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

# index front-to-end connector
def index(req):
    ctx = dict()
    return render(req, r'../templates/pages/graph.html', ctx)
