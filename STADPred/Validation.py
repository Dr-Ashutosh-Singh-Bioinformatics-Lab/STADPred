# STAD/Validation.py

import os
import pandas as pd
import joblib

def predict(df, model_type='svc'):
    # List of selected genes
    selected_genes = ['IBSP', 'HOXC8', 'ATP11A', 'FAP', 'ANGPT2', 'MMP11', 'CST4', 'RIPK2', 'DNAJC2', 'WNT2',  'E2F3', 'MTHFD1L', 'INHBA', 'HOXC11', 'COL10A1', 'COLGALT1', 'DKC1', 'DHX34', 'BAAT',  'SEPTIN11', 'ADAMTS18', 'SERPINH1', 'ADAMTS12', 'ATAD2', 'ZNF281', 'CLEC3B', 'ESM1',  'PGM2L1', 'CST1', 'TGIF1', 'FOXS1', 'HOXC9', 'HOXC10', 'BGN', 'RAD51D', 'GABRD', 'SLC39A10',  'TEAD4', 'TIGD1', 'TUBB3']
   # Select features from dataframe
    df_selected = df[selected_genes]
    
    # Construct model path
    model_path = os.path.join(os.path.dirname(__file__), 'models', f'{model_type.lower()}.pkl')
    
    # Check if model file exists
    if not os.path.exists(model_path):
        raise ValueError(f"Model '{model_type}' not found. Ensure the model file exists at {model_path}.")
    
    # Load the model
    model = joblib.load(model_path)
    
    # Make predictions
    y_pred = model.predict(df_selected)
    
    # Add predictions to dataframe
    df['Prediction'] = ['Cancer' if pred == 1 else 'Normal' for pred in y_pred]
    
    # Save predictions to CSV file
    df.to_csv('predictions.csv', index=False)
    
    # Print diagnosis
    count_cancer = y_pred.sum()
    count_normal = len(y_pred) - count_cancer
    percentage_cancer = count_cancer / len(y_pred)
    percentage_normal = count_normal / len(y_pred)
    
    if percentage_cancer > 0.6:
        print(f"STAD patient detected, {percentage_cancer*100:.2f}%")
    else:
        print(f"Normal patient detected, {percentage_normal*100:.2f}%")

