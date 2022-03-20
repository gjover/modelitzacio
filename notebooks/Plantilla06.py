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
# ## Pràctica 6
# ### Gestió de residus
#
# [<center><img src=./static/Deer_Island_digesters.jpg width=50%></center>](#img_Deer_Island)

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
# ## Gestió de residus
# - Tenim una planta de gestió de residus i hem de limitar la concentració d'un reactiu
# - El nostre reactor està compost de 2 dipòsits connectats en sèrie amb un cabal continu.
# - Volem saber quin ha de ser el cabal d'aigua per no superar a la sortida una concentració de $0.05 \pm 0.01\, mg/l$ amb un CL del 99%
# - Al primer dipòsit es carrega el reactiu
# - Del primer dipòsit passen al segon i d'ací surten cap a la següent fase.
# - El volum dels dipòsits és de $100.0 \pm 0.1 \,m^3$
# - Cada càrrega és de $80.0 \pm 0.1 \,g$ de reactiu
# - El reactiu té una taxa de descomposició de $0.10 \pm 0.01\, min^{-1}$ reaccions per segon

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Dades
# - Per validar el model hem contractat un laboratori d'assaigs que ha fet les següents mesures:
#     - Volum d'aigua dels tancs de proves $1.0000 \pm 1\times10^{-4} m^3$
#     - Concentració inicial $10.0 \pm 0.1 \,mg/l$
#     - Flux d'aigua $60.000 \pm 0.001 \,l/s$

# %% slideshow={"slide_type": "subslide"}
# Dades
data = pd.read_csv("../data/reactiu.csv")
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

# %% slideshow={"slide_type": "subslide"}
# Visualització de dades
# l = data.plot(x="", y="")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Assumpcions

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Modelització

# %%
# P = sp.Function()(x)
# Pp = sp.diff(P, x)
# fP = 
# eq = sp.Eq(Pp, fP)

# %%
# sp.classify_ode(eq)

# %%
# sp.dsolve(eq, P)

# %%
#valors = {}
#par = {}

#ft = sp.lambdify(t, f.subs(valors).subs(par))

#temps = np.linspace(0, 60, 50)
#y = ft(temps)

#l = plt.plot(temps, y)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Coeficients de sensitivitat del model

# %% slideshow={"slide_type": "subslide"}
# CX = X / F * sp.diff(F, X)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Verificació i validació

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Verificació

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Validació

# %%
# Dades

# %% slideshow={"slide_type": "subslide"}
# Simulació

# %% slideshow={"slide_type": "subslide"}
# Discrepància
# E = S - D
# E

# %% slideshow={"slide_type": "subslide"}
# Derivades parcials
# mesures = {}
# SX = sp.diff(E, X).subs(valors).subs(mesures).n()

# %% slideshow={"slide_type": "subslide"}
# Incertesa dels paràmetres al quadrat
# up2 = np.sum(np.power([
#     SX * EX,
# ], 2))
# up2

# %% slideshow={"slide_type": "subslide"}
# Incertesa de l'estimació de la discrepància
# uV = np.sqrt(up2)

# Discrepància
# show("E = %0.3f \pm %0.3f" % (E, uV))

# %% slideshow={"slide_type": "subslide"}
# Nivell de confiança per un error del 5% amb nu graus de llibertat
# t = 0.05 / ur
# l, h = stats.t.cdf([-t, t], nu)
# CL = h - l

# %% slideshow={"slide_type": "subslide"}
# Interval de t per un cert nivell de confiança amb nu graus de llibertat
# stats.t.interval(CL, nu) 

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Anàlisi crítica

# %% slideshow={"slide_type": "subslide"}
# Resultat


# %% [markdown] slideshow={"slide_type": "slide"}
#  

# %% [markdown] slideshow={"slide_type": "skip"}
# # Referències
#
# - <a id='bib_Edwards'></a> Edwards, D., **2001**. *Guide to mathematical modelling*. Palgrave, Basingstoke.
# - <a id='img_Deer_Island'></a> https://commons.wikimedia.org/wiki/File:Deer_Island_P1110304.jpg

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
