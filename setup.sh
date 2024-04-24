#!/bin/bash
echo Setting up virtual environment
python3 -m venv venv
source venv/bin/activate

echo Downloading NLP models from HuggingFace Hub
mkdir Models
cd /Models
git clone https://huggingface.co/google/vit-base-patch16-224

cd ..
echo Installing Python libraries
pip install -r requirements.txt