#!/bin/sh

export PYTHONPATH=/Users/smoolaga/Desktop/safe_computing
source venv/bin/activate


pip install -r requirements.txt

echo "Setting Training Data"
python set_training_data.py

echo "Training Chatbot"
python query.py