# Bookstore CRUD Application

This project is a CRUD (Create, Read, Update, Delete) application for managing a bookstore. It consists of a FastAPI backend for handling the API operations and a Streamlit frontend for the user interface. The backend interacts with a MySQL database to store and retrieve book information.

## Features

- List all books
- Get book details by ID
- Add a new book
- Update the quantity of an existing book
- Delete a book

## Technologies Used

- FastAPI
- SQLAlchemy
- MySQL
- Streamlit
- Docker

## Getting Started

### Prerequisites

- Docker
- Python 3.8+

### Setup MySQL with Docker

1. Pull the MySQL Docker image:

    ```bash
    docker pull mysql:latest
    ```

2. Run the MySQL container:

    ```bash
    docker run --name bookstore_db -e MYSQL_ROOT_PASSWORD=your_password -e MYSQL_DATABASE=bookstore_db -p 3306:3306 -d mysql:latest
    ```

### Backend Setup (FastAPI)

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/bookstore-crud.git
    cd bookstore-crud
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

### Frontend Setup (Streamlit)

1. In a new terminal, navigate to the project directory and activate the virtual environment:

    ```bash
    cd bookstore-crud
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Start the Streamlit application:

    ```bash
    streamlit run app.py
    ```

## Project Structure


- `app.py`: Streamlit application for the frontend.
- `crud.py`: CRUD operations for interacting with the database.
- `database.py`: Database setup and connection configuration.
- `main.py`: FastAPI application setup and endpoints.
- `models.py`: SQLAlchemy models for the database.
- `schemas.py`: Pydantic models for request and response validation.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## API Endpoints

- **GET /books/**: Retrieve a list of all books.
- **GET /books/{book_id}**: Retrieve details of a specific book by ID.
- **POST /books/**: Add a new book.
- **PUT /books/{book_id}**: Update the quantity of a specific book by ID.
- **DELETE /books/{book_id}**: Delete a specific book by ID.

## Logging and Error Handling

The application includes logging and error handling for better debugging and user experience. Errors encountered during API calls in the Streamlit frontend are logged and displayed to the user with appropriate messages.

## License

This project is licensed under the MIT License.
