from django.shortcuts import render
from .models import Editor
from .forms import EditorForm


def index(request):
    form = EditorForm()
    contaxt = {'form': form}
    return render(request, 'project/index.html', contaxt)
