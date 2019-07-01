from models import Model
import time
from movieclassifier.classifier import classify, train
from utils import local_time


class Review(Model):
    def __init__(self, form):
        self.id = None
        self.movie = None
        self.content = form.get('content')
        self.creat_time = int(time.time())
        self.upgrade_time = self.creat_time
        self.classification = None
        self.positive = None

    def get_classification(self):
        result = classify(self.content)
        self.classification = result[0]
        self.positive = round(result[1], 4)
