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
  return render_template('photography.html')

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

@website.route('/mosaic')
def mosaic():
  return render_template('mosaic.html')

@website.route('/turtle')
def turtle():
  return render_template('turtle.html')

@website.route('/cmoa')
def cmoa():
  return render_template('cmoa.html')

@website.route('/helvetica')
def helvetica():
  return render_template('helvetica.html')

@website.route('/lamp')
def lamp():
  return render_template('lamp.html')

@website.route('/cardboard')
def cardboard():
  return render_template('cardboard.html')

@website.route('/cherry')
def cherryBlossoms():
  return render_template('cherry.html')

@website.route('/bubblegum')
def bubblegumPop():
  return render_template('bubblegum.html')
