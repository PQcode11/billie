from flask import Flask
from flask import request
from threading import Thread
import time
import requests


app = Flask('')

@app.route('/')
def home():
  return "I'm alive"

def run():
  app.run(host='52.41.36.82' port=80)

def keep_alive():
  t = Thread(target=run)
  t.start()
