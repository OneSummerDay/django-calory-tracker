from django.shortcuts import render, redirect
from food_consuming.models import Food, Consume
from django.http import HttpResponse


from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foods'] = Food.objects.all()
        context['consumed_food'] = Consume.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        return redirect('/')
