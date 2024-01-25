from django.urls import path
from .views import person_list, delete_person, add_person, UpdateMatchCountView

urlpatterns = [
    path('', person_list, name='person_list'),
    path('person/add/', add_person, name='add_person'),
    path('person/<int:person_id>/delete/', delete_person, name='delete_person'),
    path('api/update_match_count/<int:person_id>/', UpdateMatchCountView.as_view(), name='update_match_count'),
]
