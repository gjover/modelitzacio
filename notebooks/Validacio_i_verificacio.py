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
# # Modelització
# ## Validació i verificació

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Per tancar el cicle de modelització hem de validar, verificar el nostre model i interpretar els resultats
# - Per una banda, hem de verificar que els nostres càlculs representen el model que hem descrit
# - Per altra banda, hem de validar que el model es correspon amb les dades

# %% [markdown] slideshow={"slide_type": "subslide"}
# <center></br>
# <img src=./static/cicle_modelitzacio_VV.png width=75%>
# </center>

# %% slideshow={"slide_type": "skip"}
import numpy as np
from scipy import optimize
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Verificar
# - Determinar en quina mesura el resultat del càlcul que hem fet es correspon amb el model que hem dissenyat

# %% [markdown] slideshow={"slide_type": "notes"}
# - Durant la resolució del model solem verificar que el resultat és l'esperat
# - En algunes simulacions haurem de determinar l'incertesa numèrica del càlcul
# - Quan desenvolupem codi podem escriure tests funcionals per verificar els diferents mòduls que componen el programari.

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Verificació del codi
#     - Comprovar que el codi funciona com s'espera
#     - Control de qualitat del codi
#     - Testatge funcional

# %% [markdown] slideshow={"slide_type": "notes"}
# - Comprovar que el codi funciona com s'ha dissenyat
# - Comprovar que és repetible i estable
#     - Per tant, els tests han de ser repetibles

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Verificació del càlcul
#     - Quantificar l'error numèric
#     - Comprovar la convergència de la simulació
#     - Verificació de dades d'entrada i sortida

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Validar
# - Estimar el nivell de precisió amb què el model representa la realitat al context modelat.
#     - Avaluar l'error del model
# - Quantificar el nivell de confiança en el resultat del model
# - El criteri per validar el model és el definit a l'inici del cicle de modelització

# %% [markdown] slideshow={"slide_type": "notes"}
# - Hem d'estimar l'error del model, la difèrencia entre el valor mesurat i la predicció del model
# - A partir de les incerteses de les mesures i les incerteses del resultat del model avaluarem aquest error
# - Si l'error del model és superior al necessari, haurem de revisar el model o les mesures

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Error experimental i de simulació
# - L'error de les dades experimentals es compon dels errors estadístics i sistemàtics
#
# $$\delta_D = \epsilon_i + \beta_j$$
#
# - A les simulacions podem distingir els errors del model, els numèrics i els dels paramètrics
#
# $$\delta_S = \delta_m +  \delta_n + \delta_p$$

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Els errors del model provenen de les aproximacions i assumpcions fetes
# - Els errors numèrics provenen de la solució numèrica dels càlculs
# - Els errors paramètrics provenen de l'estimació dels paràmetres

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Les incerteses degudes als errors numèrics i paramètrics els podem estimar
# - No podem calcular o avaluar directament les incerteses degudes al model
# - Podem avaluar la discrepància del model $E$ indirectament mitjançant els valors de les mesures i la simulació
#
# $$D + E = S$$

# %% hideCode=true hidePrompt=false slideshow={"slide_type": "subslide"}
d = np.random.normal(np.zeros(100000) + 2.8)
s = np.random.normal(np.zeros(100000) + 3.6) * 1.5
plt.hist(s, bins=40)
plt.hist(d, bins=40)
plt.legend(["simulació", "dades"])
l = plt.plot([2, 2], [0, 10000], [2.8, 3.6 * 1.5], [8000, 8000], "r")

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Discrepància experiment i model
# - El valor real i els errors absoluts de la mesura i la simulació són desconeguts
# - Podem relacionar els errors amb la discrepància del model com
#
# $$E = S - D = \delta_S - \delta_D = \delta_m +  \delta_n + \delta_p - \delta_D$$

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Indirectament podem obtenir que l'error del model és
#
# $$\delta_m = E - (\delta_n + \delta_p - \delta_D)$$
#
# - Que ens pot servir per a avaluar la validesa del model

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Fent una estimació dels errors mitjançant les incerteses podem construir l'incertesa de la validació
#
# $$u_v = \sqrt{u_n^2 + u_p^2 + u_D^2}$$
#
# - Podem interpretar que $E$ és una estimació de l'error del model i $u_v$ l'incertesa d'aquesta estimació
#
# $$E \pm u_v$$
#
# - Com a altres incerteses, podem expandir l'incertesa $u_v$ per diferents nivells de confiança

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Presentació dels resultats
# - Un cop tenim un model satisfactori, hem d'interpretar el resultat
# - Redactarem els resultats i conclusions

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Introducció
# - Fem una breu introducció per al públic general explicant el problema i els objectius
# - Una breu explicació del mètode
# - Les conclusions més destacades

# %% [markdown] slideshow={"slide_type": "notes"}
# - Expliquem:
#     - Perquè, com i resultat principal
# - En un petit resum hem d'atraure el lector perquè el motiu de l'estudi i les seves conclusións són d'interès
# - Pensa que necessita saber el lector i que és el que ja sap.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Informe
# - Desenvolupem amb detall el problema, els objectius i el context
# - Expliquem l'anàlisi del sistema
# - Defensem argumentadament les assumpcions que hem fet i les confirmem amb dades o referències

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Expliquem el desenvolupament del model, la formulació i resolució
#     - Aquesta és la part central de l'informe
# - Presentem com hem verificat i validat el model
# - Analitzem els resultats i extraiem conclusions
#     - Podem fer una anàlisi crític del model indicant les seves limitacions o context de validesa

# %% [markdown] slideshow={"slide_type": "notes"}
# - Després es poden afegir apèndixs amb informació rellevant de l'estudi
# - També és convenient afegir un apartat de referències o bibliografia

# %% [markdown] slideshow={"slide_type": "subslide"}
#  

# %% [markdown] slideshow={"slide_type": "skip"}
# # Bibliografia
#
# - <a id='bib_Edwards'></a> Edwards, D., **2001**. *Guide to mathematical modelling*. Palgrave, Basingstoke.
# - <a id='bib_Schaller'></a>Schaller, Ch., **2004**. *Concepts of Model Verification and Validation*. Los Alamos N.L.
# - <a id='bib_Coleman'></a> Coleman, Hugh W. & Steele, W. Glenn, **2018**. *Experimentation, validation, and uncertainty analysis for engineers*. Wiley.

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
