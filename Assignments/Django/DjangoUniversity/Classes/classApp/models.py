from django.db import models


# #3 creating class with int,string, and float attributes
class djangoClasses(models.Model):
    Title = models.CharField(max_length=100, default="", blank=True, null=False)
    CourseNumber = models.IntegerField(default=0)
    InstructorName = models.CharField(max_length=100, default="", blank=True, null=False)
    Duration = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)

    # model-manager communicates with database
    objects = models.Manager()

    # displays course name
    def __str__(self):
        return self.Title