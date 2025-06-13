
# Python Calculator – Tests Automatisés & Intégration Continue

Dans le cadre du TP "Automatisation des tests avec Pytest & Jenkins".

Projet Python simple de calculatrice avec :

* Fonctions mathématiques de base
* Tests automatisés avec `pytest`, `pytest-cov`, `mock`
* Intégration continue avec Jenkins (webhook GitHub)

## Fonctionnalités

L'application fournit les fonctions suivantes :

* `addition(a, b)`
* `soustraction(a, b)`
* `multiplication(a, b)`
* `division(a, b)` (gestion division par zéro)
* `puissance(a, b)`
* `modulo(a, b)` (gestion modulo par zéro)
* `calcul_complexe(a, b)` (utilisée pour tests avec `mock`)

## Tests

Tests unitaires avec `pytest` :

* Cas de réussite et cas d'erreur
* Simulation de comportements avec `mock`

Commande locale :

```bash
pytest --cov=app --cov-report=term-missing
```

## Intégration Jenkins

Pipeline défini dans `Jenkinsfile` :

* Création d'un environnement Python
* Installation des dépendances
* Exécution des tests avec couverture
* Rapport HTML de couverture (archivé dans Jenkins)
* Déclenchement automatique à chaque `git push` via webhook

## Structure du projet

```
.
├── app/
│   └── calculatrice.py
├── tests/
│   └── test_calculatrice.py
├── requirements.txt
├── Jenkinsfile
├── pytest.ini
└── README.md
```

## Installation locale

```bash
git clone https://github.com/Beezell/TP-AutoTest-CalculatorPython.git
cd TP-AutoTest-CalculatorPython
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest --cov=app --cov-report=term-missing
```
