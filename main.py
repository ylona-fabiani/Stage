import streamlit as st
import numpy as np
import pandas as pd
import math  # need it for f_input
import sympy as sp
from sympy import SympifyError
from sympy.core.function import UndefinedFunction
from sympy.core.function import AppliedUndef
from typing import Optional
from traceback import print_exc
import gettext


_ = gettext.gettext


@st.cache
def lins(mini, maxi, nb_samples):
    return np.linspace(start=mini, stop=maxi, num=nb_samples)


@st.cache
def compute_samples(user_input, expr, mini, maxi, nb_samples):
    lin = lins(mini, maxi, nb_samples)
    df = pd.DataFrame(
        data=map(lambda x: float(expr.evalf(subs={'x': x})), lin),  # map f(x) with the linspace
        index=lin,
        columns=[user_input])
    return df


def main():
    st.set_page_config(page_title="Function Plot", layout="wide", initial_sidebar_state="expanded")
    language = st.sidebar.selectbox("Languages:", ('English', 'Français'))
    if language == 'English':
        en = gettext.translation('base', localedir='locales', languages=['en'])
        en.install()
        _ = en.gettext
    if language == 'Français':
        fr = gettext.translation('base', localedir='locales', languages=['fr'])
        fr.install()
        _ = fr.gettext
    st.write(_("# Function Plot"))
    st.sidebar.write(_("**Function Definition:**"))
    # use a relatively complex default expression to serve as an example of the type of operations available to the user
    f_input = st.sidebar.text_input(_("Enter a mathematical expression:"), "1 / (1 + exp(-2 * pi * x))")
    st.sidebar.write(_("*For a full list of available functions click "),
                     "[here](https://docs.sympy.org/latest/modules/functions/index.html#contents)*")
    try:
        expr = sp.sympify(f_input)
    except SympifyError as e:
        raise UserError(_("Could not parse the input expression (%s), please enter a valid mathematical expression") % e.expr, cause=e)
    st.sidebar.latex(expr)

    undefined_functions = expr.atoms(AppliedUndef, UndefinedFunction)
    if undefined_functions:
        raise UserError(_("Invalid input, the function '%s' is not defined.") % list(undefined_functions)[0].name)
    for symbol in expr.free_symbols:
        if str(symbol) != 'x':
            raise UserError(_("Input must be a single-variable function of 'x'. You may not use a '%s' variable!") % symbol)

    st.sidebar.write(_("**Plot interval:**"))
    x_min = st.sidebar.number_input(_("Minimum value of 'x'"), step=0.5, value=-1.0)
    x_max = st.sidebar.number_input(_("Maximum value of 'x'"), step=0.5, value=1.0)

    samples = st.sidebar.number_input(_("Number of samples"), 0, 10000, 100)

    st.write(_("Function plot over interval [%s, %s] ") % (x_min, x_max))
    st.line_chart(compute_samples(f_input, expr, x_min, x_max, samples))


class UserError(BaseException):
    def __init__(self, userMessage: str, cause: Optional[BaseException] = None):
        self.userMessage = userMessage
        self.__cause__ = cause


if __name__ == "__main__":
    try:
        main()
    except UserError as e:
        st.error(e.userMessage)
    except BaseException as e:
        st.error(_("An unexpected error has occurred! Please verify your input and try again."))
        print_exc()

