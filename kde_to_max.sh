#!/bin/sh
#
# the next line is a "magic" comment that tells codine to use bash
#$ -S /bin/bash
#
# and now for some real work
#cd $PBS_O_WORKDIR
pwd
echo $SGE_TASK_ID
python2.6 kde_to_max.py $SGE_TASK_ID
