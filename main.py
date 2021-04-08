import streamlit as st
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import sympy as sp

st.write("# My first challenge")


def f_user():
    x = 2
    f_input = st.sidebar.text_input("Enter a python function:", "x")
    st.sidebar.latex(f_input)

    x_min = st.sidebar.number_input("x_min?", step=0.5)
    x_max = st.sidebar.number_input("x_max?", step=0.5)
    st.write("Your x_min is: ", x_min, "Your x_max is: ", x_max)
    # dist = x_max - x_min
    # rows = []  # results f_input(x)
    # index = []  # absciss
    samples = st.sidebar.number_input("Sample size?", 0, 10000, 100)

#    for i in range(samples):
#        x = x_min + (dist / samples * i)  # find step of iteration
#       rows.append(eval(f_input))  # append() add sth at the end
#       index.append(x)  # same
    index = np.linspace(x_min, x_max, samples)
    st.write("Chart:")
    df = pd.DataFrame(
        eval(f_input),
        index,
        columns=[f_input])
    st.line_chart(df)


if __name__ == '__main__':
    f_user()
