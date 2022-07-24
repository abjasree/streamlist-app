import streamlit as st


st.write("""
# Find the largest Number
This app gives the largest number of three numbers given by the user
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
   
    number_1 = st.number_input("First Number",min_value=0.0,max_value=20000.0)
    number_2 = st.number_input("Second Number",min_value=0.0,max_value=20000.0)
    number_3 = st.number_input("Third Number", min_value=0.0,max_value=20000.0)
    data = {'number_1':number_1, 'number_2':number_2, 'number_3':number_3}
    return data

d = user_input_features()
st.subheader('Largest Number')
if d['number_1'] > d['number_2'] and d['number_1'] > d['number_3']:
    st.write(d['number_1'])
elif d['number_2'] > d['number_3']:
    st.write(d['number_2'])
else:
    st.write(d['number_3'])
