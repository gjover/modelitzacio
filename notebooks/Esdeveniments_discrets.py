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

# %% [markdown] id="f3ef8ea1"
# # Simulació
#

# %% [markdown] id="51bd06c5"
# - La realitat sol estar formada per sistemes complexos
# - Els sistemes senzills es poden modelitzar analíticament
# - Els més complexos pot caldre simular-los numèricament per estudiar el seu comportament.
# - Els sistemes els podem classificar amb tres categories:
#     - Estàtic - Dinàmic
#     - Deterministic - Estocàstic
#     - Continus - Discret
# - Per estudiar el comportament de sistemes discrets, dinàmics i estocàstics farem servir simulacions d'esdeveniments discrets (DES)

# %% [markdown] id="d64724ca"
# ## Simulació d'esdeveniments discrets (DES)

# %% [markdown] id="d8053f1d"
# - Rellotge de simulació
#     - Marca l'instant de tir de cada esdeveniment
# - Entitats
#     - Atributs
#     - Els estats de les entitats conformen l'estat del sistema
#     - Processos
#         - Generen canvis d'estat
# - Esdeveniments
#     - Canvis d'estat del sistema
# - Recursos
#     - Alguns processos generen o consumeixen recursos
# - Cues
#     - La limitació de recursos generen cues

# %% [markdown] id="d1eea48b"
# ### Rellotge de simulació

# %% [markdown] id="cbf1a54c"
# - Se solen donar dues implementacions: fixed-increment i next-event
#     - Fixed-increment: s'actualitza l'estat a cada increment processant l'esdeveniment del darrer increment
#     - Next-event: es registra el temps quan ocorreran esdeveniments

# %% [markdown] id="1ed1da57"
# - Cada esdeveniment inicia un o diversos processos
# - Aquests processos modifiquen el sistema i introdueixen esdeveniments

# %% [markdown] id="06923a9a"
# ### Estructura de la SED (DES)

# %% [markdown] id="0f653296"
# - Inicialització
#
#     - Init clock
#     - Init events
#     - Init system
#         - Init entities
#         - Init statistics
#
#  - Loop
#      - Trigger next event
#      - Process event
#      - Update system
#      - Update statistics
#      - Generate future events
#
#  - Report

# %% [markdown] id="213fc176"
# ## Cua FIFO

# %% [markdown] id="a3d02dad"
# - Tenim un servei de venda per taquilla que triga una mitjana de 10s en atendre a cada client
# - Tenim un fluix d'arribada d'un client cada 8s
# - Assumim que la cua està buida per t=0

# %% colab={"base_uri": "https://localhost:8080/"} id="a9vAks0baSVw" executionInfo={"status": "ok", "timestamp": 1742202171412, "user_tz": -60, "elapsed": 11120, "user": {"displayName": "Gabriel JM", "userId": "04913946655420947744"}} outputId="9dc4be82-bf5d-488d-ea50-8700cda84330"
# %pip install simpy

# %% id="0ae2664c"
import simpy
import numpy as np
import pandas as pd


# %% id="0fc3400b"
def venda(env, taquilla, cua):
    """
    Simula el temps de venda
    """
    with taquilla.request() as req:
        yield req
        temps = np.random.exponential(10)
        print("venda", env.now, "trigarà", temps)
        yield env.timeout(temps)
        cua.loc[env.now] = cua.iloc[-1].pers - 1
        print(env.now, "Següent!")


# %% id="502eb5ce"
def simulacio(env, n_taquilles, cua):
    """
    Inicialitza la simulació
    """
    # La taquilla és un recurs limitat
    taquilla = simpy.Resource(env, capacity=n_taquilles)

    # La cua comença buida
    cua.loc[0] = 0

    # Comença l'arribada de clients
    while True:
        temps = np.random.exponential(8)
        yield env.timeout(temps)
        print("arribat", env.now)
        cua.loc[env.now] = cua.iloc[-1].pers + 1
        v = venda(env, taquilla, cua)
        env.process(v)



# %% [markdown] id="ee4ce93e"
# ### Llaç de simulació

# %% colab={"base_uri": "https://localhost:8080/"} id="41050a5b" executionInfo={"status": "ok", "timestamp": 1742202768624, "user_tz": -60, "elapsed": 44, "user": {"displayName": "Gabriel JM", "userId": "04913946655420947744"}} outputId="7a1ebbd5-337b-4dd8-80c8-821f381b6549"
env = simpy.Environment()
n_taquilles = 2

# Guardem l'evolució de la cua
cua = pd.DataFrame(columns=['pers'])

env.process(simulacio(env, n_taquilles, cua))
env.run(until=300)

# %% [markdown] id="e36bce14"
# ### Report

# %% colab={"base_uri": "https://localhost:8080/", "height": 363} id="5451d542" executionInfo={"status": "ok", "timestamp": 1742202425516, "user_tz": -60, "elapsed": 55, "user": {"displayName": "Gabriel JM", "userId": "04913946655420947744"}} outputId="f4eec87a-0b5e-43ae-97d2-276dcfab8787"
cua.head(10)

# %% colab={"base_uri": "https://localhost:8080/", "height": 447} id="f1330dac" executionInfo={"status": "ok", "timestamp": 1742202771777, "user_tz": -60, "elapsed": 399, "user": {"displayName": "Gabriel JM", "userId": "04913946655420947744"}} outputId="fc7c651e-e05b-429f-f54d-00991b5b7d4a"
cua.plot()

# %% [markdown] id="03756f77"
# Per estimar el rendiment del nostre sistema podem mesurar diferents paràmetres
#
# - Quina és la llargària mitjana de la cua?
# - Quin és el temps mitjà fent cua?
# - Quin percentatge del temps estan les taquilles ocupades?
#

# %% [markdown] id="d4826dff"
# - La simulació és una composició d'esdeveniments estocàstics
#     - El resultat té una component aleatòria
#     - Cal repetir la simulació prou cops per obtenir un resultat estable
#     - La distribució de resultats ens pot donar molta informació

# %% [markdown] id="b62a14be"
# ## Altres exemples

# %% [markdown] id="d7601808"
# - [Transport](https://colab.research.google.com/github/vitostamatti/discrete-event-simulation-simpy/blob/main/notebooks/02-transportation_examples.ipynb)
# - [Fluix d'entitats](https://colab.research.google.com/github/vitostamatti/discrete-event-simulation-simpy/blob/main/notebooks/03-entity_flow_examples.ipynb)
# - [Benzinera](https://colab.research.google.com/github/vitostamatti/discrete-event-simulation-simpy/blob/main/notebooks/04-fuel_station_example.ipynb)

# %% [markdown] id="d928e593"
# # Bibliografia
#
#
# - <a id='bib_Law'></a> Law, Averill M., **2015**. *Simulation modeling and analysis*. Mcgraw-Hill.
# - <a id='bib_Law'></a> Cantot, Pascal, **2011**. *Simulation and Modeling of Systems of Systems*. John Wiley & Sons.
# - <a id='bib_Law'></a> Kroese, Dirk P., **2011**. *Handbook of Monte Carlo Methods*. John Wiley & Sons.

# %% [markdown] id="c105f73a"
# # Referències
#
# - [SimPy](https://simpy.readthedocs.io)
# - [Discrete Event Simulation with Python](https://github.com/vitostamatti/discrete-event-simulation-python/)

# %% [markdown] id="95e9c092"
# Copyright (C) 2025 Gabriel Jover Mañas
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
