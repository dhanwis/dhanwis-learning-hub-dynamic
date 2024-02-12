from django.urls import path
from admin_app.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('course/add/', course_add, name='course-add'),
    path('course/list/', course_list, name='course-list'),
    path('course/<int:course_id>/edit/', course_edit, name='course-edit'),
    path('course/<int:course_id>/delete/', course_delete, name='course-delete'),
    
    path('company/', company_list, name='company-list'),
    path('company/<int:company_id>/', company_detail, name='company-detail'),
    path('company/add/', company_add, name='company-add'),
    path('company/<int:company_id>/edit/', company_edit, name='company-edit'),
    path('company/<int:company_id>/delete/', company_delete, name='company-delete'),

    path('placements/', placement_list, name='placement-list'),
    path('placements/<int:placement_id>/', placement_detail, name='placement-detail'),
    path('placements/add/', placement_add, name='placement-add'),
    path('placements/<int:placement_id>/edit/', placement_edit, name='placement-edit'),
    path('placements/<int:placement_id>/delete/', placement_delete, name='placement-delete'),

    path('gallery/', gallery_list, name='gallery-list'),
    path('gallery/<int:gallery_id>/', gallery_detail, name='gallery-detail'),
    path('gallery/add/', gallery_add, name='gallery-add'),
    path('gallery/<int:gallery_id>/edit/', gallery_edit, name='gallery-edit'),
    path('gallery/<int:gallery_id>/delete/', gallery_delete, name='gallery-delete'),
]