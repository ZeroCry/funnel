import sys
import os.path
sys.path.insert(0, os.path.dirname(__file__))
from funnel import app, init_for

def application(environ, start_response):
    environ['SCRIPT_NAME'] = '/funnel/'
    return app(environ, start_response)

init_for('production')
