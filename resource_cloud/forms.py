from flask.ext.wtf import Form
from wtforms_alchemy import model_form_factory
from wtforms import BooleanField, StringField, TextField
from wtforms.validators import DataRequired, Email, Length

from resource_cloud.models import MAX_EMAIL_LENGTH, MAX_NAME_LENGTH, MAX_PASSWORD_LENGTH
from resource_cloud.server import db

BaseModelForm = model_form_factory(Form)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session


class UserForm(ModelForm):
    email = StringField('email', validators=[DataRequired(), Email(), Length(max=MAX_EMAIL_LENGTH)])
    password = StringField('password', default=None)
    is_admin = BooleanField('is_admin', default=False)


class ResourceForm(ModelForm):
    name = StringField('name', validators=[DataRequired(), Length(max=MAX_NAME_LENGTH)])
    config = StringField('config', validators=[DataRequired()])
    plugin = StringField('plugin', validators=[DataRequired()])
    is_enabled = BooleanField('is_enabled', default=False)


class ChangePasswordForm(ModelForm):
    password = StringField('password', validators=[DataRequired(), Length(
        min=8,
        max=MAX_PASSWORD_LENGTH, message=("Password must be between %(min)d and "
                                          "%(max)d characters long"))])


class ProvisionedResourceForm(ModelForm):
    resource = StringField('resource_id', validators=[DataRequired()])


class SessionCreateForm(ModelForm):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])


class ActivationForm(ModelForm):
    token = StringField('token', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired(), Length(
        min=8,
        max=MAX_PASSWORD_LENGTH, message=("Password must be between %(min)d and "
                                          "%(max)d characters long"))])


class PluginForm(ModelForm):
    plugin = StringField('plugin', validators=[DataRequired()])
    schema = TextField('schema', validators=[DataRequired()])
    form = TextField('form', validators=[DataRequired()])
    model = TextField('model', validators=[DataRequired()])
