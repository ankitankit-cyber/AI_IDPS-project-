# AI_IDPS-project-

# AI-Powered Intrusion Detection and Prevention System (IDPS)

## Project Overview
This project is an **AI-Powered Intrusion Detection and Prevention System (IDPS)** designed to detect and prevent malicious activities in real-time. The system utilizes machine learning to analyze network traffic and block potential threats effectively. The project focuses on ensuring network security by providing a reliable and automated solution.

## Key Features
- **Real-Time Intrusion Detection**: Uses a trained machine learning model to detect intrusions by analyzing network traffic data.
- **Automated Threat Prevention**: Automatically blocks malicious IP addresses or activities upon detection.
- **Class Imbalance Handling**: Implements SMOTE (Synthetic Minority Oversampling Technique) to manage class imbalance in training data for improved model performance.
- **Extensive Logging**: Logs all detected threats and actions for auditing and analysis.
- **Modular Design**: Organized into separate modules for preprocessing, detection, prevention, and logging, ensuring scalability and maintainability.

## Project Structure
The project is organized into the following structure:

```
AI-IDPS/
├── modules/
|   |__ data_collector.py        # Data collection file
│   ├── detection_engine.py        # Logic for intrusion detection using ML
│   ├── prevention_module.py       # Handles threat prevention mechanisms
│   ├── feature_extractor.py    # Data preprocessing and feature extraction
│   └── real_time_detection.py           # Logs threats and actions
├── load_data/
│   ├── training_data.csv   # Training dataset for ML model
│   ├── test_data.csv       # Testing dataset
│__ logs/
|   |__ detected_threats.log # All the detected information
├── models/
│   └── trained_model.pkl   # Trained ML model file
├── main.py                 # Entry point of the application
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## How It Works
1. **Data Preprocessing**:
   - Raw network traffic data is cleaned and processed.
   - Relevant features are extracted for analysis.
   - SMOTE is applied to handle class imbalance in training datasets.

2. **Intrusion Detection**:
   - The machine learning model analyzes preprocessed data to detect anomalies or known threats.

3. **Threat Prevention**:
   - Automatically blocks IP addresses or actions identified as malicious.

4. **Logging**:
   - All detected threats and preventive actions are logged for auditing and debugging purposes.

## Prerequisites
- **Python**: Version 3.8 or higher
- Required Python libraries:
  - scikit-learn
  - pandas
  - numpy
  - smote-tomek
  - joblib

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-idps.git
   cd ai-idps
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage
### Training the Model
- Use the `training_data.csv` file in the `load_data/` directory to train a machine learning model.
- Modify the `main.py` script to retrain the model if needed.

### Real-Time Detection
- The system monitors network traffic and identifies potential threats in real-time.
- Logs are generated in the `logs/detected_threats.log` file.

### Threat Prevention
- Malicious IPs or actions are blocked automatically based on detection results.

## Future Enhancements
- Integration with more advanced threat detection algorithms.
- Improved scalability to support larger network environments.
- Dynamic model retraining for better adaptability.

## Please note that my trianing model file in large size that cross the limit of github so i can't upload them but i upload all other  files 

