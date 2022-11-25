import streamlit as st
import  math 

st.title("    Body Mass Index   ")


n=st.text_input("Name : ")

st.radio("Select Gender :",('Male','Female'))

a=st.number_input('Age of The person',min_value=1)

st.text_area('Address :')

st.text("Hobbies")
st.checkbox('Danceing')
st.checkbox('Singing')
st.checkbox('Reading')
st.checkbox('Playing')

h=st.number_input('Height of person in cms',min_value=1)

w=st.number_input('weight of person in Kgs',min_value=1)

bmi=(w/(math.sqrt(h))*10000)


st.write("Body Mass Index of {} : {} ".format(n,bmi))
