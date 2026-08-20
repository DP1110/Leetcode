cols=$(head -1 file.txt | wc -w)
for i in $(seq 1 $cols); do
  cut -d' ' -f$i file.txt | paste -s -d' '
done