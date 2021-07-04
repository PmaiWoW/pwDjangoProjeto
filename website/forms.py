from django import forms
from django.forms import ModelForm
from .models import Message, Agent, Quiz, Comment


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'

    def emailToString(self):
        return str(self.fields['email'])


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
        exclude = ['correctAnswers']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
