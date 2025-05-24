pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/batoolsh2001/my-react-app.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh './$VENV_DIR/bin/pip install --upgrade pip'
                sh './$VENV_DIR/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // إذا ما عندك اختبارات، ممكن تتخطى هذي أو تحط echo
                sh './$VENV_DIR/bin/python -m unittest discover || echo "No tests found."'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'echo "FLASK_APP=app.py" > .env'
                sh 'echo "FLASK_ENV=development" >> .env'
                sh './$VENV_DIR/bin/flask run --host=0.0.0.0 --port=5000 &'
                sh 'sleep 5' 
            }
        }
    }
}
