pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Code') {
            steps {
                sh 'python main.py || echo "No main.py found"'
            }
        }

        stage('Show Metrics') {
            steps {
                sh 'cat metrics.json'
            }
        }

        stage('Print Details') {
            steps {
                echo "Name: Ridhima"
                echo "Roll No: 2022BCS0047"
            }
        }
    }
}
