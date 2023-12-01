from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm
def index(request):
    entries = Entry.objects.order_by('-date_posted')

    context = {'entries' : entries}

    return render(request, 'entries/index.html', context)

def add(request):
    
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = EntryForm()  

    context = {'form':form}

    return render(request, 'entries/add.html', context)


def edit(request, entry_id):
    entries = Entry.objects.get(pk=entry_id)
    form = EntryForm(request.POST or None, instance=entries)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'entries/edit.html', {'entries':entries,'form':form})

def delete(request, entry_id):
	venue = Entry.objects.get(pk=entry_id)
	venue.delete()
	return redirect('home')		
