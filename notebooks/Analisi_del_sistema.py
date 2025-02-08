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
# ## Formulació del problema
# ## i anàlisis del sistema 

# %% [markdown] slideshow={"slide_type": "notes"}
# - L'objecte dels models és resoldre problemes
# - La modelització comença acotant el problema

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Formulació del problema
# - Àmbit d'estudi
# - Objectiu que es busca
#     - Precisió de l'estudi

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Àmbit d'estudi

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Acotar l'abast de l'objecte d'estudi

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Revisar el context present, passat i futur

# %% [markdown] slideshow={"slide_type": "notes"}
# - Exemples: Guerra de preus, dimensionat d'un aljub, propagació d'una malaltia.
# - Què, perquè, on, quan, qui, exclusions i primeres assumpcions.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Objectiu que es busca

# %% [markdown] slideshow={"slide_type": "fragment"}
# - **S**pecific
# - **M**easurable
# - **A**ssignable
# - **R**ealistic
# - **T**ime-bound

# %% [markdown]
# - Específic: Sobre un aspecte molt concret i acotat.
# - Mesurable: El nivell de millora ha de ser mesurable.
# - Assignable: Les responsabilitats han d'estar ben definides.
# - Realista: L'abast dels objectius ha de ser possible amb els recursos disponibles.
# - Acotat temporalment: L'evolució temporal del desenvolupament i els resultats esperats ha d'estar ben definit.

# %% [markdown] slideshow={"slide_type": "fragment"}
# ### Precisió de l'estudi

# %% [markdown] slideshow={"slide_type": "notes"}
# - És un atribut dels objectius, però d'especial importància
# - Cal establir un criteri de qualitat per verificar el model

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Anàlisis del sistema
# - Context
# - Factors i esdeveniments mesurables
# - Relacions, comportament i estats

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Context
# - Espacial
# - Temporal
# - Sistemàtic
# - Econòmic
# - Casos d'ús
# - Afectació
# - Personal

# %% [markdown] slideshow={"slide_type": "notes"}
# - Partint de la definició dels objectius i del seu àmbit podem començar a identificar el sistema i el seu context
# - Fer assumpcions sobre els límits del context per acotar-lo

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Factors i esdeveniments mesurables
# - Identificar els factors més rellevants
#     - Recerca de coneixements previs
#     - Mantenir un model senzill
#     - Identificar unitats i magnituds

# %% [markdown] slideshow={"slide_type": "notes"}
# - Triarem factors que a priori afectaran més al resultat
#   - Posteriorment analitzarem la sensibilitat del model
# - En el cicle de modelització podem afegir o eliminar factors

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Observem la realitat
# - Documentar-se i cercar coneixements previs de sistemes similars
# - Cercar fonts de dades rellevants
# - Mesurar els factors, el seu canvi i com afecten els uns als altres

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Relacions, comportament i estats
# - Agrupar i relacionar factors
# - Identificar relacions i comportament dels factors
# - Identificar estats i esdeveniments

# %% [markdown] slideshow={"slide_type": "notes"}
# - Podem agrupar factors per subsistema o per categories
# - Hem d'identificar relacions entre factors i comportaments que després modelitzarem
# - Alguns comportaments poden dependre de l'estat del sistema
# - Si el sistema canvia d'estat, hem d'identificar els esdeveniments i transicions
#
# - En aquest procés d'anàlisi poden sortir nous factors que hem d'avaluar i relacionar

# %% [markdown] slideshow={"slide_type": "slide"}
#  

# %% [markdown] slideshow={"slide_type": "skip"}
# # Bibliografia
#
# - <a id='bib_Edwards'></a> Edwards, D., **2001**. *Guide to mathematical modelling*. Palgrave, Basingstoke.

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
