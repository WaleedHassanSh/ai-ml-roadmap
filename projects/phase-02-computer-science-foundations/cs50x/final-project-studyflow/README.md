# StudyFlow

#### Video Demo: <https://youtu.be/rcWY2JsWQKE>

#### Description

StudyFlow is a student task and course management web application built with Flask, SQLite, HTML, and CSS. The purpose of the project is to help students organize their academic work in one simple dashboard. Instead of keeping deadlines, assignments, labs, and course tasks in different places, StudyFlow allows a student to add tasks, assign each task to a course, set a deadline, choose a priority level, and track whether the task is still pending or has been completed.

I built this project because students often have several courses running at the same time, and it becomes easy to forget small deadlines or lose track of which tasks are urgent. StudyFlow solves this problem by giving the user a clear view of all saved tasks, sorted by deadline. The application is simple enough to use quickly, but it also includes useful features such as searching, filtering, dashboard counts, completion tracking, and deletion.

The main page of StudyFlow shows the project title, a short description, task statistics, a search bar, status filter buttons, and a table of saved tasks. The dashboard count section displays the total number of tasks, the number of pending tasks, and the number of completed tasks. This gives the user an immediate summary of their workload. The search feature allows the user to find tasks by course name or task title. For example, searching for a course such as CS50 or a word such as project will return matching tasks from the database. The filter buttons allow the user to view all tasks, only pending tasks, or only completed tasks.

The add task page contains a form where the user enters the course name, task title, deadline, and priority. The form uses validation so that empty submissions are not accepted. If the user leaves a required field empty or does not select a valid priority, an error message is shown. Once a valid task is submitted, the task is inserted into the SQLite database and the user is redirected back to the homepage. New tasks are automatically given a status of pending by default.

Each task displayed on the homepage includes its course, title, deadline, priority, and status. Pending tasks show a Mark Completed button. When the user clicks this button, the application updates that task in the database and changes its status from pending to completed. Completed tasks no longer show the Mark Completed button, which prevents unnecessary repeated updates and makes the interface clearer. Each row also includes a Delete Task button, which removes the selected task from the database.

## Features

StudyFlow includes the following main features:

- Add new academic tasks with course, title, deadline, and priority.
- Validate form input before saving a task.
- Store all tasks permanently in an SQLite database.
- Display all saved tasks in a table.
- Sort tasks by deadline in ascending order.
- Search tasks by course name or task title.
- Filter tasks by status: all, pending, or completed.
- Show dashboard counts for total, pending, and completed tasks.
- Mark pending tasks as completed.
- Hide the Mark Completed button for already completed tasks.
- Delete tasks from the database.
- Display a message when no tasks are available.
- Use CSS styling for a clean dashboard layout.

## Files

The project is organized into several files and folders.

`app.py` is the main Flask application file. It contains the route for the homepage, the route for adding a task, the route for marking a task as completed, and the route for deleting a task. It also connects the application to the SQLite database using the CS50 SQL library. The homepage route reads optional search and filter values from the URL, selects the correct tasks from the database, calculates task counts, and passes all required data to the template.

`templates/index.html` contains the homepage layout. It displays the StudyFlow heading, dashboard counts, search form, filter buttons, and task table. It also uses Jinja template logic to loop through the tasks returned from Flask and display each task in a table row. The template also checks whether a task is pending or completed so that the Mark Completed button is only shown for pending tasks.

`templates/add.html` contains the add task form. It allows the user to enter the course, title, deadline, and priority of a new task. It also displays an error message when Flask sends a validation message back to the page.

`static/styles.css` contains the styling for the project. It defines the page background, main container, dashboard cards, buttons, forms, table, error message, and search bar. The design uses a clean student-dashboard style with readable spacing, rounded corners, and separate colors for normal actions, completion actions, and delete actions.

`studyflow.db` is the SQLite database file used to store tasks. The database keeps the saved tasks available even after the Flask server is stopped and restarted.

`requirements.txt` lists the Python packages needed to run the project, including Flask and the CS50 library.

## Database Design

The project uses one main database table named `tasks`. Each row in the table represents one student task. The table contains the following columns:

- `id`: a unique integer ID for each task.
- `course`: the course name connected to the task.
- `title`: the title or short description of the task.
- `deadline`: the due date of the task.
- `priority`: the priority level, such as low, medium, or high.
- `status`: the current task status, either pending or completed.

The `id` column is used when updating or deleting a specific task. The `status` column has a default value of pending, so every new task starts as pending unless it is later marked completed.

## Design Choices

I chose Flask because it is lightweight, beginner-friendly, and suitable for building a small web application with multiple routes and templates. I used SQLite because the project only needs local storage and does not require a large external database system. SQLite also works well for a CS50-style project because it allows the application to demonstrate real database operations such as insert, select, update, delete, count, search, and filtering.

I used separate HTML templates for the homepage and add task page to keep the structure clear. I also used a separate CSS file so that the design is not mixed directly into the HTML. The dashboard count section was added to make the application more useful at a glance. The search and filter features were added because a task list becomes harder to use as more tasks are added.

## How to Run

To run the project, first make sure the required packages are installed:

```bash
pip install flask cs50
```

Then run the Flask application from the project folder:

```bash
flask run
```

After the server starts, open the local URL shown in the terminal. The homepage will show the StudyFlow dashboard. From there, the user can add tasks, search tasks, filter tasks, mark tasks as completed, and delete tasks.

## Challenges and Future Improvements

One challenge in this project was connecting the HTML forms correctly to Flask routes. I had to make sure that form field names matched the names used in `request.form.get()` and that actions which changed the database used POST requests. Another challenge was writing the correct SQL queries for searching, filtering, updating, deleting, and counting tasks.

In the future, StudyFlow could be improved by adding user accounts so that multiple students can have their own private task lists. It could also include deadline warnings, overdue task highlighting, priority-based sorting, edit-task functionality, and a calendar view. Another possible improvement would be combining search and filters together so that a user can search only within pending or completed tasks.

During development, I used ChatGPT for guidance, debugging help, and explanations. The final implementation, testing, and design decisions are my own.
