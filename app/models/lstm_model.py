import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import os
from ..config import BASE_DIR

MODELS_DIR = os.path.join(BASE_DIR, 'data', 'models')
os.makedirs(MODELS_DIR, exist_ok=True)

def create_model(input_shape):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(50, return_sequences=False),
        Dropout(0.2),
        Dense(25),
        Dense(1)
    ])
    
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_lstm_model(symbol, df):
    # Prepare data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df['close'].values.reshape(-1, 1))
    
    # Create training data
    x_train = []
    y_train = []
    
    for i in range(60, len(scaled_data)):
        x_train.append(scaled_data[i-60:i, 0])
        y_train.append(scaled_data[i, 0])
    
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    
    # Create and train model
    model = create_model((x_train.shape[1], 1))
    model.fit(x_train, y_train, batch_size=32, epochs=10)
    
    # Save model
    model_path = os.path.join(MODELS_DIR, f'{symbol}_lstm.h5')
    model.save(model_path)
    
    return model

def load_model(symbol):
    model_path = os.path.join(MODELS_DIR, f'{symbol}_lstm.h5')
    if os.path.exists(model_path):
        return load_model(model_path)
    return None

def make_prediction(model, df, days=7):
    # Prepare data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df['close'].values.reshape(-1, 1))
    
    # Use last 60 days for prediction
    last_60_days = scaled_data[-60:]
    
    predictions = []
    for _ in range(days):
        x_input = np.array([last_60_days])
        x_input = np.reshape(x_input, (x_input.shape[0], x_input.shape[1], 1))
        
        pred = model.predict(x_input)
        predictions.append(pred[0][0])
        
        # Update last_60_days with the new prediction
        last_60_days = np.append(last_60_days[1:], pred)
    
    # Inverse transform predictions
    predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
    
    return [float(p[0]) for p in predictions]