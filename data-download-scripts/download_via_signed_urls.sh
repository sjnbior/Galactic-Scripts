declare -a urls=( 
   # place list of sign urls here (not included as publically accessible for the first week)
   # e.g.:
   # https://storage.googleapis.com/biorelate_galactic_data_2022_03/aggregate.csv.gz?x-goog-signature...
   # https://storage.googleapis.com/biorelate_galactic_data_2022_03/aggregate2context.csv.gz?x-goog-signature...
   # https://storage.googleapis.com/biorelate_galactic_data_2022_03/aggregate_binding.csv.gz?x-goog-signature...
)


for URL in "${urls[@]}"
do
   FILE=`echo $URL | awk -F 'https://storage.googleapis.com/biorelate_galactic_data/2022_01/|\?' '{print $2}'`
   wget -O $FILE $URL  # &
done


