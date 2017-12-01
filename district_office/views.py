# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from reportlab.pdfgen import canvas
from .models import Car

class CarListView(generic.ListView):
  template_name = 'district_office/index.html'
  context_object_name = 'all_car_list'
  
  def get_queryset(self):
    return Car.objects.all()
    
class CarDetailView(generic.DetailView):
   model = Car
   template_name = 'district_office/detail.html'
   
   def get_queryset(self):
     return Car.objects.filter(pk=self.kwargs['pk'])
     
class CarAdd(CreateView):
    model = Car
    fields=['vin','owner','reg_no','model','mark','production_year',
	'engine_number','engine_capacity','engine_power','last_tech_exam']
    success_url = '/office/'

def card_generation_view(request, car_id):
  car = Car.objects.get(pk=car_id)
  response = HttpResponse(content_type='application/pdf')
  response['Content-Disposition'] = 'attachment; filename="'+car_id+'.pdf"'
  p = canvas.Canvas(response)
  offset = 100
  fields = car.__dict__
  for field, value in fields.items():
    if (field == "_state"):
      continue
    p.drawString(100, offset, str(field) + " - " + str(value))
    offset = offset + 50
  p.showPage()
  p.save()
  return response