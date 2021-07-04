from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('index', views.home_page_view, name='home'),
    path('about', views.about_page_view, name='about'),
    path('projects', views.projects_page_view, name='projects'),
    path('contacts', views.contacts_page_view, name='contacts'),
    path('techniques', views.techniques_page_view, name='techniques'),
    path('bruhh', views.bruhh_page_view, name='bruhh'),
    path('agents', views.agents_page_view, name='agents'),
    path('agent-messages/<int:agent_id>', views.agent_messages_page_view, name='agent-messages'),
    path('agent-edit/<int:agent_id>', views.agent_edit_page_view, name='agent-edit'),
    path('agent-delete/<int:agent_id>', views.agent_delete_page_view, name='agent-delete'),
    path('agent-add', views.agent_add_page_view, name='agent-add'),
    path('message-add', views.message_add_page_view, name='message-add'),
    path('message-delete/<int:message_id>', views.message_delete_page_view, name='message-delete'),
    path('quiz', views.quiz_page_view, name='quiz'),
    path('quiz-scores', views.quiz_scores_page_view, name='quiz-scores'),
    path('do-quiz', views.do_quiz_page_view, name='do-quiz'),
    path('comments', views.comments_page_view, name='comments'),
    path('comment-add', views.comment_add_page_view, name='comment-add'),
    path('previous', views.previous_page_view, name='previous'),
]