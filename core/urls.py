from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings


from . import views

app_name = 'core'

urlpatterns = [
    path(r'', views.PersonListView.as_view(), name='home'),
    path(r'department/', views.DepartmentListView.as_view(), name='department_list'),
    path(r'department/create', views.DepartmentCreateView.as_view(),
         name='department_create'),
    path(r'department/update/<int:pk>/', views.DepartmentUpdateView.as_view(),
         name='department_update'),
    path(r'department/delete/<int:pk>/', views.DepartmentDeleteView.as_view(),
         name='department_delete'),
    path(r'staff/', views.StaffListView.as_view(), name='staff_list'),
    path(r'staff/create', views.StaffCreateView.as_view(),
         name='staff_create'),
    path(r'staff/update/<int:pk>/', views.StaffUpdateView.as_view(),
         name='staff_update'),
    path(r'staff/delete/<int:pk>/', views.StaffDeleteView.as_view(),
         name='staff_delete'),
    path(r'state/', views.StateListView.as_view(), name='state_list'),
    path(r'state/create', views.StateCreateView.as_view(),
         name='state_create'),
    path(r'state/update/<int:pk>/', views.StateUpdateView.as_view(),
         name='state_update'),
    path(r'state/delete/<int:pk>/', views.StateDeleteView.as_view(),
         name='state_delete'),

    path(r'lga/', views.LGAListView.as_view(), name='lga_list'),
    path(r'lga/create', views.LGACreateView.as_view(),
         name='lga_create'),
    path(r'lga/update/<int:pk>/', views.LGAUpdateView.as_view(),
         name='lga_update'),
    path(r'lga/delete/<int:pk>/', views.LGADeleteView.as_view(),
         name='lga_delete'),
    path(r'accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path(r'accounts/logout/', auth_views.LogoutView.as_view(),
         {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path(r'person/', views.PersonListView.as_view(), name='person_list'),
    path(r'person/create', views.PersonCreateView.as_view(),
         name='person_create'),
    path(r'person/update/<int:pk>/', views.PersonUpdateView.as_view(),
         name='person_update'),
    path(r'person/delete/<int:pk>/', views.PersonDeleteView.as_view(),
         name='person_delete'),
    path(r'person/detail/<int:pk>/', views.PersonDetailView.as_view(),
         name='person_detail'),
]
