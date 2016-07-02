from flask import render_template
from app import website

@website.route('/')
def index():
  return render_template('index.html')
