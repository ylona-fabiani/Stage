import streamlit as st
import numpy as np
import pandas as pd
import math  # need it for f_input
import sympy as sp
from sympy import SympifyError
from sympy.core.function import UndefinedFunction
from sympy.core.function import AppliedUndef


st.write("# Function Plot")


@st.cache
def lins(mini, maxi, nb_samples):
    return np.linspace(start=mini, stop=maxi, num=nb_samples)


@st.cache
def compute_samples(user_input, mini, maxi, nb_samples):
    lin = lins(mini, maxi, nb_samples)
    df = pd.DataFrame(
        data=map(lambda x: float(user_input.evalf(subs={'x': x})), lin),  # map f(x) with the linspace
        index=lin,
        columns=[user_input])
    return df


if __name__ == '__main__':
    x = sp.symbols('x')
    f_input = st.sidebar.text_input("Enter a python function:", "x*x")
    try:
        expr = sp.sympify(f_input)
        if expr.atoms(AppliedUndef, UndefinedFunction):
            st.error("An error has occurred, the function %s is not valid." % expr)
        st.sidebar.latex(expr)
    except SympifyError:
        st.error("An error as occurred, please try again.")

    x_min = st.sidebar.number_input("x_min?", step=0.5, value=1.0, help="Choose a min value for your x")
    x_max = st.sidebar.number_input("x_max?", step=0.5, value=5.0, help="Choose a max value for your x")
    st.write("Your x_min is: ", x_min, "Your x_max is: ", x_max)

    samples = st.sidebar.number_input("Sample size?", 0, 10000, 100, help="Choose a number of samples between 0 and "
                                                                          "10000")

    st.write("Chart:")
    st.line_chart(compute_samples(expr, x_min, x_max, samples))
