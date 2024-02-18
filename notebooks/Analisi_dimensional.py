# ---
# jupyter:
#   jupytext:
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] hideCode=false hidePrompt=false slideshow={"slide_type": "slide"}
# # Analisi dimensional

# %% [markdown] hideCode=false hidePrompt=false slideshow={"slide_type": "slide"}
# ### Anàlisi dimensional
# - En sistema internacional defineix 7 unitats de mesura (s, m, kg, A, K, mol, cd)
# - La resta de magnituds físiques es poden expressar en termes d'aquestes unitats
# - Qualsevol magnitud la podem descompondre en les seves dimensions
# - Per simplicitat treballarem amb T, L i M

# %% [markdown] slideshow={"slide_type": "notes"}
# - Podem repassar el canvi d'unitats
# - Recordem l'accident del mars climate orbiter a 1999

# %% [markdown] slideshow={"slide_type": "subslide"}
# [àrea] = $L^2$
#
# [velocitat] = $L T^{-1}$
#
# [densitat] = $M L^{-3}$
#
# [angle] = $L L^{-1}$ = 1

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Qualsevol model que escriguem ha de ser consistent
# - Una avaluació bàsica de la seva consistència és l'anàlisi dimensional
# - Les dimensions dels membres de l'equació han de ser iguals
# - Les dimensions dels factors d'una suma han de ser iguals
# - Les variables de les funcions trascendents han de ser adimensionals

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Exemple: Atracció de la terra
# - Newton va descriure que l'atracció de dos cossos celestials és proporcional a les seves masses
#     i inversament proporcional al quadrat de la seva distància
# $$F \propto \frac{M_1 M_2}{r^2}$$
#
# $[F] = [MLT^{-2}]$
#
# $\left[ \frac{M_1 M_2}{r^2}  \right] = [M^2 L^{-2}]$

# %% [markdown] slideshow={"slide_type": "subslide"}
# - L'expressió de la llei de gravitació universal és
# $$F = G \frac{M_1 M_2}{r^2}$$
#
# $[F] = [MLT^{-2}] = [G] \left[ \frac{M_1 M_2}{r^2}  \right] = [G][M^2 L^{-2}]$
#
# $[G] = [M^{-1} L^3 T^{-2} ]$

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Exemple: oscil·lació del pèndol
# - L'oscil·lació d'un pèndol es pot expressar com:
#
# $$\frac{d\theta}{dt} = \omega B cos(\omega t)$$
#
# - On $t$ es el temps i $\theta$ es l'angle

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Si fem l'anàlisi dimensional de l'expressió obtindrem
# $$
# \begin{align}
# \left[\frac{d\theta}{dt}\right] = [T^{-1}] \qquad [\omega t] & = 1 \qquad & [\omega B] & = [T^{-1}] \\
# [\omega] & = [T^{-1}] \qquad & [B] & = 1 \\
# \end{align}
# $$

# %% [markdown] slideshow={"slide_type": "slide"}
# - Sovint, l'anàlisi dimensional ens pot servir per corregir o descartar una formulació
# - També ens pot servir per identificar les relacions entre paràmetres

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Considerem el pèndol i cerquem el seu període $p$
# - Identifiquem que la seva oscil·lació depèn de la llargària del pèndol $l$, la seva massa $m$ i la força de la gravetat $g$
#
# $$[p] = [T] = [l^a m^b g^c] = [L^a M^b (L T^{-2})^c]$$

# %% [markdown] slideshow={"slide_type": "subslide"}
# $$
# \begin{align}
# T&: &-2c & = 1 \\
# L&: &a + c & = 0 \\
# M&: &b & = 0 \\
# \end{align}
# $$
#
# $$[p] = [l^{1/2} g^{-1/2}] $$
#
# - Obtenint que $p \propto \sqrt{l/g}$

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Podem millorar el nostre model afegint el fregament de l'aire $R$ i l'angle $\theta$
#
# $$[p] = [T] = [l^a m^b g^c R^d \theta^e] = [L^a M^b (LT^{-2})^c (M L T^{-2})^d 1^e]$$

# %% [markdown] slideshow={"slide_type": "subslide"}
# $$
# \begin{align}
# T&: &-2c -2d & = 1 \\
# L&: &a + c + d& = 0 \\
# M&: &b + d & = 0 \\
# \end{align}
# $$
#
# - $e$ pot tindre qualsevol valor
# - Ens sobra un grau de llibertat que ens permet expressar la relació en funció de $d$

# %% [markdown] slideshow={"slide_type": "subslide"}
# $$
# \begin{align}
# b & = -d \\
# c & = -d - 1/2 \\
# a & = 1/2 \\
# \end{align}
# $$
#
# $$[p] = [l^{1/2} m^{-d} g^{-1/2 - d} R^d \theta^e]$$
#
# - Obtenint que $p \propto \sqrt{l/g} \cdot f\left(\frac{R}{mg}, \theta \right)$

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Si expressem la solució en funció de $c$
# $$
# \begin{align}
# d & = -c - 1/2 \\
# b & = c + 1/2 \\
# a & = 1/2 \\
# \end{align}
# $$
#
# $$[p] = [l^{1/2} m^{1/2 + c} g^{c} R^{-1/2 -c} \theta^e]$$
#
# - Obtenint que $p \propto \sqrt{ml/R} \cdot f\left(\frac{R}{mg}, \theta \right)$

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Podem interpretar que el període d'oscil·lació té un factor que depèn de la gravetat $\sqrt{l/g}$
# - Té un factor d'esmorteïment que depèn de R $\sqrt{ml/R}$
# - I altres factors adimensionals com $\theta$ i $\frac{R}{mg}$

# %% [markdown] hideCode=false hidePrompt=false slideshow={"slide_type": "skip"}
# # Bibliografia
#
# - <a id='bib_Edwards'></a> Edwards, D., **2001**. *Guide to mathematical modelling*. Palgrave, Basingstoke.
# - <a id='bib_'></a> Dym, Clive L., **2004**. Principles of mathematical modeling. Elsevier Academic Press.
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
