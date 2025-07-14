import streamlit as st
import time
from streamlit.components.v1 import html

st.set_page_config(page_title="Spoken Countdown Timer", layout="centered")

st.markdown(
    """
    <style>
    .big-button > button {
        height: 60px;
        width: 250px;
        font-size: 22px;
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🗣️ Spoken Countdown Timer")

countdown_placeholder = st.empty()

# Function to speak a number using JS
def speak_number(number):
    html(f"""
        <script>
        var utterance = new SpeechSynthesisUtterance("{number}");
        speechSynthesis.speak(utterance);
        </script>
    """, height=0)

# Bigger button inside a styled container
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔁 Start / Restart Countdown", key="start", help="Start countdown"):
            for i in range(10, -1, -1):
                countdown_placeholder.markdown(
                    f"<h1 style='text-align: center; color: red; font-size: 80px;'>{i}</h1>",
                    unsafe_allow_html=True
                )
                speak_number(i)
                # Delay AFTER speech so the number remains visible while voice plays
                time.sleep(2)

            st.success("🎉 Countdown Complete!")

            # Final beep
            html("""
                <script>
                var audio = new Audio("https://actions.google.com/sounds/v1/alarms/beep_short.ogg");
                audio.play();
                </script>
            """, height=0)
