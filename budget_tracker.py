import streamlit as st
import pandas as pd
from datetime import date

# Title
st.title("💰 Personal Budget Tracker")

# Create session state to store expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Section title
st.subheader("Add a New Expense")

# Input fields
expense_date = st.date_input("Date", value=date.today())
expense_item = st.text_input("Expense Item")
amount_spent = st.text_input("Amount Spent (RM)")

# Submit button
if st.button("Add Expense"):
    try:
        # Convert amount to float
        amount = float(amount_spent)

        # Check if amount is negative
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        # Save expense into session state
        st.session_state.expenses.append({
            "Date": expense_date,
            "Expense Item": expense_item,
            "Amount Spent (RM)": amount
        })

        st.success(f'Expense "{expense_item}" added successfully!')

    except ValueError:
        st.error("Please enter a valid positive number for Amount Spent.")

# Display expenses
st.subheader("Expense Summary")

if st.session_state.expenses:
    # Convert list to DataFrame
    df = pd.DataFrame(st.session_state.expenses)

    # Display table
    st.table(df)

    # Calculate total
    total_expenses = df["Amount Spent (RM)"].sum()

    # Show total
    st.markdown(f"### Total Expenses: RM {total_expenses:.2f}")

else:
    st.info("No expenses added yet.")