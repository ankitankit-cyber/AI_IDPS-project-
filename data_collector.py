# lets import the data

import pandas as pd
import  os


def load_dataset(file_path):
    # loading csv data file using pandas

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at {file_path}")
    data = pd.read_csv(file_path)
    print(f"Dataset loaded successfully with {data.shape[0]} row and {data.shape[1]} columns.")
    return data


def explore_dataset(data):
    """
    So here Display basic information about
    dataset
    """

    print("\nData Overview:\n")
    print(data.head()) # Display the first five rows

    print("\nDataset Info:\n")
    print(data.info()) # Display column data types and non-null counts

    print("\nMissing Values per column:\n")
    print(data.isnull().sum())



if __name__ == "__main__":
    train_dataset_path = "C:\\Users\\ankit\\Desktop\\AI_IDPSPRoject\\load_data\\KDDTrainPlus.txt"
    test_dataset_path = "C:\\Users\\ankit\\Desktop\\AI_IDPSPRoject\\load_data\\KDDTest+.txt"
    dataset = load_dataset(train_dataset_path)
    explore_dataset(dataset)

    dataset = load_dataset(test_dataset_path)
    explore_dataset(dataset)