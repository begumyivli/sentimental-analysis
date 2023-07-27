import pickle
from .preprocess import preprocess
from django.shortcuts import render

# Load the logistic regression model
with open('Sentiment-LR.pickle', 'rb') as file:
    LRmodel = pickle.load(file)

# Used to convert a collection of raw text documents (tweets) into a matrix of TF-IDF, loading this
with open('vectoriser-ngram-(1,2).pickle', 'rb') as file:
    vectoriser = pickle.load(file)

def analyze_sentiment_text(request):
    if request.method == 'POST':
        input_text = request.POST['input_text']

        # Preprocess the input text using preprocess.py in same directory
        processed_text = preprocess([input_text])

        # Vectorize the processed text
        text_data = vectoriser.transform(processed_text)

        # Predict the sentiment using the logistic regression model
        sentiment = LRmodel.predict(text_data)[0]

        # Convert the numeric sentiment to a readable label
        result = "Positive" if sentiment == 1 else "Negative"

        return render(request, 'index.html', {'result': result})
    else:
        return render(request, 'index.html')


def analyze_sentiment_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file'] #  This is a dictionary-like object that contains all the uploaded files submitted with the request
        # file : This is the key used to access the uploaded file
        content = uploaded_file.read().decode('utf-8')

        # Preprocess the content of the uploaded file
        processed_text = preprocess([content])

        # Vectorize the processed text
        text_data = vectoriser.transform(processed_text)

        # Predict the sentiment using the logistic regression model
        sentiment = LRmodel.predict(text_data)[0]

        # Convert the numeric sentiment to a readable label
        result = "Positive" if sentiment == 1 else "Negative"

        return render(request, 'index.html', {'result': result})
    else:
        return render(request, 'index.html')
