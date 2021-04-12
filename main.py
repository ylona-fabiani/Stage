import streamlit as st
import numpy as np
import pandas as pd
import math
import sympy as sp

st.write("# My first challenge")


@st.cache(suppress_st_warning=True)
def lins(min, max, nb_samples):
    return np.linspace(start=min, stop=max, num=nb_samples)


@st.cache(suppress_st_warning=True)
def data_frame(input_user, lins, min, max, nb_samples):
    lin = lins(min, max, nb_samples)
    df = pd.DataFrame(
        data=map(lambda x: eval(input_user), lin),  # map f(x) with the linspace
        index=lin,
        columns=[input_user])
    return df


if __name__ == '__main__':
    x = 2
    f_input = st.sidebar.text_input("Enter a python function:", "x")
    st.sidebar.latex(f_input)

    x_min = st.sidebar.number_input("x_min?", step=0.5)
    x_max = st.sidebar.number_input("x_max?", step=0.5)
    st.write("Your x_min is: ", x_min, "Your x_max is: ", x_max)

    samples = st.sidebar.number_input("Sample size?", 0, 10000, 10)

    st.write("Chart:")
    st.line_chart(data_frame(f_input, lins, x_min, x_max, samples))
