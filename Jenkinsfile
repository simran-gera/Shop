pipeline { 
  agent any stages 
  { 
    stage("Compile") 
    { steps 
     { //pip install requirements.txt 
       echo "Python compilation done" 
     } 
    } 
    stage("Unit test") 
    { 
      steps 
      { 
        sh "python test.py" 
      }
    } 
  } 
} 
