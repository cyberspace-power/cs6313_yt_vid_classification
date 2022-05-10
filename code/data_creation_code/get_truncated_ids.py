import tensorflow as tf
import numpy as np
import pandas as pd
import pandas_tfrecords as pdtfr
import os
import pickle
from tqdm import tqdm

# filenames = ["train_data/train0059.tfrecord"]
filenames = os.listdir("train_data")
for _ in range(len(filenames)): filenames[_] = "train_data/" + filenames[_]
print(filenames)

truncated_ids = []
for i in tqdm(range(len(filenames)), desc="Loading..."):
    print("\n" + filenames[i], end=" ")
    df = pdtfr.tfrecords_to_pandas(filenames[i], schema={'id': str})
    truncated_ids += df['id'].to_list()
    print(len(truncated_ids))

with open('truncated_ids', 'wb') as fh:
    pickle.dump(truncated_ids, fh)


# raw_dataset = tf.data.TFRecordDataset(filenames)

'''for raw_record in raw_dataset.take(1):
    example = tf.train.Example()
    example.ParseFromString(raw_record.numpy())
    hi = tf.io.parse_example(example.SerializeToString(),
                             features={'id': tf.io.RaggedFeature(dtype=tf.string)})
    print(hi)
    print(example)'''


'''count = 0
for raw_record in raw_dataset:
    count += 1
print(count)'''
