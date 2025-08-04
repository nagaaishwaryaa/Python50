import streamlit as st
from datetime import datetime

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year
    # Adjust age if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

# Streamlit UI
st.title("🎂 Age & Leap Year Checker")

name = st.text_input("Enter your name")
dob = st.date_input("Enter your Date of Birth")

if name and dob:
    birth_year = dob.year
    age = calculate_age(dob)
    leap_status = "a leap year" if is_leap_year(birth_year) else "a non-leap year"
    
    st.markdown(f"---")
    st.success(f"Dear **{name}**, your age is **{age}** and you were born in **{leap_status}**.")
