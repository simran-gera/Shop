pipeline {
    agent any
    stages {
    stage("Compile") {
    steps {
        echo "Python compilation done" 
    }
    }
    stage("Unit test") {
    steps {
        sh "python test.py" 
    }
    }
    }
   }
