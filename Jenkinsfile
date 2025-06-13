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
                echo "Lancement des tests Pytest avec couverture"
                sh '''
                    . venv/bin/activate && \
                    pytest --cov=app --cov-report=term-missing --cov-report=html
                '''
            }

            // Optionnel : Archive le rapport HTML pour consultation dans Jenkins
            post {
                always {
                    archiveArtifacts artifacts: 'htmlcov/**', fingerprint: true
                }
            }
        }
    }

    post {
        always {
            echo "Fin du pipeline"
        }
    }
}
