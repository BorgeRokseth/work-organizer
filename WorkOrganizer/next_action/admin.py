from django.contrib import admin
from next_action.models import Project, NextAction, Context

admin.site.register([Project, NextAction, Context])