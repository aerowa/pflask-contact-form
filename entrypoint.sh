#!/bin/bash

# Start Postfix
postfix start

# Start the Flask app
python app.py
