from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
from django.views.generic import DetailView, UpdateView, DeleteView


def home_page(request):
    event = Event.objects.all()
    return render(request, 'event_logger/home_page.html', {'event': event})


def create_event(request):
    error = ''
    if request.method == 'POST':
        form_post = EventForm(request.POST)
        if form_post.is_valid():
            form_post.save()
            return redirect('home_page')
        else:
            error = 'The form is not filled out correctly '

    form = EventForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'event_logger/form_add_event.html', data)


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_logger/details_view.html'
    context_object_name = 'event_view'


class EventUpdateView(UpdateView):
    model = Event
    template_name = 'event_logger/form_add_event.html'
    context_object_name = 'event_update'

    form_class = EventForm


class EventDeleteView(DeleteView):
    model = Event
    success_url = '/'
    template_name = 'event_logger/delete_event.html'
    context_object_name = 'event_delete'

