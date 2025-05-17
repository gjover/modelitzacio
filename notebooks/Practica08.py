# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## Pràctica 8
#

# %%
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
import simpy

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

# %% [markdown]
# ### Exercici 1
# - A una cabina experimental es genera ozó, que és un gas tòxic que volem extreure.
# - Hem modelitzat l'extracció d'ozó de la següent manera:
# $$x'  = -x \cdot Q/V + O \cdot R $$
#
# on $x$ representa la concentració del gas, $Q$ representa el flux d'extracció d'aire, $V$ és el volum de l'habitació, $O$ és la concentració d'oxigen a l'aire i $R$ és el ritme de generació d'ozó.
#
# Els valors mesurats dels paràmetres són els següents:
# - La generació d'ozó es produeix a un ritme d'una molècula d'ozó per cada $(3.7 \pm 0.1) \times 10^9$ molècules d'oxigen per segon.
# - La concentració d'oxigen a l'aire és de $20.9476 \pm 0.0005 \%$
# - La cabina experimental té un volum de $125.4 \pm 0.8 \, m^3$
#

# %% [markdown]
# #### Dades
# - Per validar el model hem fet unes proves irradiant un volum d'aire amb un extractor.
#     - Volum d'aire $1.0000 \pm 1\times10^{-4} m^3$
#     - Cabal d'aire de l'extractor $1.0 \pm 0.1 \,l/s$
#     - La precisió de les mesures de concentració és de $1\times10^{-3}$ ppm

# %%
# Dades
data = pd.read_csv("https://raw.githubusercontent.com/gjover/modelitzacio/refs/heads/main/data/ozo.csv")
print(data.columns)
l = pd.plotting.scatter_matrix(data[data.columns])

# %% [markdown]
# - Fes la validació del model i una anàlisi crítica considerant que l'ozó és tòxic a concentracions de 5 ppm i el seu nivell de seguretat és de 0.1 ppm

# %% [markdown]
# ### Exercici 2

# %% [markdown]
# Tenim un taller en el qual hi ha 5 màquines idèntiques que processen tasques que arriben de forma aleatòria cada 12 minuts de mitjana.
# Les tasques s’assignen a qualsevol màquina que estigui lliure, o fan cua esperant que hi hagi alguna màquina lliure.
# El temps necessari per completar una tasca també és aleatori, però de mitjana es triga una hora per a totes les tasques i màquines.
#
# Al taller hi treballen 3 operaris, que tenen dues feines principals:
#
# - Preparar les màquines perquè inicien la tasca que ha arribat.
#
# - Reparar una màquina que ha fallat.
#
# La preparació de la tasca necessita un temps aleatori, però que de mitjana és de 20 minuts.
# La reparació necessita dos operaris i un temps aleatori, que de mitjana és de mitja hora.
# Quan ha finalitzat una tasca, el 20% dels cops cal reparar la màquina.
#
# - Fes 10 simulacions d'una setmana i calcula la llargària mitjana de la cua de tasques.
#
# - Què faries per reduir la cua de tasques i per què?
#

# %%
# def proces1(env, ###):
#     """
#     Explicació del procés
#     """
#     ###
#     with recurs.request() as req:
#         yield req
# 
#         p2 = proces2(###)
#         yield env.process(p2)
# 
#         temps = np.random.###
#         yield env.timeout(temps)

# %%
# log = pd.DataFrame(columns=['xxx'])
# env = simpy.Environment()
# 
# recurs = simpy.Resource(env, capacity=##)
# 
# env.process(###)
# env.run(until=###)

# %% [markdown]
# ### Exercici 3

# %% [markdown]
# Analitza la següent cadena de Markov:
# [<center><img src=https://raw.githubusercontent.com/gjover/modelitzacio/refs/heads/main/notebooks/static/markov.png width=25%></center>](#bib_Konstantopoulos)
#
# - Escriu la matriu de transició
# - És irreductible?
# - És aperiòdica?
# - Si comencem a l'estat 1, quina probabilitat n'hi ha que ens trobem a cada un dels estats deprés de 3 passes?
# - Troba la distribució d'estats estable si existeix.

# %%
# np.linalg.solve(M, X)

# %% [markdown]
# # Referències
#
# - <a id='img_FaXToR'></a> Takis Konstantopoulos, **2019**. *Stochastic Processes I*

# %% [markdown]
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
