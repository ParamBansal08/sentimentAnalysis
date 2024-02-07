from django.shortcuts import render, HttpResponse
from transformers import pipeline
# Create your views here.
def home(request):
    if(request.method=='POST'):
        form=request.POST
        text=form['text']
        print("PODPOP",request.POST,text)
        sentiment_pipeline = pipeline("sentiment-analysis")
        score = sentiment_pipeline(text)
        print(score[0]["label"])
        return render(request,'home.html',{
            'text':text,
            'score':score[0]["label"]
        })
    else:
        return render(request,'home.html',{
            # 'text':score
        })
