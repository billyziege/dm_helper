from typing import List, Tuple

from flask_wtf import FlaskForm
from wtforms.fields import SelectMultipleField
from wtforms.validators import StopValidation
from wtforms import widgets, Form, BooleanField, StringField, PasswordField, validators

from dm_helper.models.account_management.accounts import User
from dm_helper.models.account_management.roles import roles_enum


class MultiCheckboxField(SelectMultipleField):
    """
    Field with multiple checkboxes.
    """
    widget = widgets.ListWidget(html_tag='ul', prefix_label=False)
    option_widget = widgets.CheckboxInput()


class MultiCheckboxAtLeastOne(object):
    """
    Captures the validation of the MultipleCheckboxField so that at least one checkbox is checked.
    """
    def __init__(self, message: str = None):
        if not message:
            message = 'At least one option must be selected.'
        self.message = message

    def __call__(self, form, field):
        if len(field.data) == 0:
            raise StopValidation(self.message)


class MultiCheckboxForced(object):
    """
    Captures the validation of the MultipleCheckboxField enforcing that the given value must be present.
    """
    def __init__(self, forced_option: str, option_enum: List[Tuple[int, str]], message=None):
        if not message:
            message = 'The option {} must be chosen.'.format(forced_option)
        self.forced = None
        for pair in option_enum:
            if pair[1] == forced_option:
                self.forced = pair[0]
                break
        if self.forced is None:  # Forced not found.
            err_msg = "No option {} found. ".format(forced_option)
            err_msg += "Options are: " + " ,".join([pair[1] for pair in option_enum])
        self.message = message

    def __call__(self, form, field):
        if self.forced not in field.data:
            raise StopValidation(self.message)


class FullRegistrationForm(Form, forced_option: str = None):
    username = StringField('Username', [validators.Length(min=4, max=User.username_max)])
    full_name = StringField('Full Name', [validators.Length(min=0, max=User.full_name_max)])

    email = StringField('Email Address', [validators.Length(min=6, max=User.email_max)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    if force_option == None:
        roles = MultiCheckboxField('Roles', choices=get_roles_enum(), validators=[MultiCheckboxAtLeastOne()], coerce=int)
    else:
        roles = MultiCheckboxField('Roles', choices=get_roles_enum(), validators=[MultiCheckboxForced(forced_option, get_roles_enum())], coerce=int)
