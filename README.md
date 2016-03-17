# Ground Truth for Grammatical Error Correction Metrics


This repository contains a python implementation of the GLEU metric
(**G**eneral **L**anguage **E**valuation **U**nderstanding), which
can be used for any monolingual "translation" task. It also contains
human rankings of the CoNLL-14 Shared Task system output as well as
scripts to evaluate the rankings to extract an absolute system
ranking.

These results were described in our ACL 2015 paper

> Courtney Napoles, Keisuke Sakaguchi, Joel Tetreault, and Matt
Post. 2015. Ground Truth for Grammatical Error Correction
Metrics. In *Proc. of the 53rd Annual Meeting of the Association
for Computational Linguistics*, pages 588-593. ACL.  ([pdf](http://www.aclweb.org/anthology/P/P15/P15-2097.pdf)|[bib](http://www.aclweb.org/anthology/P/P15/P15-2097.bib)).

Please cite this work when using our metric or data.

## Instructions

<h4>1. Obtain the raw system output</h4>

The rankings found in the gec-ranking-data correspond to the 12 system outputs
from the CoNLL-14 Shared Task on Grammatical Error Correction, which can be 
downloaded from <http://www.comp.nus.edu.sg/~nlp/conll14st.html>.

Human judgments are located in gec-ranking/data.

<h4>2. Run TrueSkill</h4>

To get the human rankings, run TrueSkill (which can be downloaded from
<https://github.com/keisks/wmt-trueskill>) on all_judgments.csv, following
the instructions in the TrueSkill readme.

<h4>3. Calculate metric scores</h4>

GLEU is included in gec-ranking/scripts. To obtain the GLEU scores for 
system output, run the following command:

```
./compute_gleu -s source_sentences -r reference [reference ...] \
        -o system_output [system_output ...] -n 4 -l 0.0
```
    
where each file contains one sentence per line. GLEU can be run with multiple
references. To get the GLEU scores of multiple outputs, include the path to 
each system output file. GLEU was developed using Python 2.7.

I-measure scores were taken from Felice and Briscoe's 2015 NAACL paper,
*Towards a standard evaluation method for grammatical error detection and 
correction*. The I-measure scorer can be downloaded from 
<https://github.com/mfelice/imeasure>.

M2 scores were calculated using the official scorer (3.2) of the CoNLL-2014 Shared Task (<http://www.comp.nus.edu.sg/~nlp/sw/>).
--
# Update, 17 March 2016

There was an error in the calculation of the GLEU denominator, which was corrected in the 10 March 2016 commit.
Since then, we have identified a problem with the GLEU metric as the number of references increases. We are currently addressing this issue and will post a thorough explanation as well as revised results from our ACL 2015 paper.


--
Courtney Napoles,  <courtneyn@jhu.edu>  
21 June 2015, updated 17 March 2016