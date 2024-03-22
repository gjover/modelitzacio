# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Pràctica 8
# ### Publicitat
#
# [<center><img src=https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Mejores_Productos_Online.jpg/800px-Mejores_Productos_Online.jpg width=50%></center>](#img_Productos)

# %% slideshow={"slide_type": "skip"}
import numpy as np
import pandas as pd
import scipy
from scipy import stats
import matplotlib.pyplot as plt
from IPython.display import Math, display
import sympy as sp
from sympy.physics.units.systems import SI
from sympy.physics.units import meter, second, liter, hour, degree, convert_to
from sympy import sin, cos, pi, Abs

sp.init_printing()

def show(*args):
    out = ""
    for arg in args:
        if isinstance(arg, (sp.Expr, sp.Eq)):
            arg = sp.latex(arg)
        else:
            arg = str(arg)
        out += arg
    display(Math(out))
    
qq = "\quad "

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Publicitat
# - Un grup de publicistes vol que estudiem l'impacte de les campanyes publicitaries mitjançant «difusió social».
# - S'estima que el públic objectiu és de 220.000 possibles compradors.
# - Estudis previs han mostrat que el boca-orella fa que les vendes augmenten un 1% al mes per cada 500 vendes fetes.
# - Volen saber amb un CL 95% a quin percentatge de la població poden arribar en 1 any amb una promoció inicial on es regalen 4000 unitats.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Dades
# - Per validar el model s'ha fet un estudi estadístic a una població de 30.000 individus amb una promoció inicial de 1000 unitats.

# %% slideshow={"slide_type": "subslide"}
# Dades
data = pd.read_csv("../data/sales.csv")
print(data.columns)
l = pd.plotting.scatter_matrix(data[data.columns])

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Apartats
# - Descriu i analitza el sistema rellevant per a l'estudi (5 punts)
# - Fes les assumpcions pertinents i argumenta-les adequadament (5 punts)
# - Modelitza i resol el model (10 punts)
# - Verifica i valida el model (10 punts)
# - Fes una anàlisi crítica dels resultats (5 punts)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Anàlisi del sistema

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Context

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Paràmetres

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Paràmetres de l'assaig

# %% slideshow={"slide_type": "subslide"}
# Visualització de dades
# l = data.plot(x="", y="")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Assumpcions

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Modelització

# %% slideshow={"slide_type": "subslide"}
# from sympy.abc import t
# S = sp.Function('S', positive=True)(t)

# Sp = sp.diff(S, t)
# fS = ...

# eq = sp.Eq(Sp, fS)
# ics = {...}

# sol = sp.dsolve(eq, S, ics=ics)
# St = sol.rhs
# St = sp.separatevars(St)
# St

# %% slideshow={"slide_type": "subslide"}
# Comportament del model
# valors = {...} # Posa les unitats

# fSt = sp.lambdify(t, St.subs(valors))

# temps = np.linspace(0, 300, 30)
# y = fSt(temps)
# plt.plot(temps, y)
# plt.legend(["y (unitats)"])
# plt.show()

# %% slideshow={"slide_type": "subslide"}
# Calcular el percentatge de la població que ha comprat després d'un any 

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Coeficients de sensitivitat del model

# %% slideshow={"slide_type": "subslide"}
# CX = X / F * sp.diff(F, X)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Verificació i validació

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Verificació

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Validació

# %% slideshow={"slide_type": "subslide"}
# Dades

# %% slideshow={"slide_type": "subslide"}
# Simulació

# %% slideshow={"slide_type": "subslide"}
# Discrepància
# E = S - D

# %% slideshow={"slide_type": "subslide"}
# Derivades parcials
# SX = sp.diff(E, X).subs(valors).n()


# %% slideshow={"slide_type": "subslide"}
# Incertesa de l'estimació de la discrepància
# up2 = np.sum(np.power([
#     SX * EX,
# ], 2))

# uV = sp.sqrt(up2 + uD**2)

# %% slideshow={"slide_type": "subslide"}
# Discrepància
# show("E = %0.3f \pm %0.3f" % (E, uV))

# %% slideshow={"slide_type": "subslide"}
# Interval de t per un nivell de confiança del X%
# ti = stats.t.interval(X, ndata)[1]

# %% slideshow={"slide_type": "subslide"}
# Percentatge de la població que ha comprat després d'un any amb un nivell de confiança del 95%

# %% slideshow={"slide_type": "subslide"}
# Incertesa en el percentatge
# SX = sp.diff(F, X).subs(valors).n()

# uF = np.sum(np.power([
#     SX * EX,
# ], 2)).subs(valors)

# %% slideshow={"slide_type": "subslide"}
# Comprovació

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Anàlisi crítica

# %% [markdown] slideshow={"slide_type": "subslide"}
#

# %% [markdown] slideshow={"slide_type": "slide"}
#  

# %% [markdown] slideshow={"slide_type": "skip"}
# # Referències
#
# - <a id='img_Productos'></a> https://commons.wikimedia.org/wiki/File:Mejores_Productos_Online.jpg

# %% [markdown] slideshow={"slide_type": "skip"}
# Copyright (C) 2022 Gabriel Jover Mañas
#
#     Permission is granted to copy, distribute and/or modify this document
#     under the terms of the GNU Free Documentation License, Version 1.3
#     or any later version published by the Free Software Foundation;
#     with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
#     A copy of the license is included in the section entitled "GNU
#     Free Documentation License".
#
# ![GFDL][GFDL]
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ![GPL3][GPL3]
#
# [GFDL]: static/gfdl-logo-small.png
# [GPL3]: static/gplv3-127x51.png
