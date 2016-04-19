from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import ScoresRow
from django.core.urlresolvers import reverse
from django.views import generic

#uses a generic view
class IndexView(generic.ListView):
  template_name = 'snpSearchTool/index.html'
  context_object_name = 'snp_list'

  def get_queryset(self):
    return ScoresRow.objects.order_by('-snpid')[:5]

#uses a generic view 
#expects the url parameter to be a primary key called 'pk'
class DetailView(generic.DetailView):
  model = ScoresRow
  template_name = 'snpSearchTool/detail.html'
  context_variable_name = 'snp_scores_row'


#renders some conrtrols that make other requests?
def controlset(request):
  allRows = ScoresRow.objects.all() 
  return render(request, 'snpSearchTool/controlset.html', { 'all_scores_rows' : allRows }   )


#used to handle form input for a lookup
#redirect on successful lookup is apparently the thing to do.
def lookup_one_snp(request ):
   #snp_scores_row = get_object_or_404(ScoresRow, snpid=requested_snpid) 
   snpid_in = request.POST['requested_snpid']
   try:
     looked_up_row = ScoresRow.objects.get(snpid=snpid_in)
     id_to_use = looked_up_row.id
   except (KeyError, ScoresRow.DoesNotExist):
     return HttpResponse("the snp id " + snpid_in + "isn't here")
     #consider redisplying the control form.
   else:
     return HttpResponseRedirect(reverse('snpSearchTool:detail',  args=(id_to_use,)  ))

def results(request, requested_snpid):
  return HttpResponse("going to check out the results when you ask for %s" % requested_snpid) 

"""  
#detail should show the detail about ONE ScoresRow identified by snpid.
def detail(request, id_of_scoresrow):  #requested_snpid comes out of the url.
  try:
    snp_scores_row = ScoresRow.objects.get(id= id_of_scoresrow)
  except (KeyError, ScoresRow.DoesNotExist):
    raise Http404("Scores row for requested snpid does not exist")
  return render(request, 'snpSearchTool/detail.html', 
            { 'id_of_scoresrow' : id_of_scoresrow,
             'snp_scores_row' : snp_scores_row,
             'more_context'   : "More Context!", })
            #return HttpResponse("detail for snpid: %s" % requested_snpid)
"""

"""
def index(request):
  snp_list = ScoresRow.objects.order_by('-snpid')[:5]
  output = ', '.join(s.snpid for s in snp_list)
  context = { 'snp_list' : snp_list, 'output_str' : output  }
  return render(request, 'snpSearchTool/index.html', context)

"""
