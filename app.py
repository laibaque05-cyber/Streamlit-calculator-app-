
import  streamlit as st
# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Smart Calculator", page_icon="🧮", layout="centered")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
        .main {
            background-color: #f0f4f8;
            padding: 2rem;
            border-radius: 15px;
        }
        .stButton>button {
            background-color: #0078ff;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            height: 3em;
            width: 100%;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #005fcc;
        }
        h1 {
            text-align: center;
            color: #005fcc;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("🧮 Smart Streamlit Calculator")

st.markdown("### Perform basic arithmetic operations easily!")

# ---------- INPUTS ----------
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number", value=0.0, step=1.0)
with col2:
    num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# ---------- OPERATION ----------
operation = st.radio(
    "Select Operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"],
    horizontal=True
)

# ---------- CALCULATE ----------
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (×)":
        result = num1 * num2
    elif operation == "Division (÷)":
        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
            result = None
        else:
            result = num1 / num2
    if result is not None:
        st.success(f"✅ **Result:** {result}")

