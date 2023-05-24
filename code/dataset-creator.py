import argparse
import os
import zipfile
import yaml
import hashlib
import shutil


def copy_files(input_path, output_path, mode, labels):
    labels_path = os.path.join(input_path, 'markup', 'obj_train_data')
    images_path = os.path.join(input_path, 'images')
    new_labels_path = os.path.join(output_path, mode, 'labels')
    new_images_path = os.path.join(output_path, mode, 'images')
    
    for label in labels:
        old_label_name = os.path.join(labels_path, label + '.txt')
        new_label_name = os.path.join(new_labels_path, label + '.txt')
        old_image_name = os.path.join(images_path, label + '.jpg')
        new_image_name = os.path.join(new_images_path, label + '.jpg')

        shutil.copy(old_label_name, new_label_name)  
        shutil.copy(old_image_name, new_image_name)


def create_dataset(input_path, output_path, train_size = 70, test_size = 20):
    val_size = 100 - train_size - test_size
    os.makedirs(output_path, exist_ok=True)
    os.makedirs(f"{output_path}/test", exist_ok=True)
    os.makedirs(f"{output_path}/test/images", exist_ok=True)
    os.makedirs(f"{output_path}/test/labels", exist_ok=True)
    os.makedirs(f"{output_path}/train", exist_ok=True)
    os.makedirs(f"{output_path}/train/images", exist_ok=True)
    os.makedirs(f"{output_path}/train/labels", exist_ok=True)
    os.makedirs(f"{output_path}/val", exist_ok=True)
    os.makedirs(f"{output_path}/val/images", exist_ok=True)
    os.makedirs(f"{output_path}/val/labels", exist_ok=True)    
    os.makedirs(f"{input_path}/tmp", exist_ok=True)

    data_config = {
                'names': [
                'plast_bot',
                'plast_bag',
                'carton'
        ],
        'nc': 3,
        'test': f'{output_path}/test',
        'val': f'{output_path}/val',
        'train': f'{output_path}/train',
    }   

    with open(f"{output_path}/data.yaml", 'w') as outfile:
        yaml.dump(data_config, outfile, default_flow_style=False)

    label_names = [i[:-4] for i in os.listdir(f'{input_path}/markup/obj_train_data')]
    dataset_size = len(label_names)
    print(dataset_size)

    train_labels = label_names[: int(train_size / 100 * dataset_size)]
    print(len(train_labels))
    test_labels = label_names[int(train_size / 100 * dataset_size) : int((train_size + val_size) / 100 * dataset_size) ]
    print(len(test_labels))
    print(int(train_size / 100 * dataset_size), int((train_size + val_size) / 100 * dataset_size) )
    val_labels = label_names[int((test_size + train_size) / 100 * dataset_size):]
    print(len(val_labels))
    # print(val_labels, test_labels, train_labels)
    copy_files(input_path, output_path, mode = 'train', labels = train_labels)
    copy_files(input_path, output_path, mode = 'test', labels = test_labels)
    copy_files(input_path, output_path, mode = 'val', labels = val_labels)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        type=str,
    )
    parser.add_argument(
        "output",
        type=str,
    )
    parser.add_argument(
        "train_size",
        type=int,
    )
    parser.add_argument(
        "test_size",
        type=int,
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    input_path = args.input
    output_path = args.output
    create_dataset(
        input_path=args.input,
        output_path=args.output,
        train_size = args.train_size,
        test_size = args.test_size
    )