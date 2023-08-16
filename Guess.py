import streamlit as st
from PIL import Image


import random

st.header('Dice Game')
st.subheader ('Lets see how good you are at guessing')
st.image('roll dice.gif')


a = random.randint (1,6)
b = st.number_input('Please input a number from 1-6', step=1)

def randgame (a,b):
    
    if b > 6:
        return ('Invalid Input, please select a number between 1-6')

    else:
        if a == b:
            return ('Correct')

        else:
            st.write (f'Your selected number is {b}')
            st.write (f'Random number is {a}')
            return ('Wrong, try again')


if st.button ('Try your luck'):
    st.write(randgame(a,b))