import streamlit as st

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")

st.title('Profile')
st.subheader('Welcome to your Profile Page!')

st.write('This is your profile page. You can view and edit your profile details here.')

st.color_picker('Pick a color', '#00f900')
ballon_button = st.button('Click me')
if ballon_button:
    st.balloons()
st.error('This is an error message')
st.success('This is a success message')

st.slider('Select a number', 0.0, 100.0, (25.0, 75.0))