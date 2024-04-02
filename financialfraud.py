import numpy as np
import streamlit as st
import joblib

# Load the saved model
model = joblib.load('my_fraud_detection_model.sav')

# Function to make predictions
def predict_fraud(transaction_data):
    # Convert user input to a NumPy array
    data_array = np.array([
        transaction_data["Time"], transaction_data["V1"], transaction_data["V2"],
        transaction_data["V3"], transaction_data["V4"], transaction_data["V5"],
        transaction_data["V6"], transaction_data["V7"], transaction_data["V8"],
        transaction_data["V9"], transaction_data["V10"], transaction_data["V11"],
        transaction_data["V12"], transaction_data["V13"], transaction_data["V14"],
        transaction_data["V15"], transaction_data["V16"], transaction_data["V17"],
        transaction_data["V18"], transaction_data["V19"], transaction_data["V20"],
        transaction_data["V21"], transaction_data["V22"], transaction_data["V23"], transaction_data["V24"],
        transaction_data["V25"], transaction_data["V26"], transaction_data["V27"],
        transaction_data["V28"], transaction_data["amount"]
    ])

    # Make prediction using the model
    prediction = model.predict(data_array.reshape(1, -1))  # Reshape for single prediction
    return prediction[0]  # Return the first element (predicted probability or class)

# Streamlit app
def main():
    # Set page title and favicon
    st.set_page_config(page_title="Financial Fraud Detection", page_icon=":money_with_wings:")

    # Money-themed background image URL
    money_background_url = "https://wallpapercave.com/wp/wp2300486.jpg"

    # Business-like styling using Markdown and HTML
    st.markdown(
        f"""
        <style>
        body {{
            background-image: url("{money_background_url}");
            background-size: cover;
            background-repeat: no-repeat;
            color: #333;
        }}
        .sidebar .sidebar-content {{
            background: #1e90ff;
            color: #fff;
        }}
        .Widget>label {{
            color: #333;
            font-weight: bold;
        }}
        .stButton>button {{
            color: #fff;
            background-color: #007bff;
        }}
        .stButton>button:hover {{
            background-color: #0056b3;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Financial Fraud Detection")

    # Input fields for transaction data
    time = st.sidebar.number_input("Time:")
    v1 = st.sidebar.number_input("V1:")
    v2 = st.sidebar.number_input("V2:")
    v3 = st.sidebar.number_input("V3:")
    v4 = st.sidebar.number_input("V4:")
    v5 = st.sidebar.number_input("V5:")
    v6 = st.sidebar.number_input("V6:")
    v7 = st.sidebar.number_input("V7:")
    v8 = st.sidebar.number_input("V8:")
    v9 = st.sidebar.number_input("V9:")
    v10 = st.sidebar.number_input("V10:")
    v11 = st.sidebar.number_input("V11:")
    v12 = st.sidebar.number_input("V12:")
    v13 = st.sidebar.number_input("V13:")
    v14 = st.sidebar.number_input("V14:")
    v15 = st.sidebar.number_input("V15:")
    v16 = st.sidebar.number_input("V16:")
    v17 = st.sidebar.number_input("V17:")
    v18 = st.sidebar.number_input("V18:")
    v19 = st.sidebar.number_input("V19:")
    v20 = st.sidebar.number_input("V20:")
    v21 = st.sidebar.number_input("V21:")
    v22 = st.sidebar.number_input("V22:")
    v23 = st.sidebar.number_input("V23:")
    v24 = st.sidebar.number_input("V24:")
    v25 = st.sidebar.number_input("V25:")
    v26 = st.sidebar.number_input("V26:")
    v27 = st.sidebar.number_input("V27:")
    v28 = st.sidebar.number_input("V28:")
    amount = st.sidebar.number_input("Amount ($):")

    # Button to trigger prediction
    if st.sidebar.button("Predict Fraud Risk"):
        # Combine user input into a dictionary
        transaction_data = {
            "Time": time, "V1": v1, "V2": v2, "V3": v3, "V4": v4, "V5": v5,
            "V6": v6, "V7": v7, "V8": v8, "V9": v9, "V10": v10, "V11": v11, "V12": v12,
            "V13": v13, "V14": v14, "V15": v15, "V16": v16, "V17": v17,
            "V18": v18, "V19": v19, "V20": v20, "V21": v21, "V22": v22, "V23": v23, "V24": v24,
            "V25": v25, "V26": v26, "V27": v27, "V28": v28, "amount": amount}

        # Make prediction
        prediction = predict_fraud(transaction_data)

        # Display prediction
        if prediction == 1:
            st.write("Warning: Potential Fraudulent Transaction Detected!")
        else:
            st.write("No Fraud Detected")

    # Dropdown field to choose between displaying input fields and contact information
    display_option = st.selectbox("Choose display option", ["Transaction Data", "Contact Information"])

    # Display transaction data or contact information based on the selected option
    if display_option == "Transaction Data":
        st.write("Please enter transaction data above.")
    elif display_option == "Contact Information":
        st.markdown(
            """
            ## Contact Information

            **Name:** Sammy Ngure  
            **Email:** sngure807@gmail.com  
            **Phone:** +254 7 23 77 5 071

            Feel free to reach out for any inquiries or support!
            """
        )

# Run the Streamlit app
if __name__ == "__main__":
    main()
