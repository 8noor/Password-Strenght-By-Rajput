import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Checker By Anum Rajput", page_icon="🗝️", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
    .stButton button:hover {background-color: red; color:white}
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Generator")
st.write("Check the strength of your password and make it more secure.🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters** long.")

    # Check for uppercase and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain **uppercase and lowercase letters**.")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one number (0-9)**.")

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+{}|:<>?~]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")

    # Display password strength result
    if score == 4:
        st.success("✅ **Strong Password** - Your password is strong and secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Please make it stronger.")

    # Display feedback
    if feedback:
        with st.expander(" 🔍 **Improve your password**"):
            for item in feedback:
                st.write(item)

# Main input field
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong and secure 🔒.")

# Check button
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
