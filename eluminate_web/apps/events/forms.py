from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Layout, Field, Div, HTML
from crispy_forms.bootstrap import FormActions

from .models import Event


class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ("name", 
                  "start_time",
                  "end_time",
                  "days",
                  "location",
                  "description",
                  "collaborators")
        widgets = {
                   'days' : CheckboxSelectMultiple
                   }
        
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'saveLocation'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.help_text_inline = True
        self.helper.layout = Layout(
            Div(Field('location', template="events/_location_form_field.html",),
                Field('name'),
                Field("start_time"),
                Field("end_time"),
                Field("days"),
                Field("collaborators"),
                Field("description"),
                FormActions(
                            Submit('submit', 'Save', css_class="btn btn-primary")
                            )
                )
            )
        
        super(EventForm, self).__init__(*args, **kwargs)

        # Overriding the help text due to a django bug:
        # https://code.djangoproject.com/ticket/9321
        self.fields['days'].help_text = ''
        self.fields['collaborators'].help_text = 'Hold down "Control", or "Command" on a Mac, to select more than one.\
                                           To de-select, hold down "Control", or "Command" on a Mac, and click on the selected option'
        
                                                  
                
 
                
        