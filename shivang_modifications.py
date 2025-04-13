import streamlit as st

# Page setup
st.set_page_config(page_title="Shivang's Calculator", layout="centered")

# CSS styling and animation
st.markdown("""
    <style>
    html, body {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f9f9fc;
    }

    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }

    @keyframes slideIn {
        0% {transform: translateY(-30px); opacity: 0;}
        100% {transform: translateY(0); opacity: 1;}
    }

    .fadeIn {
        animation: fadeIn 2s ease-in;
    }

    .slideIn {
        animation: slideIn 1.5s ease-out;
    }

    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 24px;
        animation: fadeIn 3s ease-in-out;
    }

    .stButton > button:hover {
        background-color: #3e8e41;
    }
    </style>
""", unsafe_allow_html=True)

# Manage page state
if "page" not in st.session_state:
    st.session_state.page = "intro"

# Intro page
def intro_page():
    st.markdown("<h1 class='fadeIn'>👋 Welcome to Shivang's Calculator!</h1>", unsafe_allow_html=True)
    st.markdown("<p class='slideIn' style='font-size: 20px;'>A smooth and animated calculator by codingClone486.</p>", unsafe_allow_html=True)

    st.markdown("""
        ### ✨ Features:
        - Perform basic arithmetic operations
        - Stylish transitions and animations
    """)

    if st.button("🚀 Start Calculating"):
        st.session_state.page = "calculator"
        st.rerun()

# Calculator page
def calculator_page():
    st.title("🧮 Shivang's Calculator")

    num1 = st.number_input("Enter first number", key="num1")
    num2 = st.number_input("Enter second number", key="num2")
    operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

    def calculate(n1, n2, op):
        if op == "Add":
            return n1 + n2
        elif op == "Subtract":
            return n1 - n2
        elif op == "Multiply":
            return n1 * n2
        elif op == "Divide":
            if n2 == 0:
                return "❌ Cannot divide by zero!"
            return n1 / n2

    if st.button("Calculate"):
        result = calculate(num1, num2, operation)
        st.success(f"✅ Result: {result}")

        # Thanks message at the end
        st.markdown("<p class='slideIn' style='font-size: 18px;'>Thanks for using Shivang's Calculator! 😊</p>", unsafe_allow_html=True)

    if st.button("🔙 Back to Intro"):
        st.session_state.page = "intro"
        st.rerun()

# Display the appropriate page
if st.session_state.page == "intro":
    intro_page()
else:
    calculator_page()
