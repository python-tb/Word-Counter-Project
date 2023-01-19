from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == "POST":
        text = request.POST.get('text')
        words = len(text.split())

        return render(request, 'index.html', {'word_count': words, })
    else: 
        return render(request, 'index.html')

def chars(request):
    if request.method == "POST":
        text = request.POST.get('text')
        chars = len(text)

        return render(request, 'chars.html', {'char_count': chars, })
    else: 
        return render(request, 'chars.html')

def vowels(request):
    if request.method == "POST":
        text = request.POST.get('text')
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_count = 0
        for i in text:
            if i in vowels or i.lower() in vowels:
                vowel_count += 1

        return render(request, 'vowels.html', {'vowel_count': vowel_count, })
    else: 
        return render(request, 'vowels.html')

def consonants(request):
    if request.method == "POST":
        text = request.POST.get('text')
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants_count = 0
        for i in text:
            if i.isalpha():
                if i not in vowels or i.lower() not in vowels:
                    consonants_count += 1

        return render(request, 'consonants.html', {'consonants_count': consonants_count, })
    else: 
        return render(request, 'consonants.html')

def upper(request):
    if request.method == "POST":
        text = request.POST.get('text')
        up = text.upper()
        return render(request,'upper.html',{'up':up,})
    else:
        return render(request,'upper.html')


def lower(request):
    if request.method == "POST":
        text = request.POST.get('text')
        lw = text.lower()
        return render(request,'lower.html',{'lw':lw,})
    else:
        return render(request,'lower.html')