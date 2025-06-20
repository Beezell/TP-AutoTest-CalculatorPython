pipeline {
    agent any

    stages {
        stage('Préparation') {
            steps {
                echo "Nettoyage et installation de l'environnement"
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Lancer l\'application') {
            steps {
                echo "Démarrage du serveur Flask en arrière-plan"
                sh '. venv/bin/activate && nohup python web/app_web.py &'
                // Petit sleep pour laisser le temps au serveur de démarrer
                sh 'sleep 5'
            }
        }

        stage('Tests Unitaires') {
            steps {
                echo "Lancement des tests Pytest avec couverture"
                sh '. venv/bin/activate && pytest --cov=app --cov-report=term-missing --cov-report=html'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'htmlcov/**', fingerprint: true
                }
            }
        }

        stage('Tests Fonctionnels Selenium') {
            steps {
                echo "Lancement des tests Selenium"
                sh '. venv/bin/activate && pytest tests/test_functional_selenium.py --html=reports/selenium_report.html'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'reports/selenium_report.html', fingerprint: true
                }
            }
        }

        stage('Arrêt serveur') {
            steps {
                echo "Arrêt du serveur Flask"
                // Exemple: kill la tâche python web/app_web.py en cours
                sh "pkill -f 'python web/app_web.py' || true"
            }
        }
    }

    post {
        always {
            echo "Fin du pipeline"
        }
    }
}
