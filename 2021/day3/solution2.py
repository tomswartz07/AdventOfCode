#!/usr/bin/python

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
currentdataOxygen, currentdataCO2 = data, data
scrubber_rating,oxygen_rating = 0, 0

for i in range(len(data[0].strip())):
    data_with_one_co2,data_with_one_o2 = [],[]
    for line in currentdataOxygen:
        if line[i] == '1':
            data_with_one_o2.append(line)
    for line in currentdataCO2:
        if line[i] == '1':
            data_with_one_co2.append(line)

    if len(data_with_one_o2) >= len(currentdataOxygen)/2:
        currentdataOxygen = data_with_one_o2
    else:
        currentdataOxygen = [entry for entry in currentdataOxygen if entry not in data_with_one_o2]

    if len(data_with_one_co2) < len(currentdataCO2)/2:
        currentdataCO2 = data_with_one_co2
    else:
        currentdataCO2 = [entry for entry in currentdataCO2 if entry not in data_with_one_co2]

    if len(currentdataCO2) == 1:
        scrubber_rating = int(currentdataCO2[0].strip(),2)
    if len(currentdataOxygen) == 1:
        oxygen_rating = int(currentdataOxygen[0].strip(),2)
print("Final:",oxygen_rating * scrubber_rating)
