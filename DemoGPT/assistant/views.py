from django.shortcuts import render
from django.http import JsonResponse
import openai
from openai import OpenAIError, Completion
from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    return render(request, 'assistant/home.html')

#chatgpt making a response is here:
def query_view(request): 
    
    if request.method == 'GET': 
        ingredients = request.GET.get('ingredients', '')
        messages = []
        messages.append({"role": "user", "content": "make me a recipe using " + ingredients})
        
        openai.api_key = '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'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages
        )
        print("ingredients: ", ingredients)
        recipe = response['choices'][0]['message']['content']
        print(recipe)
        
        return JsonResponse({'response': recipe}) 
def rev_search(request): 
    
    if request.method == 'GET': 
        ingredients = request.GET.get('ingredients', '')
        budget = request.GET.get('budget', '')
        messages = []
        messages.append({"role": "user", "content": "make me " + ingredients + "with a budget of" + budget + "dollars"})
        
        openai.api_key = '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'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages
        )
        print("dish: ", ingredients)
        print("budget: ", budget)
        recipe = response['choices'][0]['message']['content']
        print(recipe)
        
        return JsonResponse({'response': recipe}) 