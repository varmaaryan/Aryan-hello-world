# Django Hello World API

This is a simple Django project that returns a "Hello World!" JSON response from an API endpoint.

## How to Run the Web App

1. Clone the repository:
    ```
    git clone https://github.com/your-username/django-hello-world.git
    cd django-hello-world
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Run the Django development server:
    ```
    python manage.py runserver
    ```

4. Access the Hello World response in your browser:
   1) for the main theme.
    ```
    http://127.0.0.1:8000/api/hello/
    ```
    2) for simple json response.
    ```
    http://127.0.0.1:8000/api/hello/json/
    ```
    3) for bold text
    ```
    http://127.0.0.1:8000/api/hello/bold/
    ```

## Optional - HTML Template

This project also includes couple HTML template that renders the message "Hello World!" in bold, which is displayed when visiting `/api/hello/bold/` instead of the JSON response. and it displays cool effect when visiting  `/api/hello/` instead of the JSON response 
