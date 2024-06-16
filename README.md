# Lodify

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

## Introduction

This web application is designed to function similarly to Airbnb, providing a platform for users to list, discover, and book accommodations. The application allows property owners to create listings and renters to browse and book properties.

## Features

- User Authentication: Registration and login functionalities for users.
- Property Listings: Users can create, edit, and delete property listings.
- Search and Filter: Users can search and filter properties based on various criteria.
- Booking System: Users can book properties and view their booking history.
- Reviews and Ratings: Users can leave reviews and ratings for properties.
- Responsive Design: The application is designed to be responsive and accessible on various devices.

## Technology Stack

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLAlchemy, MySQL
- **Styling**: Bootstrap for responsive design

## Installation

To get a local copy up and running, follow these steps:

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/your-repo/web-app.git
    cd web-app
    ```

2. **Set up the Virtual Environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the Database:**
    - Ensure you have MySQL installed and running.
    - Create a database named `airbnb_clone`.
    - Update the database configuration in `config.py` with your MySQL username and password.

5. **Initialize the Database:**
    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

6. **Run the Application:**
    ```sh
    flask run
    ```

## Usage

Once the application is up and running, you can access it at `http://127.0.0.1:5000/`.

- **Home Page:** Browse and search for properties.
- **User Registration/Login:** Sign up or log in to access additional features.
- **Property Management:** Create, edit, and delete property listings.
- **Booking:** Book available properties and view booking history.
- **Reviews:** Leave reviews and ratings for properties you've stayed in.

## Contributors

- **Akoma Goodness James**
- **Ginika Elizabeth**
- **Ikechukwu Miracle**

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

