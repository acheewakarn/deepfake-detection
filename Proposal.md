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

We aren't certain about what would be the input to our model yet but one of the possibility is that we will analyze the change of in pixels of a specific area in the video per a number of frame. For example, if a video contain a person, we will analyze only the area of the video where the person's face is present.


## Output Behavior of the System

The system will output the likelihood, in percentage, that a video (an MP4 file) is FAKE and a boolean result, 1 for FAKE and 0 for REAL, of the video.


## Evaluation Metric for Success

To consider the model to be successful, it should be able to correctly identify whether an MP4 file contains deepfake 50% of the time.
