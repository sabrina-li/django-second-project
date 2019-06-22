from django.shortcuts import render,get_object_or_404
from .models import Spice,SpiceMixes

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# def index(request):
#     return HttpResponse("Hello, world. You're at the spices index.")

def spice_mix(request,spice_mix_id):
    spice_mix = get_object_or_404(SpiceMixes, pk=spice_mix_id)
    try:
        spices_list = spice_mix.spice_set.all()
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'spice_mix': spice_mix,
            'error_message': "You something is wrong....",
        })
    else:
        context = {
            'spice_mix':spice_mix
        }
        return render(request,'mixes/details.html',context)


def spice(request,spice_id):
    spice = Spice.objects.filter(pk=spice_id)
    context = {'spice': spice[0]}
    return render(request, 'spice/index.html', context)
    # return HttpResponse( "this is the spice list No. "+ str(spice_id))

def spice_mix_list(request):
    # return HttpResponse("this is the spice_mix list No. "+ str(spice_mix_id))
    all_spice_mixes = SpiceMixes.objects.order_by('id')[:5]
    context = {'spice_mix_list': all_spice_mixes}
    return render(request, 'mixes/index.html', context)
    # return HttpResponse( output )

def add(request):
    # return HttpResponse("this is the spice_mix list No. "+ str(spice_mix_id))
    spices = Spice.objects.all()
    context = {'spices': spices}
    return render(request, 'add.html', context)
    # return HttpResponse( output )

def add_post(request):
    #create mix and save to DB:
    spice_mix_name = request.POST['spice_mix_name']
    new_mix = SpiceMixes(spice_mix_name=spice_mix_name)
    new_mix.save()

    #create new spice and save to DB:
    spice_name = request.POST['spice_name']
    spice_flavour_profile = request.POST['spice_flavour_profile']
    new_spice = Spice(spice_name=spice_name,spice_flavour_profile=spice_flavour_profile)
    new_spice.save()

    #get spices list:
    spice_id = request.POST['spice']
    print(spice_id)
    spice = Spice.objects.get(pk=spice_id)
    print(spice)
    # try:
    new_mix.spice_set.add(spice)
    new_mix.spice_set.add(new_spice)

    new_spice.spicemixes_set.add(new_mix)
    spice.spicemixes_set.add(new_mix)

    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     # return 
    return HttpResponseRedirect('/spices')