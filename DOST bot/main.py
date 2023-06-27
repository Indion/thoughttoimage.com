from flask import Flask,jsonify
from config import key
from flask import render_template
import openai
import os
openai.api_key=key 
app=Flask(__name__)
@app.route('/')
def index ():
    return render_template("index.html")
@app.route('/generateimages/<prompt>')
def generate(prompt):
    response=openai.Image.create(
    prompt = prompt,
    n=2,
    size="512x512"
    
)
    return jsonify(response)
app.run(host="0.0.0.0",port=81)
