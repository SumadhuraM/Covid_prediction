"""
Configuration settings for COVID Prediction Dashboard
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.absolute()

# Application settings
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'covid-prediction-secret-key-2024'
    DEBUG = os.environ.get('DEBUG', 'True') == 'True'
    
    # File paths
    MODEL_PATH = os.path.join(BASE_DIR, 'data', 'covid_all_models.pkl')
    DATASET_PATH = os.path.join(BASE_DIR, 'data', 'covid_dataset.csv')
    
    # Static files
    STATIC_FOLDER = os.path.join(BASE_DIR, 'app', 'static')
    TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'app', 'templates')
    
    # Server settings
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5000))
    
    # Features
    ENABLE_COMPARISON = True
    ENABLE_FEATURE_IMPORTANCE = True
    MAX_SYMPTOMS = 18
    
    # Sample data (if models not available)
    DEMO_DATA = {
        'models': ['Linear Regression', 'Polynomial Regression', 'Multiple Regression', 
                  'Naive Bayes', 'KNN', 'K-Means'],
        'results': {
            'Linear Regression': {'Accuracy': 0.9767, 'Precision': 0.9756, 'Recall': 1.0000, 'F1-Score': 0.9877},
            'Polynomial Regression': {'Accuracy': 0.9767, 'Precision': 0.9756, 'Recall': 1.0000, 'F1-Score': 0.9877},
            'Multiple Regression': {'Accuracy': 0.9767, 'Precision': 0.9756, 'Recall': 1.0000, 'F1-Score': 0.9877},
            'Naive Bayes': {'Accuracy': 0.9070, 'Precision': 0.9500, 'Recall': 0.9500, 'F1-Score': 0.9500},
            'KNN': {'Accuracy': 0.9767, 'Precision': 0.9756, 'Recall': 1.0000, 'F1-Score': 0.9877},
            'K-Means': {'Accuracy': 0.9535, 'Precision': 0.9750, 'Recall': 0.9750, 'F1-Score': 0.9750}
        },
        'best_model': 'Linear Regression'
    }