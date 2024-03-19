import streamlit as st
from datetime import datetime

def calculate_age(date_of_birth):
    # Convert date of birth string to datetime object
    dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
    # Get current date
    current_date = datetime.now()
    # Calculate age
    age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
    return age

def main():
    st.title("Age Calculator")
    date_of_birth = st.date_input("Enter your date of birth:")
    
    if st.button("Calculate Age"):
        age = calculate_age(str(date_of_birth))
        st.write(f"You are {age} years old.")

if __name__ == "__main__":
    main()
