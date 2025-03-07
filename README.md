# Django To-Do List ✅  

A to-do list web application built with Django. Users can add, edit, delete, and mark tasks as complete. Completed tasks are displayed on a separate page, grouped by the date of completion. This project is designed to run locally and serves as a learning exercise in Django fundamentals.  

## Features  
- 📌 Add, edit, and delete tasks  
- ✅ Mark tasks as complete  
- 📅 View completed tasks, grouped by completion date  
- 🎯 Simple and clean UI   

### Prerequisites  
- Python 3.12.4  
- Django 5.1.6

### Steps  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/django-to-do-list.git
   cd django-to-do-list
   ```

   2.	Create and activate a virtual environment:
      ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      ```
   
   3.	Install dependencies:
      ```bash
      pip install -r requirements.txt
      ```
   
   
   4.	Apply migrations:
      ```bash
      python manage.py migrate
      ```
   
   
   5.	Run the development server:
      ```bash
      python manage.py runserver
      ```
   
   6.	Open the app in your browser:
      http://127.0.0.1:8000/



Usage
   •	Add a new task using the "Add New Task" button.
   •	Edit or delete tasks using the respective buttons.
   •	Mark a task as complete, which moves it to the “Completed Tasks” page.
   •	View all completed tasks, grouped by the date they were finished.

License

   This project is licensed under the MIT License.

Contributions

   Contributions are welcome! Feel free to submit a pull request or open an issue.

⸻

🚀 Happy coding!
