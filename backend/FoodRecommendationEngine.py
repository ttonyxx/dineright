import json
import requests
import sys
import os
import ast
import time
import datetime
import logging
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.sql import func
from sqlalchemy.pool import NullPool
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message

# utilize the database to store   
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_RECYCLE'] = 299

db = SQLAlchemy(app)

# Create a TfIdfVectorizer object for the TF-IDF vectorization of the cuisine
# descriptions

#Fetch data from The Yelp API using requests.get() to get food data

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(analyzer='word',
                             ngram_range=(1, 3),
                             min_df=0,
                             stop_words='english')

YELP_API_KEY = '0WjD_Q2PVF_szvj8xWxU3O6U4_XU0v2O8j6PwZMgRcR1zf6zdHWmT1TcX-CvbPJiW8nQbDnFm7zvZsxmh8z-6Uq9X4YQ6UQjg8N_fzwH6SVZ_z1xWJdYXnYx'


def get_yelp_data(lat, lon, radius):
    """
    Function to get the Yelp data from the Yelp API.
    """
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'latitude': lat,
              'longitude': lon,
              'radius': radius,
              'limit': 50,
              'categories': 'restaurants',
              'price': '1,2,3,4',
              'sort_by': 'distance'}
    headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
    response = requests.get(url, params=params, headers=headers)
    # print(response.url)
    # print(response.json())
    return response.json()

def get_cuisine_data(lat, lon, radius):
    """
    Function to get the cuisine data from the Yelp API.
    """
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'latitude': lat,
              'longitude': lon,
              'radius': radius,
              'limit': 50,
              'categories': 'restaurants',
              'price': '1,2,3,4',
              'sort_by': 'distance'}
    headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
    response = requests.get(url, params=params, headers=headers)
    # print(response.url)
    # print(response.json())
    return response.json()

"""
Use K-means clustering to group cuisine descriptions into 4 clusters from sklearn


"""
from sklearn.cluster import KMeans
x = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
x.predict(x[0])


