pipeline {
    agent any
    triggers {
        pollSCM('* * * * *') //runs this pipeline on every commit
        cron('25 14 * * *') 
    }
    stages {
    stage("Compile") {
    steps {
        echo "Python compilation done" 
    }
    }
    stage("Unit test") {
    steps {
        sh "python3 test.py" 
    }
    }
    stage('nightly') {
       when {
           //runs only when the expression evaluates to true
           expression {
               //will return true when the build runs via cron trigger 
                   return Calendar.instance.get(Calendar.HOUR_OF_DAY) in 23
               }
            }

            steps {
                echo "Running the nightly stage only at night..."
            }
        }
     }
    }
