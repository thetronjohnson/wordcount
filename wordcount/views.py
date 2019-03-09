from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def count(request):
    text = request.GET['text']
    wordlist = text.split()
    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    return render(request,'count.html',{'word_dict':word_dict})