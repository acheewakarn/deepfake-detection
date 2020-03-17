import os
import numpy as np
import json
import subprocess
from sklearn.metrics import f1_score, accuracy_score
from utils import *

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"  # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def inference(data_set):
    os.chdir('INSERT DIR OF EXTRACTED AUDIO')
    audioFiles = os.listdir()
    os.chdir('INSERT DIR WHERE FAKE AUDIO CODE ARE')

    # data_dir = "../data/inference_data/"
    data_dir = 'INSERT DIR OF EXTRACTED AUDIO'
    mode = "unlabeled"  # real, fake, or unlabeled
    pretrained_model_name = 'saved_model_240_8_32_0.05_1_50_0_0.0001_100_156_2_True_True_fitted_objects.h5'
    print(f"Loading inference data from {os.path(data_dir)}")
    print(f"Loading pretrained model {pretrained_model_name}")


    # preprocess the files
    processed_data = preprocess_from_ray_parallel_inference(data_dir, mode, use_parallel=True)
    processed_data = sorted(processed_data, key = lambda x: len(x[0]))

    # Load trained model
    discriminator = Discriminator_Model(load_pretrained=True, saved_model_name=pretrained_model_name, real_test_mode=False)

    # Do inference
    if mode == 'unlabeled':
        # Visualize the preprocessed data
        plot_spectrogram(processed_data[0], path='visualize_inference_spectrogram.png')
        
        audio_data = discriminator.predict_labels(processed_data, audioFiles, raw_prob=True, batch_size=20)
        
        os.chdir('INSERT DIR OF EXTRACTED AUDIO')
    
        with open('new_metadata_audio.json', 'w') as fp:
            json.dump(audio_data, fp)
            print(len(audio_data))
        
        print('Audio Prediction Finished.')    

    else:
        features = [x[0] for x in processed_data]
        labels = [x[1] for x in processed_data]
        preds = discriminator.predict_labels(features, threshold=0.5, batch_size=1)
        print(f"Accuracy on data set: {accuracy_score(labels, preds)}")

        all_filenames = sorted(os.listdir(os.path(data_dir)))

        if mode == 'real':
            # True Positive Examples
            ind_tp = np.equal((preds + labels).astype(int), 2)
            ind_tp = np.argwhere(ind_tp == True).reshape(-1, )
            tp_filenames = [all_filenames[i] for i in ind_tp]
            print(f'correctly predicted filenames: {tp_filenames}')

            # False Negative Examples
            ind_fn = np.greater(labels, preds)
            ind_fn = np.argwhere(ind_fn == True).reshape(-1, )
            fn_filenames = [all_filenames[i] for i in ind_fn]
            print(f'real clips classified as fake: {fn_filenames}')
        elif mode == 'fake':
            # True Negative Examples
            ind_tn = np.equal((preds + labels).astype(int), 0)
            ind_tn = np.argwhere(ind_tn == True).reshape(-1, )
            tn_filenames = [all_filenames[i] for i in ind_tn]
            print(f'correctly predicted filenames: {tn_filenames}')

            # False Positive Examples
            ind_fp = np.greater(preds, labels)
            ind_fp = np.argwhere(ind_fp == True).reshape(-1, )
            fp_filenames = [all_filenames[i] for i in ind_fp]
            print(f'fake clips classified as real: {fp_filenames}')


data_sets = [ '21']
for data_set in data_sets:
    inference(data_set)
    print('%s complete...' %data_set)