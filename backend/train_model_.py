import joblib
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from data import generate_training_data

def main():
    print("1. Generating synthetic dataset (1500 samples)...")
    df, all_skills = generate_training_data(1500)
    
    print("2. Engineering features (One-Hot Encoding)...")
    # Convert categorical target_role into separate binary columns
    df = pd.get_dummies(df, columns=["target_role"], dtype=int)
    
    X = df.drop(columns=["fit_score"])
    y = df["fit_score"]

    # Save the exact column order so inference matches training geometry
    feature_columns = list(X.columns)
    joblib.dump(feature_columns, "feature_columns.pkl")
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("3. Training XGBoost Regressor...")
    model = xgb.XGBRegressor(
        n_estimators=150, 
        max_depth=5, 
        learning_rate=0.1, 
        random_state=42
    )
    model.fit(X_train, y_train)
    
    r2_score = model.score(X_test, y_test)
    print(f"4. Evaluation: Model R^2 Score on test set: {r2_score:.3f}")
    
    print("5. Saving model weights to disk...")
    joblib.dump(model, "xgboost_model.pkl")
    print("✅ Training complete. You can now start the server.")

if __name__ == "__main__":
    main()