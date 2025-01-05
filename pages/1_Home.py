import streamlit as st

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

st.title('Home')
st.subheader('Welcome to the Mortgage Repayment Calculator!')

st.write('This app calculates the monthly mortgage repayment based on the home price, down payment, loan term, and interest rate.')

st.select_slider('Select a number', options=[1,2,3,4,5])
st.slider('Select a number', min_value=1, max_value=5)

st.segmented_control('Select a number', options=[1,2,3,4,5])
st.radio('Select a number', options=[1,2,3,4,5])

st.text_input('Enter your name')
st.number_input('Enter a number')
st.text_area('Enter a text')
st.date_input('Enter a date')
st.time_input('Enter a time')

st.checkbox('Check me out')
st.selectbox('Select a number', options=[1,2,3,4,5])