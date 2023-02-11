year=`date +%Y`
month=`date +%m`
day=`date +%d`
mkdir -p $year/$month/$day
for i in {1..8} ; do
    cp -a ~/repos/AtCoder/TEMPLATE/A.py $year/$month/$day/${i}.py
done
