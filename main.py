import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.set_page_config(layout="wide")

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.sidebar.link_button('Go to GitHub', 'https://github.com/')

st.title('Mortgage Repayment Calculator', help='This app calculates the monthly mortgage repayment based on the home price, down payment, loan term, and interest rate.')

st.subheader('Enter the following details to calculate your monthly mortgage repayment')
col1, col2 = st.columns(2)
home_price = col1.number_input('Home Price', value=500000, min_value=0)
down_payment = col1.number_input('Down Payment', value=100000, min_value=0)
loan_term = col2.number_input('Loan Term (years)', value=30,min_value=0)
interest_rate = col2.number_input('Interest Rate (%)', value=3.0,min_value=0.0)

# Repayment Calculation
loan_amount = home_price - down_payment
monthly_interest_rate = (interest_rate / 100) / 12
num_payments = loan_term * 12
monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / ((1 + monthly_interest_rate) ** num_payments - 1)

st.divider()

# Display the monthly repayment
total_payment = monthly_payment * num_payments
total_interest = total_payment - loan_amount

st.subheader('Repayment Details:')
col1,col2, col3 = st.columns(3)
col1.metric('Monthly Payment', f"RM{monthly_payment:,.2f}")
col2.metric('Total Payment', f"RM{total_payment:,.2f}")
col3.metric('Total Interest', f"RM{total_interest:,.2f}")

st.divider()

# Amortization Schedule
st.subheader('Amortization Schedule:')
schedule = []
balance = loan_amount

for i in range(num_payments + 1):
    month = i + 1
    interest = balance * monthly_interest_rate
    principal = monthly_payment - interest
    balance = balance - principal
    year = math.ceil((i+1)/12)
    schedule.append([month, monthly_payment, interest, principal, balance, math.ceil((i+1)/12)])

df = pd.DataFrame(schedule, columns=['Month', 'Monthly Payment (RM)', 'Interest (RM)', 'Principal (RM)', 'Balance (RM)', 'Year'])
st.write(df)

# Plot the amortization schedule
st.write('### Amortization Schedule Chart')
interest_principle_df = df[['Interest (RM)', 'Principal (RM)']]
st.line_chart(interest_principle_df)

st.divider()

# Plot the yearly balance
st.write('### Yearly Balance Chart')
yearly_payment_df = df[['Year', 'Balance (RM)']].groupby('Year').min()
st.line_chart(yearly_payment_df)

st.divider()

# Plot the monthly balance
st.write('### Monthly Balance Chart')
monthly_payment_df = df[['Month', 'Balance (RM)']].groupby('Month').min()
st.line_chart(monthly_payment_df)
