from flask import Flask, render_template
from data.jobs_data_client import JobInfoClient

app = Flask('project')
jobs_db = JobInfoClient()

from project.controllers import *

# Sample HTTP error handling
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404
