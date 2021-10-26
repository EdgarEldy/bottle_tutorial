"""
Routes and views for the bottle application.
"""

from bottle import route, view

@route('/')
@view('home/index')
def home_index():
    """Renders the home page."""