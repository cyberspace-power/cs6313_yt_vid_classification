import os
import shutil
import pandas as pd
import tqdm

category_num = input("Please input the category number to collect the images for: ")
dataset = pd.read_csv("/dataset/category_wise_data/category_" + str(category_num) + ".csv")

orig_path = "../Data/category_wise_thumbnails_original/"
new_path = "/dataset/category_wise_thumbnails/category_"
for item in dataset["Video Id"].unique():
    shutil.copy(orig_path + str(category_num) + "/" + item + ".jpg", new_path + str(category_num) + "/" + item + ".jpg")
