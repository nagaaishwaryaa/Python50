import streamlit as st
import re

def count_text_metrics(paragraph):
    char_count_with_spaces = len(paragraph)
    char_count_without_spaces = len(paragraph.replace(" ", ""))

    word_count = len(paragraph.split())

    sentences = re.split(r'[.!?]+', paragraph)
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)

    return {
        "Characters (with spaces)": char_count_with_spaces,
        "Characters (without spaces)": char_count_without_spaces,
        "Words": word_count,
        "Sentences": sentence_count
    }

# ---------- Streamlit UI ---------- #

st.title("📝 Text Metrics Counter")

user_input = st.text_area("Enter your paragraph below:")

if user_input:
    results = count_text_metrics(user_input)

    st.subheader("📊 Results:")
    st.write(f"**Characters (with spaces):** {results['Characters (with spaces)']}")
    st.write(f"**Characters (without spaces):** {results['Characters (without spaces)']}")
    st.write(f"**Words:** {results['Words']}")
    st.write(f"**Sentences:** {results['Sentences']}")
else:
    st.info("Please enter a paragraph above to analyze.")

