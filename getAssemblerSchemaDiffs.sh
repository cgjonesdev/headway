file=Xojo/AssemblerSchema.xml
monthStr="October"
yearInt=2016
monthInt=10
minDays=1
maxDays=31

for n in `seq $maxDays $minDays`; do
	echo -e "\n-------------------------------------------- $monthStr $n $yearInt --------------------------------------------\n" && git blame $file | grep $yearInt-$monthInt-$n;
done
