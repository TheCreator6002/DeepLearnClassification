import os
import shutil

# dataset directory
data_dir = 'images'
# training dataset directory
train_dir = 'train'
# val dataset directory
val_dir = 'val'
# test dataset directory
test_dir = 'test'
# test dataset portion
test_data_portion = 0.15
# val dataset portion
val_dataset_portion = 0.15
number_images = 12500


def create_directory(dir_name):
    # function create directory
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)
    os.makedirs(os.path.join(dir_name, "Cat"))
    os.makedirs(os.path.join(dir_name, "Dog"))


create_directory(train_dir)
create_directory(val_dir)
create_directory(test_dir)


def copy_images(start_index, end_index, sourse_dir, dest_dir):
    # function distribution dataset
    for i in range(start_index, end_index):
        shutil.copy2(os.path.join(sourse_dir, "cat." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "Cat"))
        shutil.copy2(os.path.join(sourse_dir, "dog." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "Dog"))


start_val_data_idx = int(number_images * (1 - val_dataset_portion - test_data_portion))
start_test_data_idx = int(number_images * (1 - test_data_portion))

copy_images(0, start_val_data_idx, data_dir, train_dir)
copy_images(start_val_data_idx, start_test_data_idx, data_dir, val_dir)
copy_images(start_test_data_idx, number_images, data_dir, test_dir)
