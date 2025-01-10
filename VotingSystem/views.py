from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Competition, Entry

@login_required
def competition_list(request):
    competitions = Competition.objects.all()
    return render(request, 'competition_list.html', {'competitions': competitions})

@login_required
def competition_detail(request, competition_id):
    competition = Competition.objects.get(id=competition_id)
    entries = Entry.objects.filter(competition=competition)
    return render(request, 'competition_detail.html', {'competition': competition, 'entries': entries})

@login_required
def vote_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    if request.method == 'POST':
        entry.votes += 1
        entry.save()
        messages.success(request, 'Your vote has been counted!')
        return redirect(reverse('competition_detail', args=[entry.competition.id]))
    return HttpResponse('Invalid request', status=400)

@login_required
def add_entry(request, competition_id):
    competition = Competition.objects.get(id=competition_id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        Entry.objects.create(competition=competition, user=request.user, title=title, description=description, image=image)
        messages.success(request, 'Entry added successfully!')
        return redirect(reverse('competition_detail', args=[competition.id]))
    return render(request, 'add_entry.html', {'competition': competition})
