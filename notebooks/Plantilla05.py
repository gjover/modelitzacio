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
# ## Pràctica 5
# ### Una teulada per un canaló
#
# [<center><img src=./static/FiberGutter1.jpg width=50%></center>](#img_Gutter)

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
# ## Una teulada per un canaló
# - Un fabricant de canalons ha de preparar una fitxa tècnica del seu producte.
# - Vol saber amb quin rang d'inclinació de la teula, intensitat de pluja i duració són compatibles els seus canalons.
# - Necessita saber aquests valors per què l'aigua no vessi amb un CL del 99%.
# - Els canalons són de mitja canya amb un diàmetre de $15.00 \pm 0.01 \,cm$.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Dades
# - Per validar el model hem contractat un laboratori d'assaigs que ha fet les següents mesures:
#     - Canaló de $12.00 \pm 0.01 \,m$
#     - Canonada baixant de $63.0 \pm 0.1 \,mm$
#     - Teulada amb superfície efectiva de $(12.00 \pm 0.01 \times 10.00 \pm 0.01) \,m^2$
#     - Intensitats de pluja creixents 1 minut a $30.00 \pm 0.01 \,l/h$, 2 minuts a $60.00 \pm 0.01 \,l/h$ i 4 minuts a $90.00 \pm 0.01 \,l/h$
#     - Es mesura el cabal d'aigua sobre la teula, el cabal d'aigua a la sortida de la canonada i el nivell d'aigua al canaló

# %% slideshow={"slide_type": "subslide"}
# Dades
data = pd.read_csv("../data/gutter.csv")
print(data.columns)
l = pd.plotting.scatter_matrix(data[data.columns])

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Coneixements previs
# - El cabal d'aigua a una canonada en funció de la columna d'aigua a l'entrada és:
#
# $$Q = A \sqrt{2gh}$$
#
#     - Q és el cabal d'aigua
#     - A és l'àrea de la secció de la canonada
#     - g és l'acceleració de la gravetat ($9.80665 \,m/s^2$)
#     - h és l'alçada de la columna d'aigua
# - L'àrea del segment circular és:
#
# $$
# \begin{align}
# A & = \frac{R^2}{2}\left(\theta - \sin \theta \right) \\
# \cos \theta/2 & = \frac{R - h}{R} \\
# \sin \theta/2 & = \frac{\sqrt{2Rh - h^2}}{R} \\
# \sin \theta &= 2 \sin \theta/2 \cos \theta/2 \\
# \end{align}
# $$
#
# [<center><img src=./static/Circularsegment.png></center>](#img_Segment)

# %% slideshow={"slide_type": "subslide"}
from sympy.abc import A, g, h, R, theta

# cabal d'aigua a una canonada
Q = A * sp.sqrt(2 * g * h)

# Àrea del segment circular
a = R * R / 2 * (theta - sp.sin(theta))

show(Q, qq, a)

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
# - <a id='img_Gutter'></a> https://commons.wikimedia.org/wiki/File:FiberGutter1.jpg
# - <a id='img_Segment'></a> https://commons.wikimedia.org/wiki/File:Circularsegment.svg

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
# [GFDL]: https://www.gnu.org/graphics/gfdl-logo.svg
# [GPL3]: https://www.gnu.org/graphics/gplv3-or-later.svg
