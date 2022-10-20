year=`date +%Y`
month=`date +%m`
day=`date +%d`
mkdir -p $year/$month/$day
cp -i template.py $year/$month/$day/A.py
