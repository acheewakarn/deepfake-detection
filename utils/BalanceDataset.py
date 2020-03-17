import os
import json


def CreateBalanceMetadata():
    new_metadata = {}
    real = 0
    metadata = {}

    with open('metadata.json') as f:
        metadata = json.load(f)

    for key in metadata:
        if metadata[key]['label'] == 'REAL':
            real += 1
            new_metadata[key] = metadata[key]

    for key in metadata:
        if real > 0 and metadata[key]['label'] == 'FAKE':
            new_metadata[key] = metadata[key]
            real -= 1

    with open('new_metadata.json', 'w') as f:
        json.dump(new_metadata, f)

    return new_metadata


def RemoveFilesNotInMetadata(metadata):
    metadata = {}

    with open('new_metadata.json') as f:
        metadata = json.load(f)
    
    for fname in os.listdir():
        if fname[10:] == '.mp4' and fname not in metadata:
            print('Removing ' + fname + '...')
            os.remove(fname)

    
def GetRealFakeCount(new_metadata):
    real = 0
    fake = 0
    for key in new_metadata:
        if new_metadata[key]['label'] == 'FAKE':
            fake+=1
        else: 
            real+=1
    
    print('There are %d Real vids and %d Fake vids.' %(real, fake))



data_sets = ['example_data_folder_00', 'example_data_folder_01' ] ## INSERT THE NAME OF FOLDERS CONTAINING VIDEOS AND METADATA IN THE LIST

for data_set in data_sets:
    os.chdir('INSERT DIR TO DATA FOLDER HERE' + data_set)
    new_metadata = CreateBalanceMetadata()
    RemoveFilesNotInMetadata(new_metadata)
    GetRealFakeCount(new_metadata)




