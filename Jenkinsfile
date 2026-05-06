pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    stages {
        stage('Run App') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
