import streamlit as st
import requests

# Set the app title
st.title('💱 Currency Converter - Lessgo, StreamLit!')

# Welcome message
st.write('Convert between currencies using real-time exchange rates.')

# Fetch list of currencies
response = requests.get('https://api.vatcomply.com/rates')

if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})
    currency_list = sorted(rates.keys())
    currency_list.insert(0, data['base'])  # ensure base currency is included

    # Dropdowns for base and target currencies
    base_currency = st.selectbox('Select base currency:', currency_list, index=currency_list.index('MYR'))
    target_currency = st.selectbox('Select target currency:', currency_list, index=currency_list.index('USD'))

    # User input for amount
    amount = st.number_input(f'Enter amount in {base_currency}:', min_value=0.0, value=1.0)

    # Make API call with selected base currency
    conversion_response = requests.get(f'https://api.vatcomply.com/rates?base={base_currency}')
    if conversion_response.status_code == 200:
        conversion_data = conversion_response.json()
        rate = conversion_data['rates'].get(target_currency)

        if rate:
            converted = amount * rate
            st.success(f'💰 {amount:.2f} {base_currency} = {converted:.2f} {target_currency}')
        else:
            st.error(f'Rate for {target_currency} not found.')
    else:
        st.error('Failed to fetch conversion rate.')

    # Optionally show all rates
    with st.expander("See full rate table"):
        st.json(conversion_data)

else:
    st.error('Failed to load currency data from API.')




