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

        stage('Tests') {
            steps {
                echo "Lancement des tests Pytest"
                sh '. venv/bin/activate && pytest --cov=app'
            }
        }
    }

    post {
        always {
            echo "Fin du pipeline"
        }
    }
}
