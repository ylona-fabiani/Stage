import streamlit as st
import numpy as np
import pandas as pd
import math


st.write("# My first challenge")

x = st.sidebar.number_input("Enter a x value :", 1)
f_input = st.sidebar.text_input("Enter a python function:", "x")
st.sidebar.latex(f_input)


if x == "" or x == 0:
    raise Exception("Erreur.")

st.write("Function =", eval(f_input))

x_min = st.sidebar.number_input("x_min ?", step=0.5)
x_max = st.sidebar.number_input("x_max ?", step=0.5)

"Your x_min is : ", x_min
"Your x_max is : ", x_max

dist = x_max - x_min
rows = []            # results f_input(x)
index = []           # absciss
x_old = x            # keep the value of old x

nbEchantillons = st.sidebar.number_input("Nombre d'échantillons ?", 0, 10000, 1000)

for i in range(nbEchantillons):
    x = x_min + (dist/nbEchantillons * i)   # find step of iteration
    rows.append(eval(f_input))              # append() add sth at the end
    index.append(x)                         # same

x = x_old     # restore value of x

st.write("Chart :")
df = pd.DataFrame(
    rows,
    index,
    columns=[f_input])
st.line_chart(df)
