import json

def triangle_zhonxin(A, B, C) -> tuple:
    """
    計算一個三角形的重心
    Args:
        A(tuple): A點的座標
        B(tuple): B點的座標
        C(tuple): C點的座標
    Return: 重心座標
    """
    X = round((A[0] + B[0] + C[0]) / 3)
    Y = round((A[1] + B[1] + C[1]) / 3)
    return (X, Y)

def read_json(file_name: str) -> dict:
    """
    讀取json檔案回傳一個字典
    Args:
        file_name (str): Json檔案的名字
    Returns:
        dict: 包含json的檔案(字典的格式)
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

def print_json(data: dict) -> None:
    """
    讀取dictionary檔案，並輸出至屏幕上
    Args:
        data (dict): 形態為dict
    Returns:
        None
    """
    print(
        json.dumps(
            data, 
            sort_keys=True, 
            ensure_ascii=False, 
            indent=4, 
            separators=(',', ':')
        )
    )

def process_data(data: dict, discount: float) -> None:
    """
    將讀取的字典中每個菜品的價格做discount折數
    Args:
        data (dictionary): 形態為dict, discount(打折數): 形態為float
    """ 
    for category in data["categories"]:
        for item in category["items"]:
            item_price = round(item["price"] * discount)
            item["price"] = item_price

def write_json(data: dict, file_name: str) -> None:
    """
    將讀入的字典轉爲檔案
    Args:
        data (dictionary): 形態為dict
        file_name (str): 輸出JSON檔名，形態為str
    """
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ':'))
