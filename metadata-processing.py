# Import the metadata 
def processMetadata(file):
    jsonFile = open(file)
    data = json.load(jsonFile)

    labels = {}
    testIDs = []
    validIDs = []
    # every fifth key is validID, the rest are testID
    validationCount = 0
    for oldKey in data.keys():
        newKey = oldKey[:-4]
        if validationCount % 5 == 0:
          validIDs.append(newKey)
        else:
          testIDs.append(newKey)

        labels[newKey] = {
            # labels = 1 if fake,
            'label': int(data[oldKey]['label'] == 'FAKE'),
            'audioPrediction': data[oldKey]['fakeAudioPrediction']
        }

        validationCount += 1
    return (testIDs, validIDs, labels)


# Save metadata sorted into test and valid sets.
# arg2 = processed-metadata.json
def createTestValidMetadata(metadataPath, newMetadataPath):
    testObject = {}
    validObject = {}

    (testIDs, validIDs, labels) = processMetadata(metadataPath)

    for ID in testIDs:
        testObject[ID] = {
            'label': labels[ID]['label'],
            'fakeAudioPrediction': labels[ID]['audioPrediction']
        }

    for ID in validIDs:
        validObject[ID] = {
            'label': labels[ID]['label'],
            'fakeAudioPrediction': labels[ID]['audioPrediction']
        }

    metadataObject = {
        'test': testObject,
        'valid': validObject
    }
    with open(newMetadataPath, 'w') as outfile:
        json.dump(metadataObject, outfile)


# Merge Two processed metadata files to keep constant test and
# validation sets.
# originalFIle = 'processed-metadata.json'
# addFile = './new_dataset/merged_metadata_12_to_22.json'
# outputFile = 'processed-metadata.json'
def mergeMetadataFiles(originalFile, addedFile, outputFile):
    metadata = {}
    with open(originalFile, 'r') as file:
        metadata = json.load(file)

        (testIDs, validIDs, labels) = processMetadata(
            './new_dataset/merged_metadata_12_to_22.json')

        for ID in testIDs:
            metadata['test'][ID] = {
                'label': labels[ID]['label'],
                'fakeAudioPrediction': labels[ID]['audioPrediction']
            }

        for ID in validIDs:
            metadata['valid'][ID] = {
                'label': labels[ID]['label'],
                'fakeAudioPrediction': labels[ID]['audioPrediction']
            }

        print(len(metadata['test'].keys()))
        print(len(metadata['valid'].keys()))

    with open(outputFile, 'w') as outfile:
        json.dump(metadata, outfile)

# Sometimes there are data points that are incorrectly processed.  This removes those
# datapoints from the metadata file so they do not get used during training.
def removeIncorrectDataPoints(metadataPath):
    metadata = {}
    with open(metadataPath, 'r') as file:
        metadata = json.load(file)
        count = 0
        for ID in list(metadata['test'].keys()):
            imagePath = os.path.join(
                './merged_data', os.path.join(ID + '-data', ID + '_face' + str(89) + '.jpg'))
            #print(imagePath)

            if not os.path.isfile(imagePath):
                del metadata['test'][ID]
                count += 1

        for ID in list(metadata['valid'].keys()):
            imagePath = os.path.join(
                './merged_data', os.path.join(ID + '-data', ID + '_face' + str(89) + '.jpg'))
            #print(imagePath)

            if not os.path.isfile(imagePath):
                del metadata['valid'][ID]
                count += 1
        print(count)
        print(len(metadata['test'].keys()))
        print(len(metadata['valid'].keys()))

    with open(metadataPath, 'w') as outfile:
        json.dump(metadata, outfile)
