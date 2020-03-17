# Deepfake Detection

https://www.kaggle.com/c/deepfake-detection-challenge

# Folder Structure

#### /audio_model_replacements
This folder contains python files that will replace those from Dessa's Fake Audio Model. Simply place them in the directory where the original files are.

To download Dessa's Fake Audio Model,follow the setup instruction here: https://github.com/dessa-oss/fake-voice-detection

#### /notebooks
This directory contains Python notebook used for preprocessing data as well as all the variations of models we created.
  - data-extraction.ipynb: This notebook is used to extract/preprocess data from Kaggle Deepfake Detection Challenge.
  - models: They are all almost identical with slight variations.  The model that we had the most success with is v4 which is discussed in our paper.  To find the training results for notebook v[1-6] look in the /results directory.  When training model v1 we only had 1000 data points and had a much smaller primary dense layer.

#### /results
Each model notebook corresponds to a results subdirectory.  Inside of each directory you will find 2 files:
- `history.csv`
    - Contains the acc, loss, val_acc, and val_loss that resulted from running the corresponding model.
- `weights.h5`
    - The weights achieved while running the corresponding model so that training can continue.  These weights are only saved when the "best" val_acc so far has been seen.

There may be extra `weight.h5` files and this is so each training session does not overwrite the previous sessions weights.

#### /util

Helper modules for data processing and miscellaneous things
- processMetadata.py
        - Functions to process and integrate new metadata files into our current training and validation set. 
- VideoDataGenerator.py
        - Generator inherited from Keras.Sequence that helped us load video frames, audio classifications, and labels in 
        batches to be used with fit_generator. 
- balanceDataset.py
        - Simply goes through the metadata and remove fake videos until the dataset reaches 1:1 real/fake ratio
