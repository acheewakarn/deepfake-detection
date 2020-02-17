# [Deepfake Detection Challenge](https://www.kaggle.com/c/deepfake-detection-challenge/data)
Identify videos with facial or voice manipulations


### Team Members
___
Anon Cheewakarn (acheewak)

Ellen Kalvan (ekalvan)

Jesse Schmidt (jbschmid)


### Dataset
___
We will be working with ~470GB worth of compressed MP4 files to train our model.  This large set of training data is divided into smaller  ~10GB sets. Each ~10GB set is accompanied by a metadata.json containing the following 4 fields for each MP4 file. 

The 4 fields are:
1. `filename` - name of the MP4 file
2. `label` - (REAL/FAKE)
3. `original` - filename of the original file if the file is FAKE
4. `split` - Always set to "train"

Included with the training data is a sample validation set with 400 videos that can be used after model training to test model behavior.  However, it may be worthwhile to save some of the labeled training data for this purpose instead of for training.

Each video from the training and validation set is 10 seconds long and contains a person, or multiple people, talking.

Since the dataset is so large, we’ll most likely start with a subset of the ~470GB training data.  If we decide to use the entire dataset we could either rent a machine from a cloud provider or put the entire dataset on an external hard drive and train on a local machine.

### Input
___
The input to our model will be an mp4 video that needs to be classified as REAL or FAKE.  The video will likely need to be processed to analyze both frames and audio for manipulations of the voice and face.  

### Output Behavior of the System
___
The system will determine a likelihood percentage that a video (MP4 file) is FAKE. The output will be a floating-point value (0 - 1.0) representing the probability that the video is FAKE.

### Evaluation Metric for Success
___
We will use two different metrics to evaluate our success
1. Successful Prediction / Total Prediction Ratio
1. F1 score

##### Successful Prediction / Total Prediction Ratio
Considering that our team has never dealt with machine learning models we have picked a modest success threshold.  A successful model should be able to correctly identify whether an MP4 file contains deepfake 75% of the time.

##### F1 Score
The F1 score is a common function used for the analysis of binary classification.
![equation](http://bit.ly/2TPoIqD)
`Precision` **p** is the ratio of correct positive classifications to positive classifications and `Recall` **r** is the ratio of correct positive classifications to all classifications that should have been positive. A perfect F1 score is 1 and while the worst is 0.  Again, keeping our success threshold modest an F1 score of .75 will be considered a success.


The competition uses the log loss function to score submissions. We will be optimizing for small log loss, and avoiding false positives at all costs. 

Explanation of log loss: https://www.kaggle.com/c/deepfake-detection-challenge/overview/evaluation
