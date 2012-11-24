# Import SINQ Django project models to be used on the admin page.
from sinq3.models import Question
from sinq3.models import QuestionImage
from sinq3.models import CauseAndEffect
from sinq3.models import CauseAndEffectImage
from sinq3.models import Investigation
from sinq3.models import InvestigationStep
from sinq3.models import InvestigationStepImage
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

admin.site.register(CauseAndEffect)
admin.site.register(CauseAndEffectImage)

admin.site.register(Investigation)
admin.site.register(InvestigationStep)
admin.site.register(InvestigationStepImage)