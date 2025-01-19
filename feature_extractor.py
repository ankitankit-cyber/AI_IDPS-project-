# this Script is all about data feature extraction

import pandas  as pd
from sklearn.preprocessing import  LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
def preprocess_data(data):
    """
    Preprocessing data: handles missing values, encode categorical data.
    scaler numerical feature, and splits into training/testing sets.
    """

    # 1. Handle Missing Values
    data = data.dropna()

    #2. Ecncode Categorical Columns

    label_encoder = LabelEncoder()
    for column in data.columns:
        if data[column].dtype == 'object':
            data[column] = label_encoder.fit_transform(data[column])


    #3. Split Feature  and Target

    x = data.iloc[:,:-1] # All column except the last one
    y = data.iloc[:,-1] # Last  column as target

    #4. Scale feature to 0-1 Range
    scaler = MinMaxScaler()
    x_scaled =scaler.fit_transform(x)



    #5. Split Data into Training and Testing Sets

    x_train, x_test, y_train, y_test = train_test_split(x_scaled,y, test_size=0.3,random_state=42)

    #Now lets apply Smote
    smote = SMOTE(random_state=42)
    x_train_resampled, y_train_resampled = smote.fit_resample(x_train,y_train)
    print("SMOTE  applied  to balance the training set")
    print(f"Training Set Shape:{x_train_resampled.shape}")
    print(f"Testing Set Shape:{x_test.shape}")

    return x_train_resampled, x_test, y_train_resampled, y_test

if __name__ == "__main__":

    dataset_path = "C:\\Users\\ankit\\Desktop\\AI_IDPSPRoject\\load_data\\KDDTrainPlus.txt"
    data = pd.read_csv(dataset_path)
    x_train, x_test, y_train, y_test = preprocess_data(data)

