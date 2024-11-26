from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import ValidationError, DataRequired, Length, InputRequired
import sqlalchemy as sa
from flask_babel import _, lazy_gettext as _l
from app import db
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(
        _l('Username'),
        validators=[DataRequired()],
        render_kw={"id": "username", "placeholder": "Enter your username"}
    )
    about_me = TextAreaField(
        _l('About me'),
        validators=[Length(min=0, max=140)],
        render_kw={"id": "about_me", "placeholder": "Tell us about yourself"}
    )
    submit = SubmitField(
        _l('Submit'),
        render_kw={"id": "submit"}
    )

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = db.session.scalar(sa.select(User).where(
                User.username == username.data))
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class EmptyForm(FlaskForm):
    submit = SubmitField(
        'Submit',
        render_kw={"id": "submit"}
    )


class PostForm(FlaskForm):
    post = TextAreaField(
        _l('Say something'),
        validators=[DataRequired(), Length(min=1, max=140)],
        render_kw={"id": "post", "placeholder": "Write something..."}
    )
    submit = SubmitField(
        _l('Submit'),
        render_kw={"id": "submit"}
    )


class SearchForm(FlaskForm):
    q = StringField(
        _l('Search'),
        validators=[DataRequired()],
        render_kw={"id": "search", "placeholder": "Search..."}
    )

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'meta' not in kwargs:
            kwargs['meta'] = {'csrf': False}
        super(SearchForm, self).__init__(*args, **kwargs)


class MessageForm(FlaskForm):
    message = TextAreaField(
        _l('Message'),
        validators=[DataRequired(), Length(min=1, max=140)],
        render_kw={"id": "message", "placeholder": "Enter your message"}
    )
    submit = SubmitField(
        _l('Submit'),
        render_kw={"id": "submit"}
    )


class UploadFileForm(FlaskForm):
    file = FileField(
        "File",
        validators=[InputRequired()],
        render_kw={"id": "file"}
    )
    submit = SubmitField(
        "Upload File",
        render_kw={"id": "submit"}
    )
