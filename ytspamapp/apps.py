from django.apps import AppConfig
import joblib

class YtspamappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ytspamapp"

    def ready(self):
        super().ready()

        # Load the model and vectorizer when the app is ready
        self.model = joblib.load('ytspam/models/model.pkl')
        self.vectorizer = joblib.load('ytspam/models/vectorizer.pkl')
