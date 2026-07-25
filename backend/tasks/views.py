from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related('category').all()
    serializer_class = TaskSerializer

    #Filtering Searching and ordering built in
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Custom Action: GET /api/tasks/summary/
    @action(detail=False, methods=['get'], url_path='summary')
    def summary(self, request):
        total = Task.objects.count()
        pending = Task.objects.filter(status='Pending').count()
        in_Progress = Task.objects.filter(status='In Process').count()
        done = Task.objects.filter(status='Done').count()

        return Response({
            'total': total,
            'pending': pending,
            'in_Progress': in_Progress,
            'done': done
        }
        )



