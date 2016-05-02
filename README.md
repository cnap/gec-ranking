# Ground Truth for Grammatical Error Correction Metrics


This repository contains a python implementation of the GLEU metric
(**G**eneral **L**anguage **E**valuation **U**nderstanding), which
can be used for any monolingual "translation" task. It also contains
human rankings of the CoNLL-14 Shared Task system output as well as
scripts to evaluate the rankings to extract an absolute system
ranking.

These results were described in our ACL 2015 paper:

> Courtney Napoles, Keisuke Sakaguchi, Joel Tetreault, and Matt
Post. 2015. Ground Truth for Grammatical Error Correction
Metrics. In *Proc. of the 53rd Annual Meeting of the Association
for Computational Linguistics*, pages 588-593. ACL.  ([pdf](http://www.aclweb.org/anthology/P/P15/P15-2097.pdf))

Please cite this work when using this data or the GLEU metric.

    @InProceedings{napoles-EtAl:2015:ACL-IJCNLP,
      author    = {Napoles, Courtney  and  Sakaguchi, Keisuke  and  Post, Matt  and  Tetreault, Joel},
      title     = {Ground Truth for Grammatical Error Correction Metrics},
      booktitle = {Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 2: Short Papers)},
      month     = {July},
      year      = {2015},
      address   = {Beijing, China},
      publisher = {Association for Computational Linguistics},
      pages     = {588--593},
      url       = {http://www.aclweb.org/anthology/P15-2097}
    }

## Instructions

### 1. Obtain the raw system output

The rankings found in the gec-ranking-data correspond to the 12 system outputs
from the CoNLL-14 Shared Task on Grammatical Error Correction, which can be 
downloaded from <http://www.comp.nus.edu.sg/~nlp/conll14st.html>.

Human judgments are located in `gec-ranking/data`.

### 2. Run TrueSkill

To get the human rankings, run TrueSkill (which can be downloaded from
<https://github.com/keisks/wmt-trueskill>) on `all_judgments.csv`, following
the instructions in the TrueSkill readme.

### 3. Calculate metric scores

GLEU is included in `gec-ranking/scripts`. To obtain the GLEU scores for 
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

---

# Important Update

There was an error in the calculation of the GLEU denominator, which was corrected in the 10 March 2016 commit.
Since then, we have identified a problem with the GLEU metric as the number of references increases. We are currently addressing this issue and will post a thorough explanation as well as revised results from our ACL 2015 paper.

---

Please contact Courtney Napoles (<courtneyn@jhu.edu>) with any questions.

Last updated 2 May 2016
