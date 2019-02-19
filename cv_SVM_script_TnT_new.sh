#Usage: ./SVM_script.sh <alpha> <WindowSize_sec>
#1 2 3, 1 3 2, 2 3 1
rm final_all_day_night_data.txt
./ewma_accr.py Acc_15_30.txt $1 > ewma_Acc_15_30.txt
./ewma_accr.py Acc_17_30.txt $1 > ewma_Acc_17_30.txt
./ewma_accr.py Acc_21_30.txt $1 > ewma_Acc_21_30.txt
./ewma_accr.py Acc_24_30.txt $1 > ewma_Acc_24_30.txt
./ewma_accr.py Acc_25_30.txt $1 > ewma_Acc_25_30.txt
./ewma_accr.py Acc_29_30.txt $1 > ewma_Acc_29_30.txt
./ewma_accr.py Acc_30_30.txt $1 > ewma_Acc_30_30.txt
./ewma_accr.py Acc_31_30.txt $1 > ewma_Acc_31_30.txt

./trim_acc.py trim_gt_myvideo15_30.txt ewma_Acc_15_30.txt > trim_ewma_Acc_15_30.txt
./trim_acc.py trim_gt_myvideo17_30.txt ewma_Acc_17_30.txt > trim_ewma_Acc_17_30.txt
./trim_acc.py trim_gt_myvideo21_30.txt ewma_Acc_21_30.txt > trim_ewma_Acc_21_30.txt
./trim_acc.py trim_gt_myvideo24_30.txt ewma_Acc_24_30.txt > trim_ewma_Acc_24_30.txt
./trim_acc.py trim_gt_myvideo25_30.txt ewma_Acc_25_30.txt > trim_ewma_Acc_25_30.txt
./trim_acc.py trim_gt_myvideo29_30.txt ewma_Acc_29_30.txt > trim_ewma_Acc_29_30.txt
./trim_acc.py trim_gt_myvideo30_30.txt ewma_Acc_30_30.txt > trim_ewma_Acc_30_30.txt
./trim_acc.py trim_gt_myvideo31_30.txt ewma_Acc_31_30.txt > trim_ewma_Acc_31_30.txt

./script4.py trim_Algo5_OptFlow_myvideo15_3.txt trim_ewma_Acc_15_30.txt $2 >> final_all_day_night_data.txt
./script4.py trim_Algo5_OptFlow_myvideo17_3.txt trim_ewma_Acc_17_30.txt $2 >> final_all_day_night_data.txt
./script4.py trim_Algo5_OptFlow_myvideo21_3.txt trim_ewma_Acc_21_30.txt $2 >> final_all_day_night_data.txt
./script4.py trim_Algo4_OptFlow_myvideo24_15.txt trim_ewma_Acc_24_30.txt $2 >> day_all_day_night_data.txt
./script4.py trim_Algo4_OptFlow_myvideo25_15.txt trim_ewma_Acc_25_30.txt $2 >> day_all_day_night_data.txt
./script4.py trim_Algo4_OptFlow_myvideo29_15.txt trim_ewma_Acc_29_30.txt $2 >> day_all_day_night_data.txt
./script4.py trim_Algo4_OptFlow_myvideo30_15.txt trim_ewma_Acc_30_30.txt $2 >> day_all_day_night_data.txt
./script4.py trim_Algo4_OptFlow_myvideo31_15.txt trim_ewma_Acc_31_30.txt $2 >> day_all_day_night_data.txt

rm temp1.txt temp2.txt
python -u cv_all_fit.py final_all_day_night_data.txt > new_temp.txt
./sum_calc.py new_temp.txt
