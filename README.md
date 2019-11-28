# get_steps
Tool for getting steps data from a MongoDB Database

To deploy this function into AWS you have to follow below steps:

Create the function in AWS Portal or AWS SDK command line

Name the function as get_steps(Because that's put as a variable name in Makefile)

pip install --target . pymongo bson

Then run the command `make` in direcory. It creates a zip file outside the directory

After that you run `make deploy` at the same directory. This command uploads the zip to S3 and deploys the function from S3 to AWS lambda.
