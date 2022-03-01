from django.urls import path
from polls import views



app_name = "Polls"

urlpatterns = [
    path("", views.Polls_indexView.as_view(), name="Polls_index"),
    path("<int:pk>/", views.Polls_detailView.as_view(), name="Polls_detail"),
    path("<int:pk>/results/", views.Polls_resultsView.as_view(), name="Polls_results"),
    path("<int:question_id/vote/", views.Polls_vote, name="Polls_vote"),

]

    

    