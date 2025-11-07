Here’s a complete Streamlit Calculator App setup — including the app.py code and the requirements.txt file.


---

🧮 app.py

import streamlit as st

# App title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Simple Calculator")

# User inputs
st.write("Enter two numbers and select an operation:")
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox("Select operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Calculate result
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")
        else:
            st.error("Error: Division by zero is not allowed.")

# Footer
st.caption("Created with ❤️ using Streamlit")


---

📦 requirements.txt

streamlit==1.39.0


---

▶️ To Run the App

1. Save both files in the same folder:

app.py

requirements.txt



2. Install dependencies:

pip install -r requirements.txt


3. Run the Streamlit app:

streamlit run app.py



This will open your calculator in the browser at http://localhost:8501.

Would you like me to add extra features like history, dark mode, or scientific operations (e.g., square root, power)?
