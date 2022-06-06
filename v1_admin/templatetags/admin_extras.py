from django import template
from ..forms import TargetForm

register = template.Library()


@register.inclusion_tag('v1_admin/target_form.html', takes_context=True)
def show_comment_form(context, form=None):
    if form is None:
        form = TargetForm()
    return {
        'form': form,
    }