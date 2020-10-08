from django import forms

from .models import Department, Staff, Person, State, LGA


class DepartmentCreateForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('department_name', 'department_head', 'number_of_staffs')


class StaffCreateForm(forms.ModelForm):
    DOB = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    start_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    date_obtained = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Staff
        fields = ('first_name', 'last_name', 'other_name', 'sex', 'DOB', 'address', 'phone_number',
                  'email', 'department', 'start_date', 'end_date', 'higher_qualification', 'result_obtained',
                  'school_attended', 'date_obtained', 'other_qualification',
                  'professional_qualification')


class PersonCreateForm(forms.ModelForm):
    DOB = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Person
        fields = ('surname', 'first_name', 'other_name', 'current_age', 'DOB', 'sex', 'nationality',
                  'residential_state', 'residential_lga', 'residential_town', 'occupation', 'state_of_birth', 'lga_of_birth', 'disabled', 'work_status',)


class StateCreateForm(forms.ModelForm):

    class Meta:
        model = State
        fields = ('state_name', 'state_zone')


class LGACreateForm(forms.ModelForm):

    class Meta:
        model = LGA
        fields = ('lga_name', 'lga_zone', 'lga_state')
