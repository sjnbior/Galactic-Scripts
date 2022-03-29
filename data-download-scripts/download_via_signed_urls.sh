declare -a urls=( 
   # place list of sign urls here (not included as publically accessible for the first week)
   # e.g.:
   # https://storage.googleapis.com/biorelate_galactic_data_2022_03/aggregate.csv.gz?x-goog-signature...
   # https://storage.googleapis.com/biorelate_galactic_data_2022_03/aggregate2context.csv.gz?x-goog-signature...
   # https://storage.googleapis.com/biorelate_galactic_data_2022_03/aggregate_binding.csv.gz?x-goog-signature...
)


for URL in "${urls[@]}"
do
   YEAR=`echo $URL| cut -d'_' -f 4`
   MONTH=`echo $URL| cut -d'_' -f 5| cut -d'/' -f 1`
   PATTERN=`echo 'https://storage.googleapis.com/biorelate_galactic_data_'$YEAR'_'$MONTH'/|\?'`
   FILE=`echo $URL | awk -F $PATTERN '{print $2}'`
   echo $FILE
   wget -O $FILE $URL  # &
done