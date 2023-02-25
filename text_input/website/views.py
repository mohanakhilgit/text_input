from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def display(request):
    text = request.POST['txt_input']
    return render(request, 'display.html', {'text': text})
