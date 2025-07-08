# CSA_Project

# Problem Statement:
ABCBooks is rolling out a new web-based application for its book collection to complement its existing book database application. The company has opted for Amazon DynamoDB and a serverless architecture using AWS Lambda for this implementation.

The application is designed to perform four key functions:
1. Display all books in the database to users.
2. Enable users to add or delete database entries.
3. Allow updates to non-key attributes of any book.
4. Secure the application by integrating Amazon Cognito for user authorization.
You are responsible for creating and implementing these functionalities, leveraging Amazon DynamoDB, AWS Lambda, and Amazon API Gateway. The front-end website can be developed using your preferred programming language. The final step will involve securing the application by integrating Amazon Cognito to authorize users.


The books collection application will have the following components:
1. A static front-end written in HTML/JavaScript or in Python hosted on Amazon S3.
2. A serverless backend leveraging Amazon API Gateway, AWS Lambda, and Amazon Cognito.
3. A DynamoDB table for the persistence layer.

An initial data set will be provided to you for the application to use. This initial data set is provided in the books.json file. This sample data can be loaded into Books table in DynamoDB via script.

# Here's how to get this project to work:
1. Clone the Repository
2. Create a DynamoDB table called "Books". Upload the initial data from books.json either one by one or by using AWS CLI.
3. Create Lmabda functions called "getBooks", "addBooks", "updateBook" and "deleteBook". Copy the code from the lmabda_function.py files and paste it into their respective lambda functions.
4. Goto API Gateway on AWS, create an API using REST API protocol and name it "booksAPI".
/
/books
GET
    OPTIONS
    POST
/{id}
    DELETE
    OPTIONS
    PUT
Use this structure for the API.
Next goto Stages in your API Gateway and create a stage. My stage name for this project is "apiDevelopment2". You will need the Invoke URL for the html files.
6. Create a S3 bucket. My bucket name is "mybookbucketnow". Upload all the HTML files and backgorund.jpg to this bucket. Also create a folder called "book_images" to store book cover images in the folder. I added an image called "default.jpg", so if a user does not upload any image, this default image is set as the book cover.
Note: If the html files do not have proper extension name then complete it first. For example: change index.htm to index.html
7. Goto Permissions tab of the bucker and bucket policy and CORS policy for the API.
My bucket policy right now is:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::mybookbucketnow/*"
        },
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::mybookbucketnow/books_images/*"
        }
    ]
}

My CORS policy right now is:
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "PUT"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [],
        "MaxAgeSeconds": 3000
    }
]
You can change these policies according to your need.

7. Goto Properties tab of this bucket and in the last you will see Static website hosting. Enable it and add "index.html" as the index document and as the error document. You can also change it to login form.
8. Goto Cognito and create a user pool. Inside that user pool, create an app client using Single Page application option.
9. Create a user in your user pool and keep it as verified. You can choose how the user can be verified to sign in. You can also take AWS provided login page but I used my own.
10. Next copy paste all the ids from the AWS services to the html files. Delete all the html files from the S3 bucket and then upload the newly edited files to the S3 bucket. Test the lambda functions.


<img src="https://github.com/user-attachments/assets/23b82a3e-3f61-4b44-9c32-de31ca34b004" alt="Image 1" width="300" height="auto">
<img src="https://github.com/user-attachments/assets/80550a10-d373-40cc-9ab7-5c96da67550d" alt="Image 2" width="300" height="auto">
<img src="https://github.com/user-attachments/assets/7d187c53-4a42-43ea-9f6b-9c9060249396" alt="Image 3" width="300" height="auto">
<img src="https://github.com/user-attachments/assets/fa62260a-f95c-473a-af1d-5e7a2c10db7b" alt="Image 4" width="300" height="auto">
<img src="https://github.com/user-attachments/assets/b02db66a-a444-46a4-9401-777a0b4a260c" alt="Image 5" width="300" height="auto">
<img src="https://github.com/user-attachments/assets/88eb8a94-4822-4437-b2d0-859be4ce3c66" alt="Image 6" width="300" height="auto">
<img src="https://github.com/user-attachments/assets/ea13eddd-7f85-4e3b-9a11-7ad1bc4facb5" alt="Image 7" width="300" height="auto">
