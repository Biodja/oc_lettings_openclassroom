from django.shortcuts import render , get_object_or_404
from .models import Letting

def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


#Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id eleifend. Praesent
#  lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor, est ut luctus congue, du
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo mattis ullamcorper ac no
def letting(request, letting_id):
    letting = get_object_or_404(Letting,id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)
