import numpy as np
import cv2
import os
from keras.utils import Sequence

class VideoDataGenerator(Sequence):
    def __init__(self, ids, labels, directory,
     batchSize=16, videoDim=(150, 150), audioDim=1, 
     fps=30, maxVideoLength=3, shuffle=True):
        self.directory = directory
        self.ids = ids                          # array of video names from metadata.json
        self.labels = labels                    # array of labels from metadata.json
        self.batchSize = batchSize              # Size of batches
        self.videoDim = videoDim                # dimension of input data
        self.audioDim = audioDim                # dimension of input data
        self.framesPerSec = fps                 # fps of video being loaded. (To num of images to load)
        self.maxVideoLength = maxVideoLength    # length of video in seconds. (To num of images to load)
        self.shuffle = shuffle                  # flag to set to shuffle after each epoch.
        self.on_epoch_end()

    # Returns the number of batches per epoch
    def __len__(self):
        return int(np.floor(len(self.ids) / self.batchSize))

    # Returns a single batch of data
    def __getitem__(self, index):
        # Get the indexes of the videoIDs data for this batch
        indexes = self.indexes[index*self.batchSize:(index+1)*self.batchSize]

        ids = [self.ids[i] for i in indexes]

        X, y = self.__data__generation(ids)

        return X, y

    # Scrambles the order of indexes for different batches every epoch
    def on_epoch_end(self):
        # Will be used to keep track of ids that have been
        # seen more than once.  This will indicate that there
        # are multiple faces in the video.
        self.idCount = {}
        # Makes np array of indexes
        self.indexes = np.arange(len(self.ids))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)


    def __data__generation(self, list_IDs_temp):
        # Initialization
        XImage = np.empty((self.batchSize, self.framesPerSec * self.maxVideoLength,  *self.videoDim))
        XAudio = np.empty((self.batchSize, 1))
        y = np.empty((self.batchSize), dtype=int)

        # Generate data
        for batchIndex, ID in enumerate(list_IDs_temp):
            j = 0
            
            for frameIndex in range(0,90):

              # open folder ID
              imagePath = os.path.join(self.directory, os.path.join(ID + '-data', ID + '_face' + str(frameIndex) + '.jpg'))
              
              # Make sure image exists.  If not print it out and break
              if not os.path.isfile(imagePath):
                print()
                print('   Size 0' + ' ID: ' + ID + ' frame: ' + str(frameIndex))
                break
              # Read image data to np
              IDimage = cv2.imread(imagePath)

              # Check if we have read too many photos already.
              if (frameIndex >= self.maxVideoLength * self.framesPerSec):
                break
                
              # Save image and normalize values
              XImage[batchIndex, j, ] = IDimage / 255
              j+=1

            # Get audio classification and data point labels.
            XAudio[batchIndex, ] = self.labels[ID]['audioPrediction']
            y[batchIndex] = self.labels[ID]['label']
              

        return [XImage, XAudio], y

 

