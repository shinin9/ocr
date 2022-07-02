import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    image_id = 0
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text),
                     image_id
                     )
            xml_list.append(value)
        image_id += 1
    # column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax', 'image_id']
    xml_df = pd.DataFrame(xml_list)
    return xml_df


def main():
    image_path = os.path.join(os.getcwd(), 'data/dataset_xml')
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('data/images.csv', index=None)
    print('Successfully converted xml to csv.')


main()

