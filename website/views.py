import django.forms
from django.shortcuts import render
from django.db import models
from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Message, Agent, Quiz, Comment
from .forms import AgentForm, MessageForm, QuizForm, CommentForm
# Create your views here.


def home_page_view(request):
    context = {
        'bodyClass': "home-grid-container",
        'bodyName': "home-body",
        'headerClass': "header",
        'mainName': "gallery-flex-container",
        'home': True,
    }
    return render(request, 'website/index.html', context)


def about_page_view(request):
    context = {
        'bodyClass': "subpage-grid-container",
        'bodyName': "about-subpage",
        'headerClass': "",
        'mainName': "about-main",
    }
    return render(request, 'website/about.html', context)


def contacts_page_view(request):
    agentForm = AgentForm(request.POST or None)
    messageForm = MessageForm(request.POST or None)
    messageForm.fields['agentID'].widget = HiddenInput()
    tempAgent = Agent()
    dbAgentFound = False

    if agentForm.is_valid():
        agents = Agent.objects.all()
        for agent in agents:
            if agent.email == agentForm.data['email']:
                tempAgent = Agent.objects.get(pk=agent.id)
                dbAgentFound = True
                break

        if not dbAgentFound:
            task = agentForm.save()
            tempAgent = Agent.objects.get(pk=task.id)

        tempData = messageForm.data.copy()
        tempData['agentID'] = tempAgent
        messageForm.data = tempData

        if (messageForm.is_valid()):
            messageForm.save()
            return HttpResponseRedirect(reverse('website:home'))

    context = {
        'bodyClass': "subpage-grid-container",
        'bodyName': "contacts-subpage",
        'headerClass': "",
        'mainName': "contacts-centered",
        'agentForm': agentForm,
        'messageForm': messageForm,
        'agentFound': dbAgentFound,
    }
    return render(request, 'website/contacts.html', context)


def projects_page_view(request):
    context = {
        'bodyClass': "subpage-grid-container",
        'bodyName': "projects-subpage",
        'headerClass': "",
        'mainName': "project-container",
    }
    return render(request, 'website/projects.html', context)


def techniques_page_view(request):
    context = {
        'bodyClass': "subpage-grid-container",
        'bodyName': "techniques-subpage",
        'headerClass': "",
        'mainName': "techniques-main",
    }
    return render(request, 'website/techniques.html', context)


def bruhh_page_view(request):
    context = {
        'bodyClass': "subpage-grid-container",
        'bodyName': "showcase-subpage",
        'headerClass': "",
        'mainName': "project-main",
    }
    return render(request, 'website/bruhh.html', context)


def agents_page_view(request):
    if request.user.is_authenticated:
        agents = Agent.objects.all()
        context = {
            'headerText': "Contacts Established",
            'agents': agents
        }

        return render(request, 'website/agents.html', context)
    else:
        return HttpResponseRedirect(reverse('users:home'))



def agent_messages_page_view(request, agent_id):
    if request.user.is_authenticated:
        agent = Agent.objects.get(pk=agent_id)
        messages = Message.objects.all()
        context = {
            'headerText': "Contact Messages",
            'agent': agent,
            'messages': messages,
        }

        return render(request, 'website/agent-messages.html', context)
    else:
        return HttpResponseRedirect(reverse('users:home'))


def agent_edit_page_view(request, agent_id):
    if request.user.is_authenticated:
        agent = Agent.objects.get(pk=agent_id)
        form = AgentForm(request.POST or None, instance=agent)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('website:agents'))

        context = {
            'headerText': "Edit Contact",
            'agent': agent,
            'agent_id': agent_id,
            'form': form,
        }

        return render(request, 'website/agent-edit.html', context)
    else:
        return HttpResponseRedirect(reverse('users:home'))


def agent_add_page_view(request):
    if request.user.is_authenticated:
        agentForm = AgentForm(request.POST or None)

        if agentForm.is_valid():
            agentForm.save()
            return HttpResponseRedirect(reverse('website:agents'))

        context = {
            'headerText': "Add Contact",
            'agentForm': agentForm,
        }
        return render(request, 'website/agent-add.html', context)
    else:
        return HttpResponseRedirect(reverse('users:home'))


def message_add_page_view(request):
    if request.user.is_authenticated:
        messageForm = MessageForm(request.POST or None)

        if messageForm.is_valid():
            messageForm.save()
            return HttpResponseRedirect(reverse('website:agents'))

        context = {
            'headerText': "Add Message",
            'messageForm': messageForm,
        }
        return render(request, 'website/message-add.html', context)
    else:
        return HttpResponseRedirect(reverse('users:home'))


def agent_delete_page_view(request, agent_id):
    if request.user.is_authenticated:
        Agent.objects.get(pk=agent_id).delete()
        return HttpResponseRedirect(reverse('website:agents'))
    else:
        return HttpResponseRedirect(reverse('users:home'))



def message_delete_page_view(request, message_id):
    if request.user.is_authenticated:
        Message.objects.get(pk=message_id).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponseRedirect(reverse('users:home'))



def previous_page_view(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def quiz_page_view(request):
    context = {
        'headerText': "Quiz",
        'quizzes': Quiz.objects.all().order_by("correctAnswers").reverse()
    }

    return render(request, 'website/quiz.html', context)


def quiz_scores_page_view(request):
    context = {
        'headerText': "Quiz Scores",
        'quizzes': Quiz.objects.all().order_by("correctAnswers").reverse()
    }

    return render(request, 'website/quiz-scores.html', context)


def do_quiz_page_view(request):
    form = QuizForm(request.POST or None)
    if form.is_valid():
        current_form = form.save(commit=False)

        if current_form.most_popular_family_games_developer == "NINTENDO":
            current_form.correctAnswers += 1
        if current_form.assassins_Creed_franchise_developer == "UBISOFT":
            current_form.correctAnswers += 1
        if current_form.pokemon_Yellow_release_year == "1998":
            current_form.correctAnswers += 1
        if current_form.pokemon_Yellow_developer == "GAME FREAK":
            current_form.correctAnswers += 1
        if current_form.most_sold_game_of_all_time == "MINECRAFT":
            current_form.correctAnswers += 1
        if current_form.most_sold_console_of_all_time == "PLAYSTATION 2":
            current_form.correctAnswers += 1
        if current_form.first_commercial_game == "PONG":
            current_form.correctAnswers += 1
        if current_form.most_sold_game_on_PlayStation_1 == "GRAN TURISMO":
            current_form.correctAnswers += 1
        if current_form.most_popular_arcade_game == "SPACE INVADERS":
            current_form.correctAnswers += 1
        if current_form.name_of_the_first_main_character_from_Minecraft == "STEVE":
            current_form.correctAnswers += 1

        current_form.save()
        return HttpResponseRedirect(reverse('website:quiz'))

    context = {
        'headerText': "Quiz",
        'quizForm': form
    }

    return render(request, 'website/do-quiz.html', context)


def comments_page_view(request):
    comments = Comment.objects.all()
    context = {
        'headerText': "Comments",
        'comments': comments,
    }
    return render(request, 'website/comments.html', context)


def comment_add_page_view(request):
    commentForm = CommentForm(request.POST or None)

    if (commentForm.is_valid()):
        commentForm.save()
        return HttpResponseRedirect(reverse('website:comments'))

    context = {
        'headerText': "Add comment",
        'commentForm': commentForm,
    }
    return render(request, 'website/comment-add.html', context)
