#importing all the dependencies

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib


# Train the model

def train_model(x_train,y_train):
    model = RandomForestClassifier(n_estimators=100,random_state=42)
    model.fit(x_train,y_train)
    print("Model Training complete.")
    return model


# Evaluate the model or checking accuracy score

def  evaluate_model(model, x_test,y_test):
    prediction = model.predict(x_test)

    print("\nModel Evaluation:")
    print("confusion Matrix:\n", confusion_matrix(y_test,prediction))
    print("\nclassification Report:\n", classification_report (y_test, prediction))
    print("Accuracy:", accuracy_score(y_test, prediction))


# Saving train model

def save_model(model,filename="C:\\Users\\ankit\\Desktop\\AI_IDPSPRoject\\models\\random_forest_model_smote.pkl"):

    joblib.dump(model,filename)
    print(f"Model saved to {filename}")





if __name__=="__main__":
    from feature_extractor import preprocess_data
    import pandas as pd

    datset_path = "C:\\Users\\ankit\\Desktop\\AI_IDPSPRoject\\load_data\\KDDTrainPlus.txt"
    data = pd.read_csv(datset_path)

    x_train,x_test,y_train,y_test = preprocess_data(data)

    #Train the model
    model = train_model(x_train,y_train)

    #Evaluate the model
    evaluate_model(model,x_test,y_test)
    #Save the model
    save_model(model)