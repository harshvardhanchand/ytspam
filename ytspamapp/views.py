from django.shortcuts import render


from django.apps import apps

from django.http import JsonResponse

def classify_text(request):  
    # Get the model and vectorizer from the AppConfig
    model = apps.get_app_config('ytspamapp').model
    vectorizer = apps.get_app_config('ytspamapp').vectorizer

    # Check if the request method is POST
    if request.method == 'POST':  
        # Check if the 'text' field is present in the POST data and it's not empty
        if 'text' in request.POST and request.POST['text'].strip():
            text = request.POST['text']  
            # Preprocess and transform the input text  
            X = vectorizer.transform([text])  
            X = X.toarray()  

            # Use the model to classify the text  
            classification = model.predict(X)  
            if classification == 1:  
                result = "Not Spam"  
            else:  
                result = "Spam"  
            # Return the result to the user
            return JsonResponse({'classification': result})

        else:
            # If the 'text' field is missing or empty, return an error message
            return JsonResponse({'error': 'The text field is required.'})

    # If the request method is not POST, render the classify_text page
    return render(request, 'ytspamapp/classify_text.html')

# Create your views here.
