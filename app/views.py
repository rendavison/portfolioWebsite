from flask import render_template
from app import website

#Main webpages

@website.route('/')
def index():
  return render_template('index.html')

@website.route('/design')
def design():
  return render_template('design.html')

@website.route('/web')
def web():
  return render_template('web.html')

@website.route('/about')
def about():
  return render_template('about.html')

@website.route('/photography')
def photography():
  return render_template('photo_slider.html')

#Project subpages

@website.route('/sns')
def sns():
  return render_template('sns.html')

@website.route('/101claras')
def hundredClaras():
  return render_template('101claras.html')

@website.route('/ideate')
def ideate():
  return render_template('ideate.html')

@website.route('/drueheinz')
def drueHeinz():
  return render_template('drueheinz.html')

@website.route('/cmoa')
def cmoa():
  return render_template('cmoa.html')

@website.route('/helvetica')
def helvetica():
  return render_template('helvetica.html')

@website.route('/rzd')
def rzd():
  return render_template('rzd.html')

@website.route('/compliment')
def compliment():
  return render_template('compliment.html')

@website.route('/cherry')
def cherryBlossoms():
  return render_template('cherry.html')

@website.route('/bubblegum')
def bubblegumPop():
  return render_template('bubblegum.html')

@website.route('/hayakawa')
def hayakawa():
  return render_template('hayakawa.html')

@website.route('/hayakawa-web')
def hayakawaWeb():
  return render_template('hayakawa_web.html')

@website.route('/hayakawa-preview')
def hayakawaPreview():
  return render_template('hayakawa_web/index.html')

@website.route('/pgh-web')
def pghWeb():
  return render_template('pgh_web.html')

@website.route('/404')
def uc():
  return render_template('uc.html')