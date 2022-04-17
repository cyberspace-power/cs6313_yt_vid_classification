import pickle
import json
import requests
from tqdm import tqdm
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("truncated_ids", "rb") as file:
    truncated_ids = pickle.load(file)

long_ids = []
for i in tqdm(range(len(truncated_ids)), miniters=50, mininterval=5):
    url = "https://data.yt8m.org/2/j/i/" + truncated_ids[i][:2] + "/" + truncated_ids[i] + ".js"
    try:
        req = requests.get(url, verify=False)
        if req.status_code == 200:
            text = req.text
            video_id = text.split('"')[3]
            long_ids.append(video_id)
    except:
        print(url + " didn't work.")

print(str(len(long_ids)) + " long ids collected")

with open('actual_ids', 'wb') as fh:
    pickle.dump(long_ids, fh)
