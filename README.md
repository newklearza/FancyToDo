# 🚀 FancyToDo: A Quirky To-Do Web App
![image](https://github.com/newklearza/FancyToDo/assets/16708472/7cc117a2-a974-4837-8129-3963ab97a3c4)


Welcome to FancyToDo, a whimsical to-do web application that's bound to tickle your productivity fancy. Whether you're a task master or just want a quirky way to organize your day, FancyToDo has got you covered!

## Overview

FancyToDo is a to-do web application that offers both a delightful frontend interface and a robust backend API. This project showcases how to create, manage, and toggle tasks. Get ready to have fun while tackling your tasks!

## Tech Stack
• Python
• PostgreSQL
• Docker
• Html/JS

## Prerequisites

To get started with FancyToDo, you'll need:

- Docker: [Install Docker](https://www.docker.com/get-started)
- Requirements & dependencies are all included

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/fancy-todo.git
   cd fancy-todo

2. Once cloned, spin up a cmd line session and build the containers:

   ```bash
   • docker-compose up --build

3. FancyToDo should now be up and running! You can access it by opening your web browser and navigating to:
   ```bash
   • http://localhost:5000

## Usage
4. Frontend: Interact with the friendly web interface to add, list, and toggle tasks.
Backend API: The API exposes endpoints for task management. For details, refer to the API documentation.
Automated Tests
We've included automated tests to ensure the reliability of FancyToDo. The tests are categorized into two types:
<br><br>
5. Unit Tests: These tests focus on individual components or functions in the application, ensuring they perform as expected. 
6. Integration Tests: These tests examine how different parts of the application interact with each other, ensuring the application's behavior as a whole is correct.

7. Run Backend Tests:
   ```bash
   • Copy code
   • docker-compose exec frontend pytest
   • docker-compose exec backend pytest

8. ## What would I do to improve?
   ```bash
   • Perhaps convert into using a Redis Cache DB using key:pairs
   • Complete pages for more functionality, templates are inside
9. Contributions are welcome! Feel free to open an issue or create a pull request if you have any improvements, bug fixes, or new features to suggest.

10. License: This project is licensed under the MIT License. See the LICENSE file for details.
Get started with FancyToDo today and turn your to-do list into a to-do delight! Happy tasking! 😄

