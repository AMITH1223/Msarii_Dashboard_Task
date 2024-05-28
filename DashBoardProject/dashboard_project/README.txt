Created a Django application demonstrating role-based authentication with distinct dashboards for Admin, Manager, 
and Employee roles, and a role-specific notification system. Use Django Rest Framework for backend.

models:
we are used Role,UserProfile,Project,Task,Notification these tables to build an application.
Role: used to save role for the user.
UserProfile: role is an foreign key in this table, here for the user we are assigning the role.
Project: used to save the project details.
Task: project name is an foreign key in this table, based on the project we are assigning the task.
Notification: role is an foreign key in this table, used to assign the message or information based on the role.

Project,Task,Notification for these table we are used an apis to enter the data.
Role,UserProfile for these tables manually entered the data.

we use permissions also based on the role.

admindashboard:
username:Amith
password:Test@123
based on requirement in the dashboard is showing and filteration done.

Managerdashboard:
username:Akash
password:Test@123
based on requirement in the dashboard is showing and filteration done.

Employeedashboard:
username:Abhi
password:Test@123
based on requirement in the dashboard is showing and filteration done.

To load the login page from the URL http://127.0.0.1:8000.

To run the server:
python manage.py runserver.

for the apis url is:
http://127.0.0.1:8000/projects for project table.
http://127.0.0.1:8000/tasks for task table.
http://127.0.0.1:8000/Notification for notification table.
