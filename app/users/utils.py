import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from app import mail

#Function to save user uploaded picture
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)                       #8-bit random filenames for the images
    _, f_ext = os.path.splitext(form_picture.filename)      #filename not used to _ used to discard that variable and minimize errors
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path,'static/profile_pics',picture_fn)
    #app.root_path (full path to the package directory), joined with static/profile_pics folder
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)    #reduced image
    i.save(picture_path) # saved to the picture_path
    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='puskarrim@gmail.com', recipients=[user.email])
    msg.body = f''' To reset your password, please visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''                                                             #_external=True used to get an absolute url rather than a relative url
    mail.send(msg)
