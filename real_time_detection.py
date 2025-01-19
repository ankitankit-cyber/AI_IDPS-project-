#real_time_detection.py

from scapy.all import sniff, IP, TCP, UDP
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
from modules.prevention_module import prevent_threat
import warnings
warnings.filterwarnings("ignore")




#Load The traied model
model = joblib.load("C:\\Users\\ankit\\Desktop\\AI_IDPSPRoject\\models\\random_forest_model_smote.pkl")
print("Trained model loaded for real-time detection.")

#Preprocessing function for packet capturing

def preprocess_packet(packet):
    try:
        if IP in packet:
            # Extract more detailed features
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = packet[IP].proto
            length = len(packet)

            # TCP/UDP-specific features
            src_port = packet[TCP].sport if TCP in packet else (packet[UDP].sport if UDP in packet else 0)
            dst_port = packet[TCP].dport if TCP in packet else (packet[UDP].dport if UDP in packet else 0)

            # Flag for TCP (if present)
            flags = int(packet[TCP].flags) if TCP in packet else 0

            # Example: Dummy values for other missing features to make up 42 features
            additional_features = [0] * 36  # Add 36 placeholder features
            dummy_feature = 0

            # Combine all features
            features = [protocol, length, src_port, dst_port, flags] + additional_features + [dummy_feature]

            # Reshape for model input
            return np.array(features).reshape(1, -1), src_ip
        else:
            return None,None
    except Exception as e:
        print(f" Error processing packet: {e}")
        return None,None


#predict and alert function
def predict_packet(packet):
    feature, src_ip = preprocess_packet(packet)
    if feature is not None and src_ip is not None:
        prediction = model.predict(feature)
        if prediction == 1:
            print("alert: Potential malicious Activity Detected from {src_ip}")
        else:
            print("Normal Traffic.")


# Start real-time packet sniffing
def start_sniffing():
    print("🔍 Starting real-time network traffic monitoring...")
    sniff(prn=predict_packet, store=0)

if __name__ == "__main__":
    start_sniffing()

