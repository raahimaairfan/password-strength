import re
import random
import string
import streamlit as st

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(12))

def check_password_strength(password):
    score = 0
    common_passwords = ["password", "123456", "qwerty", "password123", "admin", "letmein"]
    
    if password in common_passwords:
        return "❌ This password is too common. Choose a unique one.", None, "#ff4d4d", 0
    
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", None, "#2ecc71", 100
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", None, "#f39c12", 65
    elif score == 2:
        return "⚠️ Weak Password - Needs more complexity.", generate_strong_password(), "#e67e22", 45
    else:
        return "❌ Very Weak Password - Improve it using the suggestions above.", generate_strong_password(), "#ff4d4d", 20

# Streamlit UI Styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
            font-family: Arial, sans-serif;
        }
        .stTextInput>div>div>input {
            border: 2px solid #2980b9;
            border-radius: 10px;
            padding: 10px;
            font-size: 18px;
            width: 100%;
        }
        .stProgress > div > div > div > div {
            border-radius: 10px;
            transition: width 0.5s ease-in-out;
        }
        .title {
            font-size: 32px;
            font-weight: bold;
            color: black;
            text-align: center;
            padding: 15px;
            border-radius: 10px;
            background: rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        .container {
            text-align: center;
            padding: 30px;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.1);
            width: 50%;
            margin: auto;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🔐 Password Strength Meter</div>", unsafe_allow_html=True)
st.markdown("<div class='container'>", unsafe_allow_html=True)
password = st.text_input("Enter your password:", type="password")

if password:
    message, suggestion, color, strength = check_password_strength(password)
    
    st.progress(strength / 100)
    st.markdown(f"<span style='color:{color}; font-size:18px; font-weight:bold;'>{message}</span>", unsafe_allow_html=True)
    
    if suggestion:
        st.write("💡 Suggested Strong Password:", suggestion)

st.markdown("</div>", unsafe_allow_html=True)