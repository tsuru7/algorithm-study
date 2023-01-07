year=`date +%Y`
month=`date +%m`
day=`date +%d`
mkdir -p $year/$month
cp -a TEMPLATE $year/$month/$day

