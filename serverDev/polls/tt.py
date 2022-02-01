
from models import Choice, Question
from django.utils import timezone



q = Question(question_text="What's new?", pub_date=timezone.now())