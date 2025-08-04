import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# === Conversion functions ===
def feet_to_meters(v): return v * 0.3048
def meters_to_feet(v): return v / 0.3048
def pounds_to_kg(v): return v * 0.453592
def kg_to_pounds(v): return v / 0.453592
def inches_to_cm(v): return v * 2.54
def cm_to_inches(v): return v / 2.54
def liters_to_ounces(v): return v * 33.814
def ounces_to_liters(v): return v / 33.814
def c_to_f(v): return (v * 9/5) + 32
def f_to_c(v): return (v - 32) * 5/9
def kmh_to_mph(v): return v * 0.621371
def mph_to_kmh(v): return v / 0.621371
def usd_to_inr(v): return v * 83.0   # Static rate
def inr_to_usd(v): return v / 83.0

# === Streamlit Theme ===
st.set_page_config(page_title="All-in-One Converter", layout="centered")

# === UI Header ===
st.title("🌐 Universal Unit Converter")


# === Conversion Type Selection ===
conversion_type = st.selectbox("Choose Conversion Type", [
    "Feet to Meters", "Meters to Feet",
    "Pounds to Kilograms", "Kilograms to Pounds",
    "Inches to Centimeters", "Centimeters to Inches",
    "Liters to Ounces", "Ounces to Liters",
    "Celsius to Fahrenheit", "Fahrenheit to Celsius",
    "Km/h to Mph", "Mph to Km/h",
    "USD to INR", "INR to USD"
])

# === Input from User ===
value = st.number_input("Enter value to convert", format="%.4f")

# === Perform Conversion ===
if st.button("Convert"):
    if conversion_type == "Feet to Meters":
        result = feet_to_meters(value)
        units = ("Feet", "Meters")
    elif conversion_type == "Meters to Feet":
        result = meters_to_feet(value)
        units = ("Meters", "Feet")
    elif conversion_type == "Pounds to Kilograms":
        result = pounds_to_kg(value)
        units = ("Pounds", "Kilograms")
    elif conversion_type == "Kilograms to Pounds":
        result = kg_to_pounds(value)
        units = ("Kilograms", "Pounds")
    elif conversion_type == "Inches to Centimeters":
        result = inches_to_cm(value)
        units = ("Inches", "Centimeters")
    elif conversion_type == "Centimeters to Inches":
        result = cm_to_inches(value)
        units = ("Centimeters", "Inches")
    elif conversion_type == "Liters to Ounces":
        result = liters_to_ounces(value)
        units = ("Liters", "Ounces")
    elif conversion_type == "Ounces to Liters":
        result = ounces_to_liters(value)
        units = ("Ounces", "Liters")
    elif conversion_type == "Celsius to Fahrenheit":
        result = c_to_f(value)
        units = ("Celsius", "Fahrenheit")
    elif conversion_type == "Fahrenheit to Celsius":
        result = f_to_c(value)
        units = ("Fahrenheit", "Celsius")
    elif conversion_type == "Km/h to Mph":
        result = kmh_to_mph(value)
        units = ("Km/h", "Mph")
    elif conversion_type == "Mph to Km/h":
        result = mph_to_kmh(value)
        units = ("Mph", "Km/h")
    elif conversion_type == "USD to INR":
        result = usd_to_inr(value)
        units = ("USD", "INR")
    elif conversion_type == "INR to USD":
        result = inr_to_usd(value)
        units = ("INR", "USD")

    # Display result
    st.success(f"{value:.4f} {units[0]} = {result:.4f} {units[1]}")

    # Graph
    df = pd.DataFrame({
        'Unit': [units[0], units[1]],
        'Value': [value, result]
    })

    fig, ax = plt.subplots()
    ax.bar(df['Unit'], df['Value'], color=['#00cec9', '#a29bfe'])
    ax.set_title('Conversion Chart')
    ax.set_ylabel('Value')
    st.pyplot(fig)
