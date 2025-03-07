from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCompleteView,
    ToggleCompleteView,
)


urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('completed/', TaskCompleteView.as_view(), name='task_complete'),
    # path('<int:pk>/mark-complete/', MarkCompleteView.as_view(), name='task_mark_completed'),
    path('<int:pk>/toggle-complete/', ToggleCompleteView.as_view(), name='task_toggle_complete'),
]