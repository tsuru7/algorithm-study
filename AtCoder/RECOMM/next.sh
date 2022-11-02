
for f in A B C D E F G H I J K L M N;
do
  if [ ! -e ${f}.py ]; then
    cp `dirname $0`/template.py ./${f}.py
    break
  fi
done
