import streamlit as st
import pandas as pd
import pickle
from streamlit_option_menu import option_menu

# Load the cleaned data
data = pd.read_csv('/Users/anithasmac/PycharmProjects/IndustrialCopper/CopperModelling/Copper_data_cleaned.csv')

# Extract unique types for the dropdown
item_types = data['item type'].unique()
status = data['status'].unique()
country = data['country'].unique()
application = data['application'].unique()
product_ref = data['product_ref'].unique()

# Load the models
with open('random_forest_regressor.pkl', 'rb') as file:
    rf_model = pickle.load(file)

with open('extra_trees_model.pkl', 'rb') as file:
    et_model = pickle.load(file)

# Streamlit setup
st.set_page_config(page_title="Copper Modelling", layout="wide")
st.header(':orange[Industrial Copper Modelling]')

with st.sidebar:
    selected = option_menu("Menu", ["Home", "Price Prediction", "Status Prediction"], 
        icons=['house', 'currency-exchange', 'check2-circle'], menu_icon="menu-button"
       )

if selected == "Home":
    st.write(" ")
    st.markdown("### :blue[Tools Used:] Pandas, Data Cleaning, Streamlit, ML Algorithms")
    st.markdown("### :blue[About the Project:] This project provides a streamlined solution for predicting key business metrics. Users can predict the selling price of items and the status of business transactions using trained machine learning models. The application offers an intuitive interface for inputting data and delivers quick, accurate predictions to aid in decision-making.")
    st.markdown("### :blue[Domain:] Manufacturing")
    st.write(" ")
    st.markdown("### Dataset: [Click Here](https://github.com/anithag09/CopperModelling/blob/main/Copper_data_cleaned.csv).")

if selected == "Price Prediction":

    st.write("### Price Prediction App")
    item_date = st.number_input("Item Date", min_value=1900, max_value=2100, value=2023, step=1, key='price_item_date')
    quantity_tons = st.number_input("Quantity (Tons)", min_value=0.0, step=0.1, value=50.0, key='price_quantity_tons')
    country = st.selectbox("Country", options=country, key='price_country')
    item_type = st.selectbox("Item Type", options=item_types, key='price_item_type')
    application = st.selectbox("Application", options=application, key='price_application')
    thickness = st.number_input("Thickness", min_value=0.0, step=0.01, value=0.5, key='price_thickness')
    width = st.number_input("Width", min_value=0, value=120, step=1, key='price_width')
    product_ref = st.selectbox("Product Reference", options=product_ref, key='price_product_ref')
    delivery_date = st.number_input("Delivery Date", min_value=1900, max_value=2100, value=2023, step=1, key='price_delivery_date')

    if delivery_date < item_date:
        st.error("Delivery Date must be greater than or equal to Item Date.")
    else:
        new_data = pd.DataFrame({
            'item_date': [item_date],
            'quantity tons': [quantity_tons],
            'country': [country],
            'item type': [item_type],
            'application': [application],
            'thickness': [thickness],
            'width': [width],
            'product_ref': [product_ref],
            'delivery date': [delivery_date]
            
        })

        if st.button("Predict Selling Price"):
            predicted_price = rf_model.predict(new_data)
            st.success(f"Predicted Selling Price: ${predicted_price[0]:,.2f}")

if selected == "Status Prediction":

    st.write("### Status Prediction App")
    item_date = st.number_input("Item Date", min_value=1900, max_value=2100, value=2023, step=1, key='status_item_date')
    quantity_tons = st.number_input("Quantity (Tons)", min_value=0.0, step=0.1, value=50.0, key='status_quantity_tons')
    country = st.selectbox("Country", options=country, key='status_country')
    item_type = st.selectbox("Item Type", options=item_types, key='status_item_type')
    application = st.selectbox("Application", options=application, key='status_application')
    thickness = st.number_input("Thickness", min_value=0.0, step=0.01, value=0.5, key='status_thickness')
    width = st.number_input("Width", min_value=0, value=120, step=1, key='status_width')
    delivery_date = st.number_input("Delivery Date", min_value=1900, max_value=2100, value=2023, step=1, key='status_delivery_date')
    selling_price = st.number_input("Selling Price", min_value=0.0, step=0.1, value=1000.0, key='status_selling_price')

    if delivery_date < item_date:
        st.error("Delivery Date must be greater than or equal to Item Date.")
    else:
        new_data = pd.DataFrame({
            'item_date': [item_date],
            'quantity tons': [quantity_tons],
            'country': [country],
            'item type': [item_type],
            'application': [application],
            'thickness': [thickness],
            'width': [width],
            'delivery date': [delivery_date],
            'selling_price': [selling_price]
        })

        if st.button("Predict Status"):
            predicted_status = et_model.predict(new_data)
            if predicted_status[0] == 1:
                st.success("Status: Won")
            else:
                st.error("Status: Lost")
