from django.shortcuts import render, redirect
from django.urls import reverse
from .inference import load_model, get_prediction
from.forms import TestingForm
# Create your views here.

model_ins = None

def index(request):
    return render(request, "yolov5/index.html")

def choice_model(request):
    return render(request, "yolov5/choice_model.html")

def testing(request, model_name):
    context = {}
    context["model_name"] = model_name
    if request.method == 'POST':
        model_ins = load_model(model_name)
        form = TestingForm(request.POST, request.FILES)
        if form.is_valid():
            iou = form.cleaned_data["iou"] if form.cleaned_data["iou"] else None
            conf = form.cleaned_data["conf"] if form.cleaned_data["conf"] else None
            image_bytes = request.FILES['image'].read()
            predicted_class, probability = get_prediction(image_bytes, model_ins, conf, iou)
            print(probability)
            return render(request, "yolov5/result.html", {"class_name":predicted_class, "proba":int(probability*100)})
    else:
        form = TestingForm()
    context["form"] = form
    return render(request, "yolov5/testing.html", context)