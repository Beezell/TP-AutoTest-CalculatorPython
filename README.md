
# Python Calculator – Tests Automatisés & Intégration Continue

Ce projet s'inscrit dans le cadre du TP2  Automatisation des tests avec Pytest & Jenkins et du TP 3 : Automatisation des tests avec Selenium.

Il s'agit d'une application Python simple de calculatrice, accompagnée d'une suite de tests automatisés et d'un pipeline d'intégration continue avec Jenkins. 

## Objectifs pédagogiques

* Développer des tests unitaires avec `pytest`
* Mettre en place des tests fonctionnels avec Selenium
* Générer des rapports de couverture et de tests en HTML
* Définir un pipeline CI avec Jenkins déclenché automatiquement à chaque modification du code

## Fonctionnalités de la calculatrice

L'application fournit les opérations mathématiques suivantes :

* `addition(a, b)`
* `soustraction(a, b)`
* `multiplication(a, b)`
* `division(a, b)` (avec gestion de la division par zéro)
* `puissance(a, b)`
* `modulo(a, b)` (avec gestion du modulo par zéro)
* `calcul_complexe(a, b)` (fonction fictive pour illustrer l’utilisation de `mock`)

## Tests automatisés

### Tests unitaires

Réalisés avec `pytest`, les tests unitaires couvrent :

* Les cas standard de chaque fonction
* Les cas d’erreur (division par zéro, modulo par zéro, etc.)
* L'utilisation de `mock` pour tester des comportements isolés

### Tests fonctionnels

Les tests fonctionnels utilisent Selenium pour interagir avec l’interface web de la calculatrice développée avec Flask.

## Intégration continue (Jenkins)

Un pipeline Jenkins est défini dans le fichier `Jenkinsfile`. Il comprend les étapes suivantes :

1. **Préparation** : création d’un environnement virtuel Python et installation des dépendances
2. **Build et lancement de l'application** : exécution de l’application Flask en arrière-plan
3. **Tests unitaires** : exécution avec `pytest` et génération d’un rapport de couverture
4. **Tests fonctionnels** : lancement des tests Selenium et génération d’un rapport HTML
5. **Archivage des rapports** : les rapports sont enregistrés dans Jenkins comme artefacts
6. **Nettoyage** : arrêt du serveur Flask

Le pipeline est automatiquement déclenché à chaque `git push` via un webhook GitHub.

## Structure du projet

```
├── app/   
│   └──  calculatrice.py
├── drivers/
│   └── chromedriver
├── reports/
│   └── selenium_report.html
├── tests/
│   ├── test_calculatrice.py
│   └── test_functional_selenium.py
├── web/
│   └── app_web.py
├── requirements.txt
├── Jenkinsfile
├── pytest.ini
└── README.md
```

### Installation locale et exécution des tests

```bash
git clone https://github.com/Beezell/TP-AutoTest-CalculatorPython.git
cd TP-AutoTest-CalculatorPython
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest --cov=app --cov-report=term-missing --cov-report=html
```
