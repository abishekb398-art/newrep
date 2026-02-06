pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Build step (No build needed for Python)'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests (if any)'
            }
        }

        stage('Run Program') {
            steps {
                echo 'Running Python file'
                sh 'star_pattern.py'
            }
        }

    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
