from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict

from .forms import SnipeForm
from .models import SnipeModel

# Create your views here.

def dashboard_control(request, *args, **kwargs):
    snipe_items = SnipeModel.objects.all()
    form = SnipeForm()

    if request.method == "POST":
        form = SnipeForm(request.POST)
        if form.is_valid():
            SnipeModel.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
        return render(request,'snipe_control.html', context={'snipe_items': snipe_items, 'form': form})
    snipe_items = SnipeModel.objects.all()
    return render(request, 'snipe_control.html', context={'snipe_items': snipe_items, 'form': form})


def delete_snipe(request, pk):
    snipe_item = get_object_or_404(SnipeModel, pk=pk)

    if request.method == "POST":
        snipe_item.delete()
        return redirect('/dashboard/')


def edit_snipe(request, pk):
    snipe_item = get_object_or_404(SnipeModel, pk=pk)
    form = SnipeForm(request.POST or None, instance=snipe_item, initial=model_to_dict(snipe_item))
    print(snipe_item)
    context = {'form': form}

    if form.is_valid():
        snipe_item = form.save(commit=False)
        snipe_item.save()
        context = {'form': form}
        return redirect('/dashboard/')

    else:
        context = {'form': form}
        return render(request, 'snipe_edit.html', context)
