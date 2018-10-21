# create desc json files
python create_desc_json_lapsbm.py data/lapsbm/ Test_dataset.csv
python create_desc_json_TTS_Portuguese.py data/TTS-Portuguese/texts.csv TTS-Portuguese.csv
python create_desc_json_voxforge.py data/voxforge/ Voxforge.csv
python create_desc_json_sid.py data/sid/ Sid.csv
# Merging the Datasets
cat Sid.csv > Train_dataset.csv
tail -n +2 TTS-Portuguese.csv >> Train_dataset.csv
tail -n +2 Voxforge.csv >> Train_dataset.csv
echo '********************************************************************'
echo 'The datasets were successfully generated'
echo 'Use Train_dataset.csv for train and Test_dataset.csv for test'
echo '********************************************************************'


