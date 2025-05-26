"""
__init__.py

Initializes Flask applciation and adds all routes

Author: Heath Dyer
Created: 2025-05-22
"""

from flask import Flask

app = Flask(__name__)

from app import views

from app import api