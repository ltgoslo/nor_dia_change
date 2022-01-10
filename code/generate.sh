#! /bin/bash

export HEADER="lemma\tpos\tdate\tgrouping\tidentifier\tdescription\tcontext\tindexes_target_token\tindexes_target_sentence"
export BIN1="1929-1965"
export BIN2="1970-2015"
#export BIN1="1980-1990"
#export BIN2="2012-2019"

while read p; do
  export WORD=$p
  echo ${WORD}
  echo -e ${HEADER} > ${WORD}.csv
  zcat tsvs/${BIN1}_${WORD}_NOUN.tsv.gz | shuf | grep -v lemma | grep -F -v ^ | head -n 11 >> ${WORD}.csv
  zcat tsvs/${BIN2}_${WORD}_NOUN.tsv.gz | shuf | grep -v lemma | grep -F -v ^ | head -n 11 >> ${WORD}.csv

done <${1}


