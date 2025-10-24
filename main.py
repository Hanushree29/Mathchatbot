import streamlit as st
import google.genai as genai
import os

# 🔑 Get your Gemini API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

# 📋 Base prompt for the Math Chatbot
PROMPT_TEXT = (
    "You are a professional Math Chatbot. "
    "Solve the provided math problem step by step, showing all reasoning clearly. "
    "Provide the final answer separately, and explain any formulas or methods used. "
    "Maintain a clear, educational, and patient tone suitable for learners of all levels."
)

# Streamlit App
st.set_page_config(page_title="Math Chatbot", page_icon="🧮")
st.title("🧮 Math Chatbot")
st.write("Enter a math question, and get a detailed step-by-step solution.")

# Input box for the math question
question = st.text_input("Your Math Question:")

# Button to generate solution
if st.button("Solve"):
    if not question.strip():
        st.warning("Please enter a valid math question.")
    else:
        if not API_KEY:
            st.error("❌ API Key not found! Please set the GEMINI_API_KEY environment variable.")
        else:
            try:
                client = genai.Client(api_key=API_KEY)

                # Combine prompt + user question
                full_prompt = f"{PROMPT_TEXT}\n\nQuestion: {question}"

                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=[full_prompt]
                )

                st.subheader("✅ Solution")
                st.text(response.text.strip())

            except Exception as e:
                st.error(f"❌ API Error: {e}")
