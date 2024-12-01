from django import forms
from blog.models import Comment
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]  # Campos del formulario

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()  # Instancia FormHelper
        self.helper.form_method = "post"  # Método POST para el formulario
        self.helper.add_input(Submit('submit', 'Submit'))  # Botón de envío
