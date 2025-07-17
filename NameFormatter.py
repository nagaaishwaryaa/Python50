import streamlit as st

st.set_page_config(page_title="Name Formatter", layout="centered")

st.title("🎨 Stylish Name Formatter")

# Input full name
full_name = st.text_input("Enter Full Name", placeholder="e.g., John Michael Smith")

# CSS styles for different formats
styles = {
    "first_last": "color:#1f77b4; font-size:22px; font-family:Arial;",
    "last_first": "color:#ff7f0e; font-size:22px; font-family:'Courier New', monospace;",
    "initials": "color:#2ca02c; font-size:22px; font-family:'Lucida Console', Monaco;",
    "first_middle_last": "color:#d62728; font-size:22px; font-family:'Georgia', serif;",
    "last_first_middle": "color:#9467bd; font-size:22px; font-family:'Trebuchet MS', sans-serif;"
}

# Display formatted outputs
if full_name:
    parts = full_name.strip().split()

    if len(parts) < 2:
        st.warning("Please enter at least a first and last name.")
    else:
        first = parts[0]
        last = parts[-1]
        middle = " ".join(parts[1:-1]) if len(parts) > 2 else ""

        st.subheader("Formatted Versions:")

        st.markdown(f"<p style='{styles['first_last']}'>• First Last: <b>{first} {last}</b></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='{styles['last_first']}'>• Last, First: <b>{last}, {first}</b></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='{styles['initials']}'>• Initials: <b>{''.join([p[0].upper() for p in parts])}</b></p>", unsafe_allow_html=True)

        if middle:
            st.markdown(f"<p style='{styles['first_middle_last']}'>• First Middle Last: <b>{first} {middle} {last}</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{styles['last_first_middle']}'>• Last First Middle: <b>{last} {first} {middle}</b></p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='{styles['first_middle_last']}'>• First Last: <b>{first} {last}</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='{styles['last_first_middle']}'>• Last First: <b>{last} {first}</b></p>", unsafe_allow_html=True)
