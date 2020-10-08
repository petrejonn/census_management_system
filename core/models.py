from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=250)
    department_head = models.CharField(max_length=250)
    number_of_staffs = models.IntegerField()
    date_of_creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name


class Staff (models.Model):
    SEX = (
        ["Male", "Male"],
        ["Female", "Female"]
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=25, choices=SEX)
    DOB = models.DateField()
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="staffs")
    start_date = models.DateField()
    end_date = models.DateField()
    higher_qualification = models.CharField(max_length=25)
    result_obtained = models.CharField(max_length=150)
    school_attended = models.CharField(max_length=250)
    date_obtained = models.DateField()
    other_qualification = models.CharField(max_length=255)
    professional_qualification = models.CharField(max_length=250)

    def fullname(self):
        return self.last_name+" "+self.first_name+" "+self.other_name

    def __str__(self):
        return self.last_name+" "+self.first_name+" "+self.other_name


class State(models.Model):
    state_name = models.CharField(max_length=250)
    state_zone = models.CharField(max_length=15)

    def __str__(self):
        return self.state_name


class LGA(models.Model):
    lga_name = models.CharField(max_length=250)
    lga_zone = models.CharField(max_length=15)
    lga_state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name="lgas")

    def __str__(self):
        return self.lga_name


class Person(models.Model):
    SEX = (
        ["Male", "Male"],
        ["Female", "Female"]
    )
    DISABLED = (
        ["Yes", "Yes"],
        ["No", "No"]
    )
    WORK_STATUS = (
        ["Employed", "Employed"],
        ["Unemployed", "Unemployed"]
    )
    surname = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    other_name = models.CharField(max_length=250)
    current_age = models.IntegerField()
    DOB = models.DateField()
    sex = models.CharField(max_length=25, choices=SEX)
    nationality = models.CharField(max_length=150)
    residential_state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name='state_residents')
    residential_lga = models.ForeignKey(
        LGA, on_delete=models.CASCADE, related_name='lga_residents')
    residential_town = models.CharField(max_length=150)
    occupation = models.CharField(max_length=150)
    state_of_birth = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name='state_of_birth')
    lga_of_birth = models.ForeignKey(
        LGA, on_delete=models.CASCADE, related_name='lga_of_birth')
    disabled = models.CharField(max_length=25, choices=DISABLED)
    work_status = models.CharField(max_length=25, choices=WORK_STATUS)

    def __str__(self):
        return self.surname+" "+self.first_name+" "+self.other_name

    def fullname(self):
        return self.surname+" "+self.first_name+" "+self.other_name
