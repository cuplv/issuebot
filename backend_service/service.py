from flask import Flask, request, Response, render_template, current_app
import json
import optparse
import logging
import os
import sys

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)