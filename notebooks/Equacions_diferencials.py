# ---
# jupyter:
#   jupytext:
#     formats: py:percent,ipynb
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

# %% [markdown] hideCode=false hidePrompt=false slideshow={"slide_type": "slide"}
# # Interpretació d'equacions diferencials

# %% [markdown] hideCode=false hidePrompt=false slideshow={"slide_type": "slide"}
# ### Equacions diferencials
#
# - Molts cops ens trobarem equacions de la forma
#     $$\frac{dy}{dx} = g(x, y)$$
# - Les solucions són sensibles  a les condicions inicials $y(x_0) = y_0$
# - Interpretant y' = g(c, y) com el pendent de la trajectòria del sistema 
# - podem analitzar gràficament el comportament del sistema representant el camp vectorial
# - En aquests gràfics podem identificar regions estables, inestables i tendències del sistema

# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
# Meshgrid 
x, y = np.meshgrid(np.linspace(-5, 5, 10),  
                   np.linspace(-5, 5, 10)) 

# Pendent
yp = y - x**2

# Vectors directors
nor = np.sqrt(yp**2 + 1)
u = 1/nor 
v = yp/nor

# Streamline
plt.streamplot(x,y,u,v, density=[0.5, 1])
plt.title('y\' = y - x^2')
plt.show()

# %%
# Meshgrid 
x, y = np.meshgrid(np.linspace(-5, 5, 10),  
                   np.linspace(-5, 5, 10)) 

# Pendent
yp = -2 * x * y / (1 + x**2)

# Vectors directors
nor = np.sqrt(yp**2 + 1)
u = 1/nor 
v = yp/nor

# Streamline
plt.streamplot(x,y,u,v, density=[0.5, 1])
plt.title('y\' = -2 * x * y / (1 + x^2)')
plt.show()

# %%
# Meshgrid 
x, y = np.meshgrid(np.linspace(-5, 5, 10),  
                   np.linspace(-5, 5, 10)) 

# Pendent
yp = (2 - x) * y + x

# Vectors directors
nor = np.sqrt(yp**2 + 1)
u = 1/nor 
v = yp/nor

# Streamline
plt.streamplot(x,y,u,v, density=[0.5, 1])
plt.title('y\' = (2 - x) * y + x ')
plt.show()

# %%
# Meshgrid 
x, y = np.meshgrid(np.linspace(0, 5, 10),  
                   np.linspace(-0.5, 1.5, 10)) 

# Pendent
yp = 2 * y * (1 - y)

# Vectors directors
nor = np.sqrt(yp**2 + 1)
u = 1/nor 
v = yp/nor

# Streamline
plt.streamplot(x,y,u,v, density=[0.5, 1])
plt.title('y\' = 2 * y * (1 - y)')
plt.show()

# %% [markdown]
# - Hem d'interpretar les regions del gràfic.
# - Podem trobar zones que no tenen sentit per al nostre sistema.

# %% [markdown]
# ### Equacions diferencials autònomes
#
# - Les equacions diferencials de la forma 
#     $$\frac{dy}{dx} = g(y)$$
#   es denominen equacions diferencials autònomes.
# - Analitzant els zeros de g(y) podem avaluar el comportament a les diferents regions .
#
# 1. Els punts y' = 0 seran punts d'equilibri
#     - poden ser estables o inestables
# 2. Identifiquem si el pendent a cada regió és positiva o negativa
# 3. Trobem els punts d'inflexió y'' = 0
# 4. Identifiquem si la tendència a cada regió és creixent o decreixent
# 5. Podem fer scketch aproximat de comportament o representar el camp vectorial
#
# - Aquesta anàlisi ens permet identificar els diferents punts i les regions significatives per al nostre sistema.

# %% [markdown] hideCode=false hidePrompt=false slideshow={"slide_type": "skip"}
# # Bibliografia
#
# - <a id='bib_Edwards'></a> Edwards, D., **2001**. *Guide to mathematical modelling*. Palgrave, Basingstoke.
# - <a id='bib_'></a> Giordano, Frank R., **2014**. A first course in mathematical modeling. Brooks/Cole.
#

# %% [markdown] hideCode=false hidePrompt=false slideshow={"slide_type": "skip"}
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
