import streamlit as st
import datetime
from datetime import date
st.title("Age calculator")
name=st.text_input("Enter your name")
if name:
    st.write(f"Hey {name} ! lets calculate your age")
dob=st.date_input(
    "enter your dob",
                  min_value=datetime.date(1900,1,1),
                max_value=datetime.date.today())
today=date.today()
age=today.year -dob.year -((today.month,today.day) <(dob.month,dob.day))
if age>0:
    st.success(f"your age is {age+1}")
