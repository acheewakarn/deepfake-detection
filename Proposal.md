# [Deepfake Detection Challenge](https://www.kaggle.com/c/deepfake-detection-challenge/data)
Identify videos with facial or voice manipulations


## Team Members

Anon Cheewakarn (acheewak)

Ellen Kalvan (ekalvan)

Jesse Schmidt (jbschmid)


## Dataset

We will be working with ~470GB worth of MP4 files that are divided into smaller sets of ~10GB per set. Each set is accompanied by a metadata.json with 4 fields for each MP4 file. 

The 4 fields are:
1. `filename` - name of the MP4 file
2. `label` - (REAL/FAKE)
3. `original` - filename of the original file if the file is FAKE
4. `split` - Always set to "train"

## Input

An MP4 file that needs to be classified as real or fake.

## Output Behavior of the System

The system will output the likelihood, in percentage, that a video (an MP4 file) is FAKE.

## Evaluation Metric for Success

To consider the model to be successful, it should be able to correctly identify whether an MP4 file contains deepfake 80% of the time.
