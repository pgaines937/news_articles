#!/usr/bin/env python3
#
# Post Processor for Google Finance Spider scraped data
# Name: Patrick Gaines
#
import pandas as pd

if __name__ == '__main__':
    try:
        dataset_files = ['dataset2.csv', 'dataset3.csv', 'dataset4.csv']
        df_list = []
        for filename in sorted(dataset_files):
            df_list.append(pd.read_csv(filename))
        full_df = pd.concat(df_list)
        full_df.to_csv('combined_dataset.csv')
    except Exception as detail:
        print("Error ==> ", detail)
