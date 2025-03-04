import streamlit as st

# Set page config
st.set_page_config(page_title="🔥 Stylish Temperature Converter", page_icon="🌡️", layout="centered")

# Apply custom CSS for animation, fonts, and styles
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        body {
            font-family: 'Poppins', sans-serif;
            background-color: #121212;
            color: white;
        }

        .stApp {
            background: #1e1e1e;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(255, 105, 135, 0.2);
        }

        /* New Stylish Heading */
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: 700;
            background: linear-gradient(90deg, #ff416c, #ff4b2b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 2px 2px 10px rgba(255, 105, 135, 0.5);
            animation: fadeIn 1.2s ease-in-out;
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .stButton>button {
            background: linear-gradient(90deg, #ff416c, #ff4b2b);
            color: white;
            font-weight: bold;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
            animation: fadeIn 0.8s ease-in-out;
        }

        .stButton>button:hover {
            background: linear-gradient(90deg, #e52d27, #b31217);
            transform: scale(1.05);
            box-shadow: 0px 0px 10px rgba(255, 75, 43, 0.8);
        }

        .stTextInput, .stNumberInput {
            animation: fadeIn 0.8s ease-in-out;
        }

        .stSuccess {
            animation: fadeIn 0.6s ease-in-out;
        }

        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Function to Convert Temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Fahrenheit":
        value = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        value = value - 273.15
    if to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif to_unit == "Kelvin":
        return value + 273.15
    return value

# Title with gradient and glow effect
st.markdown("<h1 class='title'>🌡️ Stylish & Animated Temperature Converter</h1>", unsafe_allow_html=True)

# Input fields with columns
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("Convert from:", ["Celsius", "Fahrenheit", "Kelvin"])
with col2:
    to_unit = st.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])

value = st.number_input("Enter Temperature:", min_value=-1000.0, max_value=1000.0, step=0.1)

# Convert Button
if st.button("🔥 Convert Temperature"):
    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"✅ Converted Temperature: **{result:.2f} {to_unit}**")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px; color: #ccc;'>✨ Built with love & animations using Streamlit ✨</p>", unsafe_allow_html=True)
