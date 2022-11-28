<h3 align="center">
    <img alt="Logo" title="#logo" width="118px" src="/assets/16007798203635_P9.png">
    <br>
</h3>


# OpenClassrooms Projet P11

- [Objectif](#obj)
- [Compétences](#competences)
- [Technologies](#techs)
- [Requirements](#reqs)
- [Architecture](#architecture)
- [Configuration locale](#localconfig)
- [Présentation](#presentation)

<a id="obj"></a>
## Objectif

Güdlft est une société qui a créé une plateforme numérique pour coordonner les compétitions de force (deadlifting, strongman) en Amérique du Nord et en Australie. L'objectif de ce projet est de créer une version plus légère (et moins coûteuse) de leur plateforme actuelle pour les organisateurs régionaux (repository GitHub : [gudlift-registration](https://github.com/OpenClassrooms-Student-Center/Python_Testing)). L'objectif de l'application est de rationaliser la gestion des compétitions entre les clubs (hébergement, inscriptions, frais et administration).

<a id="competences"></a>
## Compétences acquises
- Configurer un environnement Python
- Gérer les erreurs et les exceptions en Python
- Implémentez une suite de tests Python
- Debugger le code d’une application Python

<a id="techs"></a>
## Technologies Utilisées
- [Python3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [HTML](https://developer.mozilla.org/fr/docs/Web/HTML)
- [Pytest](https://docs.pytest.org/)
- [Coverage](https://coverage.readthedocs.io/)
- [Locust](https://locust.io/)

<a id="reqs"></a>
## Requirements
- flask
- pytest
- coverage
- locust

<a id="architecture"></a>
## Architecture et répertoires
```
Project
├── templates              \
├── clubs.json              \__ application Flask
├── competitions.json       /
├── server.py              /
│
├── tests : répertoire contenant les tests de notre application       \
│   ├── integration_tests                                              \
│   ├── unit_tests                                                      \__ tests et performances
│   ├── conftest.py : fichier de configuration des tests (fixtures)     /
├── locustfile.py : tests de performances                              /
│
|── requirements.txt
|── documents
```

<a id="localconfig"></a>
## Configuration locale
## Installation

### 1. Récupération du projet sur votre machine locale

Clonez le repository sur votre machine.

```bash
git clone https://github.com/GDSDC/OpenclassroomsProject-P11.git
```

Accédez au répertoire cloné.
```bash
cd OpenclassroomsProject-P11
```

### 2. Création d'un environnement virtuel 
Créez l'environnement virtuel env.
```bash
python3 -m venv env
```

### 3. Activation et installation de votre environnement virtuel 

Activez votre environnement virtuel env nouvellement créé.
```bash
source env/bin/activate
```

Installez les paquets présents dans la liste requirements.txt.
```bash
pip install -r requirements.txt
```

## Utilisation

Renseignez l'application flask en tant que variable d'environnement.
```bash
export FLASK_APP=server.py
```
Démarrez le serveur local.
```bash
python -m flask run
```


<a id="presentation"></a>
### Présentation

[<img alt="presentation" width="480px" src="/assets/presentation.png">](https://docs.google.com/presentation/d/e/2PACX-1vSlazmtFTBkbbzs9-3_QCV4yDbV1pOk_sl8MkRX5JzWPfa1szjHkOkB92EoJT-JzfEIn66POXN_XbGo/pub?start=true&loop=false&delayms=5000)