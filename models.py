
from django.db import models

# Create your models here.
class contactus(models.Model):
    Name=models.CharField(max_length=200,null=True)
    Email=models.CharField(max_length=100,null=True)
    Mobile=models.CharField(max_length=25,null=True)
    Message=models.TextField(null=True)
    def __str__(self):

        return self.Name

class studentbatch(models.Model):
    batch_name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.batch_name
class signup(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,primary_key=True)
    mobile=models.CharField(max_length=30,null=True)
    profile=models.ImageField(upload_to='static/profile/',null=True)
    course=models.CharField(max_length=30,null=True)
    pyear=models.CharField(max_length=30,null=True)
    college=models.CharField(max_length=200,null=True)
    batch=models.ForeignKey(studentbatch,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=30,null=True)
    passwd=models.CharField(max_length=100,null=True)
    batchid=models.IntegerField(null=True)
    def __str__(self):
        return self.name

class slider(models.Model):
        headlines = models.TextField(null=True)
        slider_dec = models.TextField(null=True)
        slider_picture = models.ImageField(upload_to='static/slider/', null=True)

        def __str__(self):
            return self.headlines


class newbatches(models.Model):
    name=models.CharField(max_length=100)
    batch_pic=models.ImageField(upload_to='static/newbatches/',null=True)
    starting_date=models.DateTimeField(null=True)

class college(models.Model):
    college_name=models.CharField(max_length=200,null=True)
    college_picture=models.ImageField(upload_to='static/college',null=True)
    def __str__(self):
        return self.college_name

class session_year(models.Model):
    session=models.CharField(max_length=1000,null=True)
    def __str__(self):
        return self.session


class batch(models.Model):
    batch_name=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.batch_name

class placement(models.Model):
    student_picture=models.ImageField(upload_to='static/placement/',null=True)
    student_name=models.CharField(max_length=100,null=True)
    college=models.ForeignKey(college,on_delete=models.CASCADE,null=True)
    session=models.ForeignKey(session_year,on_delete=models.CASCADE,null=True)
    batch=models.ForeignKey(batch,on_delete=models.CASCADE,null=True)
    company_name=models.CharField(max_length=200,null=True)
    company_logo=models.ImageField(upload_to='static/company/',null=True)

class category(models.Model):
    category_name=models.CharField(max_length=200,null=True)
    category_picture=models.ImageField(upload_to='static/category',null=True)
    category_date=models.DateField(null=True)
    def __str__(self):
        return self.category_name



class mylectures(models.Model):
    video_category=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    video_batch=models.ForeignKey(studentbatch,on_delete=models.CASCADE,null=True)
    vlink=models.CharField(max_length=300,null=True)
    thumbnail=models.ImageField(upload_to='static/video',null=True)
    video_description=models.TextField(null=True)
    added_date=models.DateField(null=True)

class batchtiming(models.Model):
    batch=models.ForeignKey(studentbatch,on_delete=models.CASCADE,null=True)
    clink=models.CharField(max_length=300,null=True)
    timing=models.CharField(max_length=50,null=True)
    start_date=models.DateField(null=True)

class enotes(models.Model):
    title=models.CharField(max_length=200,null=True)
    note_pic=models.ImageField(upload_to='static/enotes',null=True)
    pdf_notes=models.FileField(upload_to='static/pdf',null=True)
    batch=models.ForeignKey(studentbatch,on_delete=models.CASCADE,null=True)
    added_date=models.DateField(null=True)

class mytask(models.Model):
    taskbatch=models.ForeignKey(studentbatch,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=200,null=True)
    task_file=models.FileField(upload_to='static/task',null=True)
    added_date=models.DateField(null=True)

class submittedtask(models.Model):
    title=models.CharField(max_length=200,null=True)
    answer_file=models.FileField(upload_to='static/submittedtask',null=True)
    tid=models.CharField(max_length=20,null=True)
    userid=models.CharField(max_length=200,null=True)
    marks=models.CharField(max_length=200,null=True)




