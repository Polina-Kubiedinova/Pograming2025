pipeline {
   options{timestamps()}

   agent none
   stages{
      stage('Check scm'){
         agent any
         steps{
            checkout scm
         }
      }
      stage('Build'){
         steps{
            echo "Building ...${BUILD_NUMBER}"
            echo "Build complited"
         }
      }
      stage('Test'){
         agent any
         steps{
            sh 'pip install unittest-xml-reporting'
            sh 'python3 test.py'
         }
         post{
            always {
               junit 'test-reports/*.xml'
            }
            success{
               echo "Application testing successfully complited"
            }
            failure{
               echo "Ooops!!! Tests failed"
            }
         }
      }
   }
}