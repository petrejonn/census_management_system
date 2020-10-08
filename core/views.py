from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DetailView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (StateCreateForm, DepartmentCreateForm,
                    StaffCreateForm, StateCreateForm, LGACreateForm, PersonCreateForm)
from .models import (Person, Department, Staff, State, LGA,)


class HomeView(LoginRequiredMixin, ListView):
    model = Person
    template_name = 'dashboard/index.html'


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'dashboard/department/list.html'


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    form_class = DepartmentCreateForm
    template_name = 'dashboard/department/create.html'
    success_url = reverse_lazy('core:department_list')


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentCreateForm
    template_name = 'dashboard/department/update.html'
    success_url = reverse_lazy('core:department_list')


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    form_class = DepartmentCreateForm
    template_name = 'dashboard/department/delete.html'
    success_url = reverse_lazy('core:department_list')


class StaffListView(LoginRequiredMixin, ListView):
    model = Staff
    template_name = 'dashboard/staff/list.html'


class StaffCreateView(LoginRequiredMixin, CreateView):
    form_class = StaffCreateForm
    template_name = 'dashboard/staff/create.html'
    success_url = reverse_lazy('core:staff_list')


class StaffUpdateView(LoginRequiredMixin, UpdateView):
    model = Staff
    form_class = StaffCreateForm
    template_name = 'dashboard/staff/update.html'
    success_url = reverse_lazy('core:staff_list')


class StaffDeleteView(LoginRequiredMixin, DeleteView):
    model = Staff
    template_name = 'dashboard/staff/delete.html'
    success_url = reverse_lazy('core:staff_list')


class StateListView(LoginRequiredMixin, ListView):
    model = State
    template_name = 'dashboard/state/list.html'


class StateCreateView(LoginRequiredMixin, CreateView):
    form_class = StateCreateForm
    template_name = 'dashboard/state/create.html'
    success_url = reverse_lazy('core:state_list')


class StateUpdateView(LoginRequiredMixin, UpdateView):
    model = State
    form_class = StateCreateForm
    template_name = 'dashboard/state/update.html'
    success_url = reverse_lazy('core:state_list')


class StateDeleteView(LoginRequiredMixin, DeleteView):
    model = State
    template_name = 'dashboard/state/delete.html'
    success_url = reverse_lazy('core:state_list')


class LGAListView(LoginRequiredMixin, ListView):
    model = LGA
    template_name = 'dashboard/lga/list.html'


class LGACreateView(LoginRequiredMixin, CreateView):
    form_class = LGACreateForm
    template_name = 'dashboard/lga/create.html'
    success_url = reverse_lazy('core:lga_list')


class LGAUpdateView(LoginRequiredMixin, UpdateView):
    model = LGA
    form_class = LGACreateForm
    template_name = 'dashboard/lga/update.html'
    success_url = reverse_lazy('core:lga_list')


class LGADeleteView(LoginRequiredMixin, DeleteView):
    model = LGA
    template_name = 'dashboard/lga/delete.html'
    success_url = reverse_lazy('core:lga_list')


class PersonListView(LoginRequiredMixin, ListView):
    model = Person
    template_name = 'dashboard/person/list.html'


class PersonCreateView(LoginRequiredMixin, CreateView):
    form_class = PersonCreateForm
    template_name = 'dashboard/person/create.html'
    success_url = reverse_lazy('core:person_list')


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonCreateForm
    template_name = 'dashboard/person/update.html'
    success_url = reverse_lazy('core:person_list')


class PersonDeleteView(LoginRequiredMixin, DeleteView):
    model = Person
    template_name = 'dashboard/person/delete.html'
    success_url = reverse_lazy('core:person_list')


class PersonDetailView(LoginRequiredMixin, DetailView):
    model = Person
    template_name = 'dashboard/person/detail.html'
