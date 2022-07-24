import streamlit as st

def sub(a,b):
	return a-b


st.title("Subtracting two numbers")

a = st.number_input("First number")

b = st.number_input("Second number")


if st.button("Calculate"):
	if type(a) != str and type(b)!=str:
		val = sub(a,b)
		st.write(val)
	else:
		st.write("Please enter a valid number")


