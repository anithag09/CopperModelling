# Industrial Copper Modelling

This project provides a web-based application for predicting the selling price of items and the status of business transactions using machine learning models. The application is built using [Streamlit](https://streamlit.io/) and allows users to input relevant data through an intuitive interface.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Models](#models)

## Features

- **Selling Price Prediction**: Predict the selling price of items based on features such as quantity, customer, country, application, thickness, width, and product reference using a Random Forest Regressor model.
- **Status Prediction**: Predict the status of business transactions (e.g., Won or Lost) using an Extra Trees Classifier model.
- **User-Friendly Interface**: Simple and easy-to-use interface built with Streamlit.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/anithag09/CopperModelling.git
    ```

2. **Install the Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit App**:
    ```bash
    streamlit run CopperModelling.py
    ```

## Usage

After running the Streamlit app, you can:

1. Access the app through your web browser.
2. Navigate through the sidebar menu to choose between "Price Prediction" and "Status Prediction".
3. Enter the required input data in the provided fields.
4. Click on the "Predict" button to get the results.

## Data

The data used for training the models can be accessed [here](https://www.example.com/dataset). Ensure that your input data is encoded and structured similarly to how the models were trained.

## Models

- **Random Forest Regressor**: Used for predicting the selling price based on input features.
- **Extra Trees Classifier**: Used for predicting the status of a transaction (Won or Lost).

Both models are saved as pickle files and are loaded within the Streamlit application for making predictions.

