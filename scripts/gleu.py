# Courtney Napoles
# <courtneyn@jhu.edu>
# 21 June 2015
# ##
# gleu.py
# 
# This script calculates the GLEU score of a sentence, as described in
# our ACL 2015 paper, Ground Truth for Grammatical Error Correction Metrics
# by Courtney Napoles, Keisuke Sakaguchi, Matt Post, and Joel Tetreault.
# 
# For instructions on how to get the GLEU score, call "compute_gleu -h"
#
# This script was adapted from bleu.py by Adam Lopez.
# <https://github.com/alopez/en600.468/blob/master/reranker/>

import math
from collections import Counter

def get_ngram_counts(sentence,n) :
    return Counter([tuple(sentence[i:i+n]) for i in xrange(len(sentence)+1-n)])

# Collect BLEU-relevant statistics for a single hypothesis/reference pair.
# Return value is a generator yielding:
# (c, r, numerator1, denominator1, ... numerator4, denominator4)
# Summing the columns across calls to this function on an entire corpus will
# produce a vector of statistics that can be used to compute BLEU or GLEU
def gleu_stats(hypothesis, references, source,order=4,weight=0.1):
    #  print source
    #  print hypothesis
    #  print references[0]
  hlen=len(hypothesis)
  rlen = hlen
  # set the reference length to be the reference length closest to the hyp length 
  for r in references :
      if abs(len(r)-hlen) < abs(rlen - hlen) :
          rlen = len(r)
  yield rlen
  yield hlen
  
  for n in xrange(1,order+1):
    h_ngrams = get_ngram_counts(hypothesis,n)
    s_ngrams = get_ngram_counts(source,n)
    # initialize r_ngrams with the first rereference
    r_ngrams = get_ngram_counts(references[0],n)
    # then update for each next reference
    for r in range(1,len(references)) :
        new_r_ngrams = get_ngram_counts(references[r],n)
        for nn in new_r_ngrams.elements() :
            if new_r_ngrams[nn] > r_ngrams.get(nn,0) :
                r_ngrams[nn] = new_r_ngrams[nn]
    r_ngram_diff = r_ngrams - s_ngrams
    s_ngram_diff = s_ngrams - r_ngrams
    
    yield max([sum((h_ngrams & r_ngram_diff).values()), 0])+max([sum((h_ngrams & r_ngrams).values()), 0]) - weight * max([sum((h_ngrams & s_ngram_diff).values()), 0])
    yield max([sum(r_ngram_diff.values()), 0]) + max([hlen+1-n, 0]) 

# Compute GLEU from collected statistics obtained by call(s) to gleu_stats
def gleu(stats):
  if len(filter(lambda x: x==0, stats)) > 0:
    return 0
  (c, r) = stats[:2]
  log_gleu_prec = sum([math.log(float(x)/y) for x,y in zip(stats[2::2],stats[3::2])]) / 4.
  return math.exp(min([0, 1-float(r)/c]) + log_gleu_prec)
