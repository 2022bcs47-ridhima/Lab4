pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt || echo "pip not available"'
            }
        }

        stage('Run Code') {
            steps {
                sh 'python3 main.py || echo "No main.py found"'
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
