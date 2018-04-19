"""
Flask settings file.

For the full list of settings and their values, visit
http://flask.pocoo.org/docs/0.12/config/
"""

import os

DEBUG = True if os.environ.get('FLASK_DEBUG') in ['1', 'True', 'true'] else False

SECRET_KEY = 'Sr[I(S7haMZcDZl%DWHJF]bRN:Gm+m9]H.zxbRG%ESd<~5G]^Z'
