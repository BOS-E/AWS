1. using_lambda_layer
    - put the code that you want in the layer inside 'python' folder and zip this folder.
    - create a lambda layer with that zip.
    - attach the layer to your lambda
    - import the functions to your lambda code.
2. lambda zip (not layer) with dependencies
    - pip install requests -t ./package     
    - my_lambda.zip      # zip has lambda fn py file and dependencies all together eg:
        │── lambda_function.py   # Your Lambda function file
        │── requests/            # Requests library folder
        │── urllib3/             


 
