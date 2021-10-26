pipeline {
    agent any
    triggers {
        pollSCM('* * * * *') //runs this pipeline on every commit
        cron('30 23 * * *') //run at 23:30:00 
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
               //will return true when the build runs via cron trigger (also when there is a commit at night between 23:00 and 23:59)
                   return Calendar.instance.get(Calendar.HOUR_OF_DAY) in 23
               }
            }

            steps {
                echo "Running the nightly stage only at night..."
            }
        }
    }
   }
