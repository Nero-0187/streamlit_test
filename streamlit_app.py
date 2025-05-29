import streamlit as st
import requests

# Set the app title
st.title('Lessgo, My First StreamLit !!')

# Add a welcome message
st.write('Welcome to my Streamlit app!')

# Create a text input
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')

# Display the customized message
st.write('Customized Message:', widgetuser_input)

# Fetch exchange rates with MYR as the base currency
response = requests.get('https://api.vatcomply.com/rates?base=MYR')

if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})
    
    # Sort and create a list of currency codes
    currency_options = sorted(rates.keys())

    # Dropdown for user to select target currency
    selected_currency = st.selectbox('Select a currency to view the exchange rate from MYR:', currency_options)

    # Show the selected currency exchange rate
    if selected_currency:
        st.write(f"💱 1 MYR = {rates[selected_currency]} {selected_currency}")

    # Optionally show all data
    with st.expander("See all exchange rates"):
        st.json(data)
else:
    st.error(f"API call failed with status code: {response.status_code}")



