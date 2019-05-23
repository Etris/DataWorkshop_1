# Day 05: Cracow trams delay prediction

* Download: use src/data/download.py

Usage:
```
python src/data/download.py
```

* Processing: use src/data/preprocess.py

Usage:
```
python src/data/preprocess.py --multi=False/True INPUT_FILE/INPUT_LIST OUTPUT_FILE
```

* --multi: if you want to use it to merge few files and preprocess each, set to True
* INPUT_FILE: e.g. "data/raw/report_07-23.csv"
* INPUT_FILES (if multi=True): e.g. "data/raw/report_07-23.csv, data/raw/report_07-24.csv"
* OUTPUT_FILE: e.g. "data/preprocessed/data.csv"
