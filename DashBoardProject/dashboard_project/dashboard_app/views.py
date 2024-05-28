# # views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Project, Task, UserProfile, Notification, Role
from .serializers import ProjectSerializer, TaskSerializer, NotificationSerializer
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse

# project table api creation
class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated | IsAdminOrReadOnly]

# Task table api creation
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

# Notification table api creation
class NotificationListCreate(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]


# login page 
@login_required
def loginLandingpage(request):
    return render(request, 'Loginpage.html')

# login details 
@login_required
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            userprofile = UserProfile.objects.get(user=user)
            # Check if the user has the necessary role
            if userprofile.role.name == 'Admin':
                user_count = UserProfile.objects.count() 
                data = Project.objects.values('status').distinct()
                project_data = Project.objects.values('name').distinct()
                admin_role = Role.objects.get(name='Admin')
                notification_status = Notification.objects.filter(role=admin_role)

                context = {
                    'user_count': user_count,
                    'project_data': project_data,
                    'notification_status': notification_status,
                    'status': data,
                }
                return render(request, 'AdminDashboard.html', context)
            elif userprofile.role.name == 'Manager':
                project_name = Project.objects.values('name').distinct()
                project_team = Project.objects.values('team').distinct()
                project_data = Project.objects.all()
                admin_role = Role.objects.get(name='Manager')
                notification_status = Notification.objects.filter(role=admin_role)
                context = {
                    'project_manager_name': project_name,
                    'project_manager_team': project_team,
                    'project_manager_data': project_data,
                    'notification_manager_status': notification_status,
                }
                return render(request, 'ManagerDashboard.html', context)
            elif userprofile.role.name == 'Employee':
                Task_priority = Task.objects.values('priority').distinct()
                Task_data = Task.objects.all()
                admin_role = Role.objects.get(name='Employee')
                notification_status = Notification.objects.filter(role=admin_role)
                context = {
                    'project_employee_priority': Task_priority,
                    'project_employee_data': Task_data,
                    'notification_employee_status': notification_status,
                }
                return render(request, 'EmployeeDashboard.html', context)
        else:
            # Return an invalid login error message
            return render(request, 'Login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'Login.html')

# admindashboard filteration 
def adminFilteration(request):
    if request.method == 'POST':
        selected_status = request.POST.get('status')
        user_count = UserProfile.objects.count() 
        data = Project.objects.values('status').distinct()
        admin_role = Role.objects.get(name='Admin')
        notification_status = Notification.objects.filter(role=admin_role)

        if selected_status == 'All':
            project_data = Project.objects.values('name').distinct()
        else:
            project_data = Project.objects.filter(status=selected_status)

        context = {
            'user_count': user_count,
            'project_data': list(project_data.values()),  # Convert QuerySet to list of dictionaries
            'notification_status': list(notification_status.values()),  # Convert QuerySet to list of dictionaries
            'status': list(data),  # Convert QuerySet to list of dictionaries
        }

        return JsonResponse(context)
    else:
        # Handle other HTTP methods if necessary
        return JsonResponse({'error': 'Only POST method is allowed for this endpoint'}, status=405)


# managerdashboard filteration 
def managerFilteration(request):
    if request.method == 'POST':
        project_nme = request.POST.get('project')
        team_name = request.POST.get('team')
        print('data1',project_nme)
        print('data2',team_name)

        if project_nme == 'All' and team_name == 'All':
            project_data = Project.objects.all()
        elif project_nme == 'All':
            project_data = Project.objects.filter(team=team_name)
        elif team_name == 'All':
            project_data = Project.objects.filter(name=project_nme)
        else:
            project_data = Project.objects.filter(name=project_nme, team=team_name)
        project_name = Project.objects.values('name').distinct()
        project_team = Project.objects.values('team').distinct()
        admin_role = Role.objects.get(name='Manager')
        notification_status = Notification.objects.filter(role=admin_role)
        print('data3',project_data)
        context = {
            'project_manager_name': list(project_name),
            'project_manager_team': list(project_team),
            'project_manager_data': list(project_data.values()), 
            'notification_manager_status': list(notification_status.values()),
        }

        return JsonResponse(context)

            

# employeedashboard filteration 
def employeeFilteration(request):
    priorityname = request.POST.get('priorityname')
    
    if priorityname == 'All':
        Task_data = Task.objects.all()
    elif priorityname == 'High':
        Task_data = Task.objects.filter(priority='High')
    elif priorityname == 'Medium':
        Task_data = Task.objects.filter(priority='Medium')
    elif priorityname == 'Low':
        Task_data = Task.objects.filter(priority='Low')
    else:
        Task_data = Task.objects.none()
    
    Task_data_serialized = list(Task_data.values('name', 'end_date', 'priority', 'status'))
    Task_priority = list(Task.objects.values('priority').distinct())
    admin_role = Role.objects.get(name='Employee')
    notification_status = list(Notification.objects.filter(role=admin_role).values())
    
    context = {
        'project_employee_priority': Task_priority,
        'project_employee_data': Task_data_serialized,
        'notification_employee_status': notification_status,
    }
    return JsonResponse(context)