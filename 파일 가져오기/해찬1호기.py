import requests
import xml.etree.ElementTree as ET
import csv

def download_xml(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Error downloading data: {response.status_code}")

def parse_xml(xml_data):
    root = ET.fromstring(xml_data)
    data_list = []
    for item in root.findall('.//row'):  # XML 구조에 맞게 경로를 조정해야 할 수 있습니다.
        data = {}
        for child in item:
            data[child.tag] = child.text
        data_list.append(data)
    return data_list

def save_to_csv(data, filename):
    if data:
        keys = data[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

# 실행 부분
url = "http://openapi.foodsafetykorea.go.kr/api/9b498f223f74427ca84f/C003/XML/1/100"
xml_data = download_xml(url)
parsed_data = parse_xml(xml_data)
save_to_csv(parsed_data, 'output2.csv')

print("CSV 파일 생성 완료")