# Import SINQ Django project models to be used on the admin page.
from sinq3.models import Question
from sinq3.models import QuestionImage
from sinq3.models import Hypothesis
from sinq3.models import HypothesisImage
from sinq3.models import Project
from sinq3.models import ProjectInstruction
from sinq3.models import ProjectInstructionImage
from django.contrib import admin

# Configure the admin page
class QuestionInline(admin.StackedInline):
	model = Question
	extra = 1

class ProjectAdmin(admin.ModelAdmin):
	inlines = [QuestionInline]
	list_display = ('name', 'creation_timestamp')

# Register models for the admin page
#admin.site.register(Project, ProjectAdmin)
admin.site.register(Question)
admin.site.register(QuestionImage)

admin.site.register(Hypothesis)
admin.site.register(HypothesisImage)

admin.site.register(Project)
admin.site.register(ProjectInstruction)
admin.site.register(ProjectInstructionImage)