from django import forms
from .models import Question, Answer


class AskForm(forms.Form):

    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        #question.author_id = self._user.id
        question.save()
        return question


class AnswerForm(forms.Form):

    text = forms.CharField(max_length=100)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question_id = self.cleaned_data["question"]
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            question = None
        return question

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = 1
        #answer.author_id = self._user.id
        answer.save()
        return answer
