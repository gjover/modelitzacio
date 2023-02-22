## Modelització

[![Issues][Issues_badge]][Issues] [![mybinder][Binder_badge]][Binder] [![License: GPL v3][GPL3_badge]][GPL3] [![License: FDL 1.3][GFDL_badge]][GFDL]

Presentacions de la part de modelació de l'assignatura Modelització i Simulació.

Per visualitzar els notebooks com a presentacions, feu servir rise.
Podeu crear un entorn conda fent servir l'arxiu environment.yml que trobareu al directori binder o directament accedint a binder.

## Instal·lació

Si teniu instal·lat conda, podeu crear un entorn virtual per correr el jupyter notebook. Aquest fa servir [RISE](https://rise.readthedocs.io/en/stable).


```
git clone https://github.com/gjover/modelitzacio.git
cd modelitzacio/binder
conda env create -f environment.yml
source postBuild
```

## Feedback

Per qualsevol dubte o comentari, [obriu si us plau un issue a github][Issues]


[Issues]: https://github.com/gjover/modelitzacio/issues
[Issues_badge]: http://img.shields.io/github/issues/gjover/modelitzacio.svg
[Binder]: https://mybinder.org/v2/gh/gjover/modelitzacio.git/main?filepath=notebooks
[Binder_badge]: https://mybinder.org/badge_logo.svg
[GPL3]: https://www.gnu.org/licenses/gpl-3.0
[GPL3_badge]: https://img.shields.io/badge/License-GPLv3-blue.svg
[GFDL]: https://www.gnu.org/licenses/fdl-1.3
[GFDL_badge]: https://img.shields.io/badge/License-FDL_v1.3-blue.svg