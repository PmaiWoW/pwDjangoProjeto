from django import forms
from django.forms import ModelForm
from .models import Message, Agent, Quiz, Comment


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'

    def emailToString(self):
        return str(self.fields['email'])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'style': 'color: black'})


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'style': 'color: black'})


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
        exclude = ['correctAnswers']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'style': 'color: black'})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'style': 'color: black'})
