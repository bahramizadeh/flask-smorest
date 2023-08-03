# sky-task

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Table of Contents

- [sky-task](#sky-task)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)

## About

This project has 2 APIs which get different type of data from <https://bittrex.github.io> website and return back to the client.
JWT is used for protecting, authentication and authorization of these APIs. In this project I have user model and user resource to handle JWT and create access tokens.

## Features

- List the key features and functionalities of your Python project.
- 2 APIs for getting two different information of the mentioned website.
- User APIs for creating, updating, getting and deleting user in table users.
- User model to keep users information like username and password in database for creating JWT access token.
- Using SQLLight as our database.
- Using REDIS as cache system in our project to reduce the queries to the database and the time of getting the result from DB.
- Dockerize my project.


## Getting Started

Instructions on how to set up the project locally and get it running on a user's machine.
This project has a git link to clone and install.
First, get a clone of the project from this url <https://github.com/bahramizadeh/sky-task.git> and save it in your computer.
After getting clone the project open the project in one IDE like vscode and open a terminal.
run this command in the terminal of vscode <docker-compose up --build --force-recreate>.


### Prerequisites

List any software or libraries that users need to have installed before they can use your project. For example:

- Python (version 3.10 or higher)
- Postman to send request to the application


### Installation

Step-by-step guide on how to install your Python project. For example:

1. Clone the repository: `git clone https://github.com/bahramizadeh/sky-task.git`
2. Change into the project directory: `cd sky-task`
3. Create a virtual environment (optional but recommended): `python -m venv venv`
4. Activate the virtual environment (if created):
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. run this command in the terminal of vscode <docker-compose up --build --force-recreate>.

## Usage

Provide examples and instructions on how to use your Python project. Include code snippets and usage scenarios to make it easier for others to understand how your project works. For example:

```bash
$ flask run
