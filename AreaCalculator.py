import streamlit as st
import matplotlib.pyplot as plt
import math

st.set_page_config(page_title="Area Calculator", layout="centered")
st.title("📐 Simple Shape Area Calculator")

# --- Area calculation functions ---
def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, breadth):
    return length * breadth

def area_triangle(a, b, c):
    s = (a + b + c) / 2
    try:
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    except:
        return None  # Invalid triangle

# --- Dropdown UI ---
shape = st.selectbox("Choose a shape", ["Circle", "Rectangle", "Triangle"])

# --- Create a smaller figure for plot ---
fig, ax = plt.subplots(figsize=(4, 4))  # smaller figure

# --- Circle ---
if shape == "Circle":
    radius = st.number_input("Enter Radius", min_value=0.1, value=3.0)

    area = area_circle(radius)
    st.success(f"Area: {area:.2f} sq units")

    circle = plt.Circle((0, 0), radius, color='skyblue', edgecolor='black')
    ax.add_patch(circle)
    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)
    ax.set_aspect('equal')
    ax.set_title(f"Circle\nArea: {area:.2f}", fontsize=10)

# --- Rectangle ---
elif shape == "Rectangle":
    length = st.number_input("Enter Length", min_value=0.1, value=4.0)
    breadth = st.number_input("Enter Breadth", min_value=0.1, value=2.5)

    area = area_rectangle(length, breadth)
    st.success(f"Area: {area:.2f} sq units")

    rect = plt.Rectangle((0, 0), length, breadth, color='lightgreen', edgecolor='black')
    ax.add_patch(rect)
    ax.set_xlim(-1, length + 1)
    ax.set_ylim(-1, breadth + 1)
    ax.set_aspect('equal')
    ax.set_title(f"Rectangle\nArea: {area:.2f}", fontsize=10)

# --- Triangle ---
elif shape == "Triangle":
    a = st.number_input("Side A", min_value=0.1, value=3.0)
    b = st.number_input("Side B", min_value=0.1, value=4.0)
    c = st.number_input("Side C", min_value=0.1, value=5.0)

    if a + b > c and a + c > b and b + c > a:
        area = area_triangle(a, b, c)
        st.success(f"Area: {area:.2f} sq units")

        # Triangle plotting based on assumed base
        angle_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
        x3 = b * math.cos(angle_C)
        y3 = b * math.sin(angle_C)

        triangle = plt.Polygon([[0, 0], [a, 0], [x3, y3]], color='orange', edgecolor='black')
        ax.add_patch(triangle)
        ax.set_xlim(-1, max(a, x3) + 1)
        ax.set_ylim(-1, y3 + 2)
        ax.set_aspect('equal')
        ax.set_title(f"Triangle\nArea: {area:.2f}", fontsize=10)
    else:
        st.error("Invalid triangle. Sum of any two sides must be greater than the third.")

# Show the resized plot
st.pyplot(fig)
