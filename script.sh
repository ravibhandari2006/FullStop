#Usage: <./script.sh> <gtfile> <testFile> <WindowSize> <Threshold>
gtFile=$1
testFile=$2
testFile="${testFile%.*}"
winSize=$3
threshold=$4
x="thresh_"$testFile"_"$threshold"_algo2.txt"
y="refined_"$gtFile".txt"
#echo $x
./classify_gt.py $gtFile $winSize > $y
./script2.py $testFile.txt $winSize $threshold > $x
./compare.py $y $x $winSize
