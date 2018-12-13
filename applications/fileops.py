from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
import sys
import os
import glob

def get_search(request):
    return render(request, "applications/fops/search.html")

def post_search(request):
    fname = request.POST["filename"]
    if not fname:
        return redirect(reverse("applications:fops_get_search"))

    res = glob.glob("../../edsenv/images/*" + fname + "*.jpg")
    return render(request, "applications/fops/search.html", {"res": res})
