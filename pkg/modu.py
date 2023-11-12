import json

def triangle_zhonxin(a: tuple, b: tuple, c: tuple) -> tuple:
    """Calculate the triangle center"""
    x = (float(a[0]) + float(b[0]) + float(c[0])) / 3
    y = (float(a[1]) + float(b[1]) + float(c[1])) / 3
    return (round(x),round(y))

"""
JSON process
"""
def read_json(file_name: str) -> dict:
    """將 json 檔案轉為字典後回傳"""
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

def print_json(data: dict) -> None:
    """將字典轉爲 json 字串後輸出到螢幕"""
    print(json.dumps(data, indent=4, ensure_ascii=False))

def process_data(data: dict, discount: float) -> None:
    """將字典中每個菜品的價格打discount 折數"""
    for category in data['categories']:
        for item in category['items']:
            item['price'] = round(item['price'] * discount)

def write_json(data: dict, file_name: str) -> None:
    """將字典轉為檔案"""
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
