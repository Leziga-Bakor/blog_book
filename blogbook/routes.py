import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from blogbook import app, db, bcrypt, mail
from blogbook.forms import (RegistrationForm, LoginForm, UpdateAccountForm, 
                            PostForm, RequestResetForm, ResetPasswordForm)
from blogbook.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message




