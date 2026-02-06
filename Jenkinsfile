pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: ''
            }
        }

        stage('Build') {
            steps {
                echo 'Building...'
                bat 'echo Build completed'
            }
        }

        stage('Run Program') {
            steps {
                bat 'star_pattern.py'
            }
        }

    }
}

