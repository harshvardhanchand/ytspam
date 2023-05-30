from django.shortcuts import render


from django.apps import apps

from django.http import JsonResponse

def classify_text(request):
    model = apps.get_app_config('ytspamapp').model
    vectorizer = apps.get_app_config('ytspamapp').vectorizer

    result = "Please enter a comment to classify."

    if request.method == 'POST':
        if 'text' in request.POST and request.POST['text'].strip():
            text = request.POST['text']
            X = vectorizer.transform([text])
            X = X.toarray()
            classification = model.predict(X)
            if classification == 1:
                result = "Not Spam"
            else:
                result = "Spam"
        else:
            return render(request, 'ytspamapp/classify_text.html', {'classification': "Error: The text field is required."})

    return render(request, 'ytspamapp/classify_text.html', {'classification': result})


# Create your views here.
