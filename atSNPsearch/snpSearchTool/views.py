from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import ScoresRow
from django.core.urlresolvers import reverse

#works..
def index(request):
  #accessing snp data from the database:
  snp_list = ScoresRow.objects.order_by('-snpid')[:5]
  output = ', '.join(s.snpid for s in snp_list)
  context = { 'snp_list' : snp_list, 'output_str' : output  }
  #the following 2 lines were replaced by 'render'
  #template = loader.get_template('snpSearchTool/index.html')
  #return HttpResponse(template.render(context, request))
  return render(request, 'snpSearchTool/index.html', context)

#The snpid should be replaced by
#all of the different search input controls that have been discussed.
#FIRST ITERATION of this view.


#works
def results(request, requested_snpid):
  return HttpResponse("going to check out the results when you ask for %s" % requested_snpid) 



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


#renders some conrtrols that make other requests?
def controlset(request):
  allRows = ScoresRow.objects.all() 
  return render(request, 'snpSearchTool/controlset.html', { 'all_scores_rows' : allRows }   )



#used to handle form input for a lookup
#maybe a cleaner way to do this?
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
