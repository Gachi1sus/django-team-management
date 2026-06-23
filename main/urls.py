from django.urls import path
from .views import members_list, member_detail, add_member, edit_member, delete_member, login_user, logout_user, faction_detail, api_members_list, api_member_detail

urlpatterns = [
    path('members/', members_list, name='members_list'),
    path('members/<int:id>/', member_detail, name='member_detail'),
    path('add-member/', add_member, name='add_member'),
    path('members/<int:id>/edit/', edit_member, name='edit_member'),
    path('members/<int:id>/delete/', delete_member, name='delete_member'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('factions/<int:id>/', faction_detail, name='faction_detail'),
    path('api/members/', api_members_list, name='api_members_list'),
    path('api/members/<int:id>/', api_member_detail, name='api_member_detail'),
]