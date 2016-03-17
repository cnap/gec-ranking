#!/bin/bash

mydir="$HOME/research/gec/gec-annotations/data/no_merge"
files="$mydir/N
$mydir/expert_fluency 
$mydir/A
$mydir/[ANte]
$mydir/expert_min
$mydir/turker_min
$mydir/turker_fluency"

for i in 0 1 2 3; do
    for f in $files; do
	echo $f 1>&2
	bn=`basename $f`
	cmd="python scripts/compute_gleu \
	       -s $mydir/source \
	       -o $mydir/official_submissions/* \
	       -r $f* --version $i"
 	#awk -v ref=\"$bn\" '{print \"GLEU\"$2\"_\"ref\" err-corr nucle14 \"$1,$3}'"
	eval $cmd
    done
done
