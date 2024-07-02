

# YouTube Spam Classifier

This is a machine learning web app that classifies YouTube comments as spam or not spam. It uses:

- Django for the web framework 
- scikit-learn for the machine learning 
- NLP and TF-IDF vectorization to process the text 
- Logistic regression for the classification model

## Data

The training data is a CSV file containing thousands of YouTube comments labeled as spam or not spam.

## Model

The model pipeline is:

1. Load the data and vectorize the text using TF-IDF
2. Train a logistic regression model on the vectorized data
3. Save the model to disk

The model is retrained each time the server is started.

## Web App

The web app allows you to submit your own YouTube comments and see if they are classified as spam or not spam.
The Django view passes the submitted comment text to the model and displays the prediction.

## Usage

1. Clone the repo
2. Install requirements: `pip install -r requirements.txt`
3. Run Django server: `python manage.py runserver`
4. Visit http://127.0.0.1:8000/ and enter YouTube comments to classify!

## Future Improvements

Some ways this project could be improved in the future:

- Use a larger dataset for training 
- Experiment with other classification models like SVMs 
- Add user accounts and save classification history
- Track model metrics like accuracy, F1 score, etc. 
- Add an API to classify comments programmatically


