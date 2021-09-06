from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DiaryEntry
from .forms import EntryCreationForm
from user.forms import UserConfigForm

def entry_required(f):
    def wrap_function(request, entry_id, *args, **kwargs):
        try:
            entryInstance = DiaryEntry.objects.get(uuid=entry_id, author=request.user)
        except:
            return redirect('missing')
        return f(request, entry_id, *args, **kwargs, entryInstance=entryInstance)
    return wrap_function


# @login_required
def dashboard(request):
    if request.user.is_authenticated:
        # if you're logged in and you POSTed a form...
        if request.method == 'POST':
            # is it a creation form?
            # if 'creation_form' in request.POST:
            form = EntryCreationForm(request.POST)
            if form.is_valid():
                newEntry = DiaryEntry(title=form.cleaned_data['title'],
                    location=form.cleaned_data['location'], author=request.user)
                newEntry.save()
                return redirect('edit_entry', entry_id=newEntry.uuid)
            # if 'config_form' in request.POST
                # user.views.save_user_config(request.POST, request.user)

        # if method is GET
        entryList = DiaryEntry.objects.filter(author=request.user).order_by('dateTime')
        creationForm = EntryCreationForm()
        configForm = UserConfigForm(initial={'theme': request.user.theme, 'font_size': request.user.font_size})
        return render(request, 'diary/dashboard.html', {'entry_list': entryList,
            'creation_form': creationForm, 'config_form': configForm})
    else:
        return render(request, 'diary/dashboard.html', {})

@login_required
@entry_required
def entry(request, entry_id, entryInstance):
    if request.method == 'POST':
        entryToDelete = DiaryEntry.objects.get(uuid=request.POST['delete'], author=request.user)
        # imagesToDelete = Image.objects.filter(entry=entryToDelete)

        # imagesToDelete.delete()
        entryToDelete.delete()
        return redirect('dashboard')
    return render(request, 'diary/entry.html', {'entry': entryInstance})

# @login_required
# def create_entry(request):
#     if request.method == 'POST':
#         form = EntryCreationForm(request.POST)
#         if form.is_valid():
#             newEntry = DiaryEntry(title=form.cleaned_data['title'], location=form.cleaned_data['location'], author=request.user)
#             newEntry.save()
#             return redirect('edit_entry', entry_id=newEntry.uuid)
#     else:
#         form = EntryCreationForm()
#
#     return render(request, 'diary/create_entry.html', {'date_created': timezone.now(), 'form': form})

@login_required
@entry_required
def edit_entry(request, entry_id, entryInstance):
    if request.method == 'POST':
        # If no error, then it is an autosave update
        try:
            request.POST['is_autosave_update']

            entryInstance.content = request.POST['content']
            entryInstance.save()
            return JsonResponse(data={}, status=200)

        except KeyError:
            form = EditorForm(request.POST)
            if form._errors:
                return redirect('missing', {'error': form._errors})

            content = form.data['editor']
            # files = form.files
            entryInstance.content = content
            entryInstance.save()
            return redirect('entry', entry_id=entryInstance.uuid)
    else:
        form = EditorForm()
    return render(request, 'diary/edit.html', {'entry': entryInstance, 'form': form,
        'initial_content': entryInstance.content})

def missing(request):
    return render(request, 'diary/missing.html')
