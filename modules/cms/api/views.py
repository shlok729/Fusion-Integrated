from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from ..models import Complaint
from .serializers import ComplaintSerializer

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    @action(detail=True, methods=['post'])
    def assign(self, request, pk=None):
        complaint = self.get_object()
        complaint.status = 'assigned'
        complaint.assigned_to = request.data.get('assigned_to')
        complaint.save()
        return Response({'status': 'assigned'})

    @action(detail=True, methods=['post'])
    def resolve(self, request, pk=None):
        complaint = self.get_object()
        complaint.status = 'resolved'
        complaint.save()
        return Response({'status': 'resolved'})

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        complaint = self.get_object()
        complaint.status = 'rejected'
        complaint.save()
        return Response({'status': 'rejected'})

    @action(detail=True, methods=['post'])
    def escalate(self, request, pk=None):
        complaint = self.get_object()
        complaint.status = 'escalated'
        complaint.save()
        return Response({'status': 'escalated'})