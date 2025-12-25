# COVID-19 Prediction Dashboard

A machine learning-based COVID-19 prediction system using 6 different algorithms with an interactive web dashboard.

## 🎯 Features

- **6 ML Algorithms**: Linear Regression, Polynomial Regression, Multiple Regression, Naive Bayes, KNN, and K-Means
- **Interactive Dashboard**: Professional web interface with real-time predictions
- **Model Comparison**: Visual comparison of all algorithms
- **Best Algorithm Identification**: Automatically highlights the best performing model
- **Feature Importance**: Shows which symptoms contribute most to predictions
- **Sample Presets**: Pre-loaded symptom profiles for testing

## 📊 Algorithm Performance

| Algorithm | Accuracy | Precision | Recall | F1-Score |
|-----------|----------|-----------|--------|----------|
| Linear Regression | 97.67% | 97.56% | 100% | 98.77% |
| Polynomial Regression | 97.67% | 97.56% | 100% | 98.77% |
| Multiple Regression | 97.67% | 97.56% | 100% | 98.77% |
| Naive Bayes | 90.70% | 95.00% | 95% | 95.00% |
| KNN | 97.67% | 97.56% | 100% | 98.77% |
| K-Means | 95.35% | 97.50% | 97.5% | 97.50% |

🏆 **Best Algorithm**: Linear Regression (97.67% accuracy)

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/SumadhuraM/Covid_prediction/tree/master
cd covid-prediction-project

# Install dependencies
pip install -r requirements.txt
```

### 2. Running the Application

#### Option 1: Using the Runner Script (Recommended)
```bash
python run.py
```

#### Option 2: Direct Flask Run
```bash
python -m app.app
```

The application will start on `http://localhost:5000`

### 3. Access the Dashboard

Open your browser and navigate to: `http://localhost:5000`

## 📖 Usage

### Web Dashboard
1. **Select Symptoms**: Check the symptoms that apply to the patient
2. **Choose Algorithm**: Select from 6 available ML algorithms or use the best performing one
3. **Run Prediction**: Click "Run AI Diagnosis" to get prediction results
4. **Compare Models**: Use "Compare All" to see how all algorithms perform

### API Usage

#### Get Model Information
```bash
GET /api/models
```

#### Make Prediction
```bash
POST /api/predict
Content-Type: application/json

{
  "algorithm": "Linear Regression",
  "symptoms": [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
```

#### Compare All Algorithms
```bash
POST /api/compare
Content-Type: application/json

{
  "symptoms": [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
```

#### Health Check
```bash
GET /api/health
```

## 📁 Project Structure

```
covid-prediction-project/
├── app/
│   ├── __init__.py
│   ├── app.py              # Main Flask application
│   ├── models.py           # ML model loading and prediction logic
│   ├── utils.py            # Utility functions
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css   # Dashboard styling
│   │   ├── js/
│   │   │   └── dashboard.js # Frontend JavaScript
│   │   └── img/
│   │       └── favicon.ico
│   └── templates/
│       └── dashboard.html  # Main dashboard template
├── config.py               # Configuration settings
├── run.py                  # Application runner
├── requirements.txt        # Python dependencies
├── Covid Dataset.csv       # Training dataset
├── covid_prediction_training.ipynb # Training notebook
└── README.md
```

## 🔧 Configuration

Edit `config.py` to customize:
- Database paths
- Model file locations
- Server settings
- Feature configurations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This system is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult healthcare professionals for medical decisions.



