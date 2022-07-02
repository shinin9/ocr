import random
import os
import json

file = json.load(open('data/images.json'))

ocr_images_files = os.listdir('data/dataset_img')
print(len(ocr_images_files))  # 21

random.shuffle(ocr_images_files)

n_train = int(len(ocr_images_files) * 0.7)
n_validation = int(len(ocr_images_files) * 0.15)
n_test = int(len(ocr_images_files) * 0.15)

print(n_train, n_validation, n_test)  # 14 3 3

train_files = ocr_images_files[:n_train]
validation_files = ocr_images_files[n_train: n_train+n_validation]
test_files = ocr_images_files[-n_test:]

train_img_ids = {}
validation_img_ids = {}
test_img_ids = {}

for image in file:
    if image['filename'] in train_files:
        train_img_ids[image['filename']] = image['image_id']
    elif image['filename'] in validation_files:
        validation_img_ids[image['filename']] = image['image_id']
    elif image['filename'] in test_files:
        test_img_ids[image['filename']] = image['image_id']

train_annotations = {f: [] for f in train_img_ids.keys()}
validation_annotations = {f: [] for f in validation_img_ids.keys()}
test_annotations = {f: [] for f in test_img_ids.keys()}

print(train_annotations, validation_annotations, test_annotations)

train_ids_img = {train_img_ids[id_]: id_ for id_ in train_img_ids}
validation_ids_img = {validation_img_ids[id_]: id_ for id_ in validation_img_ids}
test_ids_img = {test_img_ids[id_]: id_ for id_ in test_img_ids}


for annotation in file:
    if annotation['image_id'] in train_ids_img:
        train_annotations[train_ids_img[annotation['image_id']]].append(annotation)
    elif annotation['image_id'] in validation_ids_img:
        validation_annotations[validation_ids_img[annotation['image_id']]].append(annotation)
    elif annotation['image_id'] in test_ids_img:
        test_annotations[test_ids_img[annotation['image_id']]].append(annotation)

print(train_annotations, validation_annotations, test_annotations)
print(train_ids_img, validation_ids_img, test_ids_img)

with open('train_annotation.json', 'w') as file:
    json.dump(train_annotations, file, indent=4)
with open('validation_annotation.json', 'w') as file:
    json.dump(validation_annotations, file, indent=4)
with open('test_annotation.json', 'w') as file:
    json.dump(test_annotations, file, indent=4)
