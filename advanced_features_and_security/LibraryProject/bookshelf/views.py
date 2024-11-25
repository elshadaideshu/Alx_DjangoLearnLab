# views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from .forms import DocumentForm  # Assume you have a form for Document

@permission_required('your_app.can_view', raise_exception=True)
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'your_app/document_list.html', {'documents': documents})

@permission_required('your_app.can_create', raise_exception=True)
def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'your_app/document_form.html', {'form': form})

@permission_required('your_app.can_edit', raise_exception=True)
def document_edit(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'your_app/document_form.html', {'form': form})

@permission_required('your_app.can_delete', raise_exception=True)
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'your_app/document_confirm_delete.html', {'document': document})
# views.py
# Permissions are enforced using the @permission_required decorator.
# Users must have specific permissions based on their assigned groups:
# - Editors: can_create, can_edit
# - Viewers: can_view
# - Admins: can_view, can_create, can_edit, can_delete