pipeline {
    agent {
        dockerContainer {
            image 'python:3.11'
        }
    }

    stages {
        stage('Check Python') {
            steps {
                sh 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip install --upgrade pip
                if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                '''
            }
        }

        stage('Run App') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
