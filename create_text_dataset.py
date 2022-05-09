'''This file either creates a new sample of data points from the inputted class, or adds onto an existing one if
that file has fewer than the number of wanted samples'''

import pandas as pd
import os
import random

# How large of a sample of the data to take
samples = 4723  # This is how many we have from category 1 (fewest of any category)

# Note: Assumes that original data files are located in the following directories:
#   ../Data/category_wise_data
#   ../Data/category_wise_thumbnails
category_num = input("Please input the category number to create dataset of: ")
try:
    full_text_df = pd.read_csv('../Data/category_wise_data/category_' + str(category_num) + '.csv', index_col=False)
except FileNotFoundError:
    full_text_df = -1
    print("Please try again and enter a category number that exists")
    exit(1)

new_text_df = full_text_df[0:0].copy()  # Get new text data if it already exists. Otherwise, create empty new df
if os.path.exists('./dataset/category_wise_data/category_' + str(category_num) + '.csv'):
    new_text_df = pd.read_csv('./dataset/category_wise_data/category_' + str(category_num) + '.csv')
else:
    new_text_df = pd.DataFrame(columns=['Video Id', 'Title', 'Description'])


# Select new rows for new_text_df
# Note: To save time with manually deleting rows towards the end of the process, there is a "manual selection mode" here
# that will allow us to say Yes ('y') or No ('n') if we want to accept a data point. See the manual_select def below.
image_files = os.listdir('../Data/category_wise_thumbnails_original/' + str(category_num))
random.shuffle(image_files)
flag = True if samples - new_text_df.shape[0] <= 10 else False  # Decides whether to manually select data or not

for file in image_files:  # Iterate through shuffled file names
    if new_text_df.shape[0] == samples:  # Number of wanted samples achieved
        break

    # If this video ID is not already in the existing data and still exists in full dataset
    if file[:-4] in set(full_text_df['Video Id']) and file[:-4] not in set(new_text_df["Video Id"]):
        i = full_text_df.index[full_text_df['Video Id'] == file[:-4]].tolist()[0]  # Get index of row with corresponding video id
        if flag:
            choice = input("Do you want to add the following data point:\n\tVideo Id:\t" + file[:-4] +
                           "\n\tTitle:\t" + str(full_text_df.at[i, 'Title']) + "\n\tDesc:\t" +
                           str(full_text_df.at[i, 'Description']) + "\n\nType 'y' for YES or 'n' for NO: ")
            if choice == 'y':
                new_text_df.loc[len(new_text_df)] = [file[:-4], full_text_df.at[i, 'Title'], full_text_df.at[i, 'Description']]
        else:
            new_text_df.loc[len(new_text_df)] = [file[:-4], full_text_df.at[i, 'Title'], full_text_df.at[i, 'Description']]

print(new_text_df)
path_str = './dataset/category_wise_data/category_' + str(category_num) + '.csv'
new_text_df.to_csv(path_str, index=False)
