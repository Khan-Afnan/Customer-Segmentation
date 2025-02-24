import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained K-Means model
kmeans = joblib.load("customer_segmentation_model.pkl")

# Define cluster labels with icons for better visualization
cluster_labels = {
    0: "🛍️ Loyal Customers",
    1: "🏆 Champions",
    2: "⚠️ At Risk Customers",
    3: "🆕 New Customers"
}

# Streamlit UI
st.title("📊 Customer Segmentation Prediction")
st.write("🔢 Enter RFM Scores to Predict Customer Segment")

# Display Customer Segmentation Image
st.image("customer.webp", caption="🧐 Customer Segmentation Categories", use_column_width=True)

# User Input Fields with Icons
st.subheader("📝 Enter RFM Scores:")
recency_score = st.number_input("📅 Recency Score (1-5)", min_value=1, max_value=5, step=1)
frequency_score = st.number_input("🔄 Frequency Score (1-5)", min_value=1, max_value=5, step=1)
monetary_score = st.number_input("💰 Monetary Score (1-5)", min_value=1, max_value=5, step=1)

# Prediction Button
if st.button("🚀 Predict Customer Segment"):
    # Convert input to DataFrame
    input_data = np.array([[recency_score, frequency_score, monetary_score]])
    
    # Predict cluster
    predicted_cluster = kmeans.predict(input_data)[0]
    
    # Get cluster label
    customer_segment = cluster_labels.get(predicted_cluster, "❓ Unknown Segment")
    
    # Display result
    st.success(f"✅ Predicted Customer Segment: {customer_segment}")
