# Plase note that external libraries, such as NumPy or Pandas
# are NOT available for this task

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import numpy as np
import pandas as pd

def solution(S):
    # write your code in Python 3.6

    # name.extension, city, date (timezone differences)
    # group by city, date, then add natural numbers from 1
    # photos may not be unique
    # task:
    # rename city, number (same length to largest number, leading 0s).extension
    # years 2000-2020
    # up to 100 photos
    # photo names are in a string separated by new lines
    
    # S = 'photo.jpg, Warsaw, 2013-09-05 14:08:15 \n' \
    # + 'photos.jpg, London, 2013-11-05 14:08:15 \n' \
    # + 'photosfirst.jpg, London, 2003-11-05 14:08:15 \n' \
    # + 'photor.jpg, Warsaw, 2021-09-05 14:08:15 \n' \
    # + 'photow.jpg, Warsaw, 2020-09-05 14:08:15 \n' \
    # + 'photoss.jpg, Warsaw, 2019-09-05 14:08:15 \n' \
    # + 'photosa.jpg, Warsaw, 2018-09-05 14:08:15 \n' \
    # + 'photoas.jpg, Warsaw, 2017-09-05 14:08:15 \n' \
    # + 'photogg.jpg, Warsaw, 2016-09-05 14:08:15 \n' \
    # + 'photoghter.jpg, Warsaw, 2015-09-05 14:08:15 \n' \
    # + 'photohtt.jpg, Warsaw, 2014-09-05 14:08:15 \n' \
    # + 'photohtr.jpg, Warsaw, 2003-09-05 14:08:15 \n' \
    # + 'photoasas.jpg, Warsaw, 2013-11-05 14:08:15'

    # get photos
    photos = S.split('\n')
    # get original order
    orig_order = [i+1 for i in range(len(photos))]
    # get cities
    cities = [photo.split(',')[1].lstrip()  for photo in photos]
    # get the set of cities
    set_cities = list(set(cities))
    # get the name of photos
    names = [photo.split(',')[0].lstrip()  for photo in photos]
    # get the dates
    dates = [photo.split(',')[2].lstrip().rstrip()  for photo in photos]
    # get the extensions of photos
    extensions = [name.split('.')[1] for name in names]
    # get the count of cities in files
    city_counts = [cities.count(city) for city in cities]
    # get the length of numbers needed for leading 0s
    lead_numbers = [len(str(cnt)) for cnt in city_counts]
    
    # work with pandas:
    df = pd.DataFrame(list(zip(photos, orig_order, cities, names, dates, extensions,
                            city_counts, lead_numbers)),
                      columns=['photos', 'orig_order', 'cities', 'names', 'dates', 'extensions',
                            'city_counts', 'lead_numbers'])

    # by city, order by date, give number
    df_dicts = {}
    for city in set_cities:
        df_city = df.loc[df['cities'] == city]
        df_city = df_city.sort_values('dates')
        df_city.insert(0, 'Ordered_Photo_ID', range(1, 1 + len(df_city)))
        df_dicts[city] = df_city

    # append all dfs in a dict:
    df = pd.concat(df_dicts.values(), ignore_index=True)
    df = df.sort_values('orig_order')

    # Ordered_Photo_ID to string
    Ordered_Photo_ID = df['Ordered_Photo_ID'].astype(str).values
    Ordered_Photo_ID_len = [len(o) for o in Ordered_Photo_ID]
    lead_numbers_diff = df['lead_numbers'].values - Ordered_Photo_ID_len
    new_ordered_photo_id = [Ordered_Photo_ID[i].zfill(lead_numbers_diff[i]+1) for i in range(len(lead_numbers_diff))]
    df['Ordered_Photo_ID'] = new_ordered_photo_id

    # file names
    file_names = df['cities'].values + df['Ordered_Photo_ID'].values + '.' + df['extensions']
    return file_names
    pass

S = 'photo.jpg, Warsaw, 2013-09-05 14:08:15 \n' \
+ 'photos.jpg, London, 2013-11-05 14:08:15 \n' \
+ 'photosfirst.jpg, London, 2003-11-05 14:08:15 \n' \
+ 'photor.jpg, Warsaw, 2021-09-05 14:08:15 \n' \
+ 'photow.jpg, Warsaw, 2020-09-05 14:08:15 \n' \
+ 'photoss.jpg, Warsaw, 2019-09-05 14:08:15 \n' \
+ 'photosa.jpg, Warsaw, 2018-09-05 14:08:15 \n' \
+ 'photoas.jpg, Warsaw, 2017-09-05 14:08:15 \n' \
+ 'photogg.jpg, Warsaw, 2016-09-05 14:08:15 \n' \
+ 'photoghter.jpg, Warsaw, 2015-09-05 14:08:15 \n' \
+ 'photohtt.jpg, Warsaw, 2014-09-05 14:08:15 \n' \
+ 'photohtr.jpg, Warsaw, 2003-09-05 14:08:15 \n' \
+ 'photoasas.jpg, Warsaw, 2013-11-05 14:08:15'

solution(S)
