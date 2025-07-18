import streamlit as st
import re

# Function to reverse individual words in a sentence
def reverse_words(sentence, reverse_all=True, keep_punct=True, change_case=None):
    original_sentence = sentence
    words = sentence.split()

    def reverse_word(word):
        if keep_punct:
            match = re.match(r"([\w\u0900-\u097F\u0B80-\u0BFF]+)([^\w\s]*)", word)
            if match:
                base, punct = match.groups()
                return base[::-1] + (punct or "")
            else:
                return word[::-1]
        else:
            return word[::-1]

    if reverse_all:
        reversed_words = [reverse_word(word) for word in words]
    else:
        reversed_words = [word if len(word) <= 3 else reverse_word(word) for word in words]

    reversed_sentence = ' '.join(reversed_words)

    # Apply case change if requested
    if change_case == "lower":
        reversed_sentence = reversed_sentence.lower()
    elif change_case == "upper":
        reversed_sentence = reversed_sentence.upper()
    elif change_case == "title":
        reversed_sentence = reversed_sentence.title()

    return original_sentence, reversed_sentence

# Streamlit UI
st.set_page_config(page_title="Multilingual Word Reverser", layout="centered")
st.title("🌐 Multilingual Word Reverser with Undo")

sentence = st.text_area("✍️ Enter your sentence (supports Hindi, Tamil, etc.):", height=150)

reverse_all = st.checkbox("🔁 Reverse All Words", value=True)
keep_punct = st.checkbox("✒️ Keep Punctuation at the End", value=True)
change_case = st.radio("🔠 Change Case of Output:", options=[None, "lower", "upper", "title"],
                       format_func=lambda x: "No Change" if x is None else x.capitalize())

# Session state to store history for undo
if 'history' not in st.session_state:
    st.session_state.history = []

# Reverse button logic
if st.button("🔄 Reverse Words"):
    original, result = reverse_words(sentence, reverse_all, keep_punct, change_case)
    st.session_state.history.append((original, result))
    st.success("✅ Reversed Sentence:")
    st.write(result)

# Undo feature
if st.button("↩️ Undo Last Reversal") and st.session_state.history:
    st.session_state.history.pop()
    if st.session_state.history:
        last_original, last_result = st.session_state.history[-1]
        st.info("⏪ Restored Previous Reversal:")
        st.write(last_result)
    else:
        st.warning("⚠️ No previous reversal found.")

# Show reversal history
if st.session_state.history:
    st.subheader("🕒 Reversal History")
    for i, (orig, rev) in enumerate(reversed(st.session_state.history), 1):
        st.markdown(f"**{i}.** `{orig}` → `{rev}`")
