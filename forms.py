# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Optional, URL, EqualTo


class ProfileForm(FlaskForm):
    nickname = StringField('昵称', validators=[DataRequired(), Length(1, 64)])
    github = StringField('GitHub', validators=[Optional(), URL(), Length(0, 128)])
    website = StringField('网站', validators=[Optional(), URL(), Length(0, 128)])
    bio = TextAreaField('简介', validators=[Optional(), Length(0, 120)])


class LoginForm(FlaskForm):
    email = StringField('电子邮件', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember = BooleanField('记住我')
    submit = SubmitField('登录')


class RegisterForm(FlaskForm):
    nickname = StringField('昵称', validators=[DataRequired(), Length(1, 64)])
    email = StringField('电子邮件', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(min=6), EqualTo('password2')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('加入')
