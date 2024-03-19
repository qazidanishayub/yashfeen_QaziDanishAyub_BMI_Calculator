import streamlit as st

def calculate_bmi(height_feet, weight_kg):
    # Convert height from feet to meters
    height_meters = height_feet * 0.3048
    # Calculate BMI
    bmi = weight_kg / (height_meters ** 2)
    return bmi

def main():
    st.title("BMI Calculator")

    # Get user input
    name = st.text_input("Enter your name:")
    height_feet = st.number_input("Enter your height in feet:")
    weight_kg = st.number_input("Enter your weight in kilograms:")

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(height_feet, weight_kg)
        st.write(f"Hello {name}! Your BMI is: {bmi:.2f}")

if __name__ == "__main__":
    main()
