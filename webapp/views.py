from django.http import HttpResponse
from rest_framework.views import APIView
from .models import classcast_student_info



class rankings(APIView):
    

    def get(self, request, student_id):
        l = len(classcast_student_info.objects.all().order_by('total_karma_points'))
        marks=[]
        for i in range(l):
            a=classcast_student_info.objects.all().get(pk=i+1)
            marks.append(a.total_karma_points)
        marks.sort()
        student = classcast_student_info.objects.get(student_id = student_id)
        karma_point = student.total_karma_points
        return(HttpResponse(marks.index(karma_point)+1))
            
        

    def post(self):
        pass
