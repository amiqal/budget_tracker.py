import streamlit as st
import pandas as pd
from datetime import date

# Title
st.title("💰 Personal Budget Tracker")

# Initialize session state for storing expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Form for input
st.subheader("Add a New Expense")

expense_date = st.date_input("Date", value=date.today())
expense_item = st.text_input("Expense Item")
amount_spent = st.text_input("Amount Spent (RM)")

# Submit button
if st.button("Add Expense"):
    try:
        amount = float(amount_spent)

        if amount < 0:
            st.error("❌ Amount cannot be negative!")
        elif expense_item == "":
            st.error("❌ Please enter an expense item!")
        else:
            # Save expense
            st.session_state.expenses.append({
                "Date": expense_date,
                "Expense Item": expense_item,
                "Amount Spent (RM)": amount
            })
            st.success(f"✅ Expense '{expense_item}' added successfully!")

    except ValueError:
        st.error("❌ Amount must be a valid number!")

# Display table
st.subheader("Expense Summary")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.table(df)

    # Calculate total
    total = df["Amount Spent (RM)"].sum()
    st.markdown(f"### 💵 Total Expenses: RM {total:.2f}")
else:
    st.info("No expenses added yet.")