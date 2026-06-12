import streamlit as st
from openai import OpenAI
from fpdf import FPDF


st.set_page_config(page_title="AI Fitness Planner", layout="wide")
st.title("🏋️ Personalized Workout & Diet Planner AI")

client = OpenAI(
    api_key=st.secrets["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1"
)

st.sidebar.header("Enter Your Details")

age = st.sidebar.number_input("Age", 10, 80, 22)
weight = st.sidebar.number_input("Weight (kg)", 30, 150, 60)
height = st.sidebar.number_input("Height (cm)", 100, 220, 165)

goal = st.sidebar.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Stay Fit"])
diet_type = st.sidebar.selectbox("Diet Type", ["Vegetarian", "Non-Veg", "Vegan"])
budget = st.sidebar.selectbox("Budget Level", ["Low", "Medium", "High"])
activity = st.sidebar.selectbox("Activity Level", ["Low", "Moderate", "High"])



bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    bmi_status = "Underweight"
elif bmi < 25:
    bmi_status = "Normal"
elif bmi < 30:
    bmi_status = "Overweight"
else:
    bmi_status = "Obese"


col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🤖 Generate AI Plan"):

        prompt = f"""
        Create a personalized fitness and diet plan.

        Age: {age}
        Weight: {weight} kg
        Height: {height} cm
        Goal: {goal}
        Diet Type: {diet_type}
        Budget: {budget}
        Activity Level: {activity}

        Provide:
        1. Weekly Workout Plan
        2. Daily Diet Plan
        3. Calories Recommendation
        4. Health Tips
        """

        try:
            with st.spinner("Generating AI plan..."):

                response = client.chat.completions.create(
                    model="meta-llama/llama-3-8b-instruct",
                    messages=[{"role": "user", "content": prompt}]
                )

                st.session_state.plan = response.choices[0].message.content

                st.success("Plan Generated Successfully!")

        except Exception as e:
            st.error("API Error. Try again later.")



with col2:
    if st.button("📊 Show BMI Result"):
        st.subheader("Your BMI Report")
        st.write(f"**BMI Value:** {round(bmi,2)}")
        st.write(f"**Health Status:** {bmi_status}")



with col3:
    if st.button("📄 Download Plan as PDF"):

        if "plan" not in st.session_state:
            st.warning("Generate AI Plan first!")
        else:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            for line in st.session_state.plan.split("\n"):
                pdf.multi_cell(0, 8, line)

            pdf.output("fitness_plan.pdf")

            with open("fitness_plan.pdf", "rb") as file:
                st.download_button(
                    "Download PDF",
                    file,
                    file_name="fitness_plan.pdf"
                )



if "plan" in st.session_state:
    st.divider()
    st.subheader("🏆 Your AI Fitness Plan")
    st.write(st.session_state.plan)
