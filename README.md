# FastAPI_Kong_with_Postgres_JWT_Example

This is a sample project demonstrating how to implement interaction with Kong API Gateway using FastAPI, along with JWT token-based authorization.

## To-Do
1. Improve testing of kong operations
2. Add tests of endpoints
2. Add endpoint to list consumers
3. Add endpoint to list services
4. Add endpoint to list routers
5. Add endpoint to list consumer JWTs

## Description

This project showcases how to set up the Kong API Gateway with JWT token authorization, leveraging FastAPI to implement the business logic.

## Features

Using Kong API Gateway with PostreSQL database.
Interaction with Kong Admin API using FastAPI.
Authorization using JWT tokens.

## Prerequisites

* Docker
* Docker-Compose

Here's a brief explanation of how this project works:

Kong API Gateway is used as the main endpoint for all requests. 
FastAPI is utilized for handling the requests and generating responses.
JWT (JSON Web Tokens) are employed for user authorization.

## Installation

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. You need Docker and Docker-compose installed on your system to run this project. Once installed, use the following command to build and start the containers: `docker-compose up -d`.
4. Run tests using command to verify is everythink working: `docker-compose exec fastapi-app python -m pytest`
5. Open your browser and go to: `http://localhost:8080/kong-fastapi-example/docs`

## Usage

Once everything is configured and running, you can start interacting with the Kong API by using FastAPI docs page.

After impleneting JWT to kong by using FastAPI Docs you want to verify is JWT working in Kong. For that you need to install Postman and send GET request with Bearer token that you generate using FastAPI Docs to:
<br />
`http://localhost:8000/kong-fastapi-example/fastapi-bearer-authorization-and-jwt-payload-decoding`

## Support

If you have any questions or run into any issues, please create a new issue in our GitHub issue tracker.


## Conclusion

We hope this project helps you understand how to set up Kong API Gateway with JWT authorization, using FastAPI for handling the business logic. We encourage further exploration and modification of the code for better understanding of how these technologies can work together.

## Author

Wojciech Ignasiak
<br />
wojciech_ignasiak@icloud.com

## Contact

If you have any questions or would like to share your feedback, feel free to get in touch with me at email.

Thank you for visiting this repository!
 
