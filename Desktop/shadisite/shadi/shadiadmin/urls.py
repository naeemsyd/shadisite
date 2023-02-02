from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("index",views.index,name="index"),
    path("userstable",views.userstable,name="userstable"),
    path("useradd",views.useradd,name="useradd"),
    path("useredit",views.useredit,name="useredit"),
    path("religion",views.religion,name="religion"),
    path("religionadd",views.religionadd,name="religionadd"),
    path("religionedit",views.religionedit,name="religionedit"),
    path("religioncategory",views.religioncategory,name="religioncategory"),
    path("religioncategoryadd",views.religioncategoryadd,name="religioncategoryadd"),
    path("religioncategoryedit",views.religioncategoryedit,name="religioncategoryedit"),
    path("state",views.state,name="state"),
    path("stateadd",views.stateadd,name="stateadd"),
    path("stateedit",views.stateedit,name="stateedit"),
    path("education",views.education,name="education"),
    path("educationadd",views.educationadd,name="educationadd"),
    path("educationedit",views.educationedit,name="educationedit"),
    path("occupation",views.occupation,name="occupation"),
    path("occupationadd",views.occupationadd,name="occupationadd"),
    path("occupationedit",views.occupationedit,name="occupationedit"),
    path("mothertongue",views.mothertongue,name="mothertongue"),
    path("mothertongueadd",views.mothertongueadd,name="mothertongueadd"),
    path("mothertongueedit",views.mothertongueedit,name="mothertongueedit"),







]