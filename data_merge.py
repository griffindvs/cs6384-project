import os

# Source directory
data_dir = 'data_source'

# Create destination directories
dest_dir = 'merged'
final_dir = 'data'
if not os.path.isdir(dest_dir):
    os.mkdir(dest_dir)
if not os.path.isdir(final_dir):
    os.mkdir(final_dir)

for dataset in os.listdir(data_dir):
    if os.path.isdir(data_dir + '/' + dataset):
        # Handle each dataset
        if dataset == 'ap':
            for data_item in os.listdir(data_dir + '/' + dataset):
                if '___' not in data_item:
                    print(f"Skipping {data_dir + '/' + data_item}")
                    continue

                plant_name = data_item.split('___')[0]
                plant_status = data_item.split('___')[1]

                if not os.path.isdir(f'{dest_dir}/1-{plant_name.lower()}'):
                    os.mkdir(f'{dest_dir}/1-{plant_name.lower()}')

                if os.path.isdir(data_dir + '/' + dataset + '/' + data_item):
                    healthy_i = 0
                    diseased_i = 0
                    for image in os.listdir(data_dir + '/' + dataset + '/' + data_item):
                        path = data_dir + '/' + dataset + '/' + data_item + '/'
                        if os.path.isfile(path + image):
                            if plant_status == 'healthy':
                                os.rename(path+image, f"{dest_dir}/1-{plant_name.lower()}/healthy-{healthy_i}.jpg")
                                healthy_i += 1
                            else:
                                os.rename(path+image, f"{dest_dir}/1-{plant_name.lower()}/diseased-{diseased_i}.jpg")
                                diseased_i += 1
        elif dataset == 'jf':
            for data_item in os.listdir(data_dir + '/' + dataset):
                if '_' not in data_item:
                    print(f"Skipping {data_dir + '/' + data_item}")
                    continue

                data_item_split = data_item.split('_')
                plant_name = data_item_split[0]
                plant_status = data_item_split[-1]

                if not os.path.isdir(f'{dest_dir}/2-{plant_name.lower()}'):
                    os.mkdir(f'{dest_dir}/2-{plant_name.lower()}')

                if os.path.isdir(data_dir + '/' + dataset + '/' + data_item):
                    healthy_i = 0
                    diseased_i = 0
                    for image in os.listdir(data_dir + '/' + dataset + '/' + data_item):
                        path = data_dir + '/' + dataset + '/' + data_item + '/'
                        if os.path.isfile(path + image):
                            if plant_status == 'healthy':
                                os.rename(path+image, f"{dest_dir}/2-{plant_name.lower()}/healthy-{healthy_i}.jpg")
                                healthy_i += 1
                            else:
                                os.rename(path+image, f"{dest_dir}/2-{plant_name.lower()}/diseased-{diseased_i}.jpg")
                                diseased_i += 1
        elif dataset == 'pd':
            for data_item in os.listdir(data_dir + '/' + dataset):
                if ' ' not in data_item:
                    print(f"Skipping {data_dir + '/' + data_item}")
                    continue

                data_item_split = data_item.split(' ')
                plant_name = data_item_split[0]
                plant_status = "healthy" if len(data_item_split) == 2 else "diseased"

                if not os.path.isdir(f'{dest_dir}/3-{plant_name.lower()}'):
                    os.mkdir(f'{dest_dir}/3-{plant_name.lower()}')

                if os.path.isdir(data_dir + '/' + dataset + '/' + data_item):
                    healthy_i = 0
                    diseased_i = 0
                    for image in os.listdir(data_dir + '/' + dataset + '/' + data_item):
                        path = data_dir + '/' + dataset + '/' + data_item + '/'
                        if os.path.isfile(path + image):
                            if plant_status == 'healthy':
                                os.rename(path+image, f"{dest_dir}/3-{plant_name.lower()}/healthy-{healthy_i}.jpg")
                                healthy_i += 1
                            else:
                                os.rename(path+image, f"{dest_dir}/3-{plant_name.lower()}/diseased-{diseased_i}.jpg")
                                diseased_i += 1
        elif dataset == 'pd-2':
            for data_item in os.listdir(data_dir + '/' + dataset):
                if ' ' not in data_item:
                    print(f"Skipping {data_dir + '/' + data_item}")
                    continue

                data_item_split = data_item.split(' ')
                plant_name = data_item_split[0]
                plant_status = "healthy" if len(data_item_split) == 2 else "diseased"

                if not os.path.isdir(f'{dest_dir}/4-{plant_name.lower()}'):
                    os.mkdir(f'{dest_dir}/4-{plant_name.lower()}')

                if os.path.isdir(data_dir + '/' + dataset + '/' + data_item):
                    healthy_i = 0
                    diseased_i = 0
                    for image in os.listdir(data_dir + '/' + dataset + '/' + data_item):
                        path = data_dir + '/' + dataset + '/' + data_item + '/'
                        if os.path.isfile(path + image):
                            if plant_status == 'healthy':
                                os.rename(path+image, f"{dest_dir}/4-{plant_name.lower()}/healthy-{healthy_i}.jpg")
                                healthy_i += 1
                            else:
                                os.rename(path+image, f"{dest_dir}/4-{plant_name.lower()}/diseased-{diseased_i}.jpg")
                                diseased_i += 1
        elif dataset == 'pv':
            for data_item in os.listdir(data_dir + '/' + dataset):
                if '___' not in data_item:
                    print(f"Skipping {data_dir + '/' + data_item}")
                    continue

                data_item_split = data_item.split('___')
                plant_name = data_item_split[0]
                plant_status = data_item_split[1]

                if not os.path.isdir(f'{dest_dir}/5-{plant_name.lower()}'):
                    os.mkdir(f'{dest_dir}/5-{plant_name.lower()}')

                if os.path.isdir(data_dir + '/' + dataset + '/' + data_item):
                    healthy_i = 0
                    diseased_i = 0
                    for image in os.listdir(data_dir + '/' + dataset + '/' + data_item):
                        path = data_dir + '/' + dataset + '/' + data_item + '/'
                        if os.path.isfile(path + image):
                            if plant_status == 'healthy':
                                os.rename(path+image, f"{dest_dir}/5-{plant_name.lower()}/healthy-{healthy_i}.jpg")
                                healthy_i += 1
                            else:
                                os.rename(path+image, f"{dest_dir}/5-{plant_name.lower()}/diseased-{diseased_i}.jpg")
                                diseased_i += 1

indeces = {}
for data_item in os.listdir(dest_dir):
    if '-' not in data_item:
        print(f"Skipping {dest_dir}/{data_item}")
        continue

    plant_name = data_item.split('-')[1]

    if plant_name not in indeces:
        indeces[plant_name] = 0

    if not os.path.isdir(final_dir + "/" + plant_name):
        os.mkdir(final_dir + "/" + plant_name)
    
    if os.path.isdir(dest_dir + "/" + data_item):
        for image in os.listdir(dest_dir + "/" + data_item):
            type = image.split('-')[0]

            os.rename(dest_dir + "/" + data_item + '/' + image, f"{final_dir}/{plant_name}/{type}-{indeces[plant_name]}.jpg")
            indeces[plant_name] = indeces[plant_name] + 1
