from flask import render_template
from app import website

@website.route('/')
def index():
  return render_template('index.html')

@website.route('/featured1.html')
def featuredOne():
  return render_template('featured1.html')
