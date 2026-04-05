pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // This pulls your code from the GitHub repo you configured
                checkout scm
            }
        }

        stage('Check Environment') {
            steps {
                // Verifies Python is installed on your RHEL VM
                sh 'python3 --version'
            }
        }

        stage('Run Calculator') {
            steps {
                // Executes the script
                sh 'python3 calculator.py'
            }
        }
    }
    
    post {
        always {
            echo 'Build Finished!'
        }
    }
}
