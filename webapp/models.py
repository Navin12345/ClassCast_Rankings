from django.db import models

class classcast_student_info(models.Model):
    student_id = models.IntegerField(null=False, primary_key=True)
    pincode = models.IntegerField()
    standard = models.IntegerField()
    stream = models.CharField(max_length=15)
    marks_scored_in_last_degree = models.FloatField()
    total_time_spent_on_platform = models.FloatField()
    active_status = models.CharField(max_length=15)
    last_active = models.DateTimeField()
    total_karma_points = models.FloatField()
    phone_number = models.CharField(max_length=15)
    DOB = models.DateField()

    class Meta:
        db_table = 'classcast_student_info'
