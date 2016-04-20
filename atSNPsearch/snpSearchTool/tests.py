from django.test import TestCase
from django.core.urlresolvers import reverse


from .models import ScoresRow
#make sure that when a snp is entered it can be retrieved?




#create a scores row object and ensure that it 
#responds as expected.
class ScoresRowMethodTests(TestCase):
  def test_one_method(self): #which one?
    pass


def create_one_scores_row():
     return ScoresRow.objects.create(snpid="rs11111111",  motif="M.900.1.2", motif_len=12,
     log_lik_ref = 2.3, log_lik_snp = -1.10023, log_lik_ratio = 2.33333,
     log_enhance_odds = -0.33333, log_reduce_odds = 1.13, ref_start = 238992012,
     snp_start = 1292292, ref_end = 30030002, snp_end = 200048290, ref_strand =
     "+", snp_strand="-")


class IndexViewTests(TestCase):
  def test_that_index_loads(self):
    response = self.client.get(reverse('snpSearchTool:index'))
    self.assertEqual(response.status_code, 200)
    #self.assertContains(response, 'Some part of an expected response message.')
    #if we expect the context to be empty: 
    #self.assertQuerysetEqual(response.context['part_of_context'], [])  #empty list, see?



class DetailViewTests(TestCase):
  def test_that_detail_loads(self):
    sr = create_one_scores_row()
    response = self.client.get(reverse('snpSearchTool:detail', args=(sr.id,)))
    self.assertEqual(response.status_code, 200)   
    #self.assertContains(response, (part of the hardcoded ScoresRow that I put in up top, here) 

  def test_that_detail_does_not_load_for_missing_row(self):
    #figure out a reliable way for this to always give a 404 
    response = self.client.get(reverse('snpSearchTool:detail', args=(669699450,)))
    self.assertEqual(response.status_code, 404) 
