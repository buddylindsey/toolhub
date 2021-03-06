from crispy_forms.layout import Fieldset, Submit, Field, Div
from django import forms
from django.utils.translation import ugettext_lazy as _

from tools.models import ClearancePermission, UserTool
from utils.forms import CrispyFormMixin


class UserToolCreateForm(CrispyFormMixin, forms.ModelForm):
    action_button_label = _("Add tool")
    form_action = "tools:create"

    def __init__(self, *args, **kwargs):
        super(UserToolCreateForm, self).__init__(cols=(2, 10), *args, **kwargs)

    def layout_args(self, helper):
        return (
            Fieldset(
                None,
                Field("title"),
                Field("description", css_class="h-100", label_class="", field_class=""),
                Field("taxonomies"),
                Field("visibility"),
                Field("clearance"),
            ),
            Div(
                Div(Submit("action", self.action_button_label), css_class="offset-md-2"),
                css_class="form-group",
            ),
        )

    class Meta:
        fields = ("title", "description", "taxonomies", "visibility", "clearance")
        model = UserTool


class UserToolUpdateForm(UserToolCreateForm):
    action_button_label = _("Update tool")
    form_action = "tools:edit"
    pk_field = "pk"


class UserToolFilterViewForm(CrispyFormMixin, forms.Form):
    has_columns = False

    def layout_args(self, helper):
        helper.form_method = "GET"
        return (
            Field("name"),
            Field("state"),
            Field("taxonomies"),
            Submit("action", _("Filter")),
            # Button('clear', _("Clear Filter"), type="reset")
        )


class ClearancePermissionForm(CrispyFormMixin, forms.ModelForm):
    class Meta:
        fields = ("cleared_user", "tool")
        model = ClearancePermission

    def layout_args(self, helper):
        return (
            Field("tool", type="hidden"),
            Field("cleared_user"),
            Submit("action", _("Clear Person"), css_class="offset-md-3"),
        )

    def clean_cleared_user(self):
        tool = self.initial.get("tool")
        cleared_user = self.cleaned_data.get("cleared_user")

        if (
            cleared_user
            and ClearancePermission.objects.filter(tool=tool, cleared_user=cleared_user).exists()
        ):
            raise forms.ValidationError(_("This person already has clearance to use this tool."))

        return cleared_user
