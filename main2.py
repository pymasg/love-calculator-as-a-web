import streamlit as st


def reduce_number(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n


def cal(boy, girl):

    name1 = boy
    name2 = girl

    combined = name1.lower() + name2.lower()

    # Count letters in "TRUE"
    true_count = sum(combined.count(char) for char in ['t', 'r', 'u', 'e'])
    # Count letters in "LOVE"
    love_count = sum(combined.count(char) for char in ['l', 'o', 'v', 'e'])

    # Reduce counts to single digits
    true_digit = reduce_number(true_count)
    love_digit = reduce_number(love_count)

    # Calculate love percentage
    love_percentage = int(f"{true_digit}{love_digit}")

    return love_percentage


st.set_page_config(page_title="Love calculator", page_icon="💕")

st.header(body="❤️ Love Calculator ❤️", divider='rainbow')

boy_name = st.text_input(label="Your boy name: ")

girl_name = st.text_input(label="Girl name: ")

btn = st.button(label="Calculate love")

if btn:
    st.header(body="", divider='rainbow')
    st.header(body="")
    per = cal(boy=boy_name, girl=girl_name)
    if per >= 50:
        st.success(f"Love Percentage is {per} % ❤️")
        st.balloons()
    else:
        st.warning(f"Love Percentage is {per} % 😿😿")
    st.header(body="", divider='rainbow')
