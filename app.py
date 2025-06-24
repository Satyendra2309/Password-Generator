import streamlit as st
import random
import string

st.set_page_config(page_title="Password Generator", layout="centered")
st.title("🔐Password Generator")

n = st.number_input("Enter the length of the password", min_value=4, max_value=100, step=1)
alpha = st.checkbox("Include Alphabets", value=True)
numbers = st.checkbox("Include Numbers")
special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    if not (alpha or numbers or special):
        st.error("Please select at least one option!")
    else:
        chars = ""
        if alpha:
            chars += string.ascii_letters
        if numbers:
            chars += string.digits
        if special:
            chars += string.punctuation
        
        password = ''.join(random.choice(chars) for _ in range(n))
        st.success("Generated Password:")
        st.code(password, language='text')
