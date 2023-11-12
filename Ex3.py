from pkg import read_json, print_json, process_data, write_json

MENU_FILE = 'menu.json'
OUTPUT_FILE = 'output.json'

new_item = {
    "name": "海鮮燉飯",
    "price": 239,
    "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
}

menu_data = read_json(MENU_FILE)
menu_data["categories"][1]["items"].append(new_item)

print(menu_data["categories"][1]["items"])
print_json(menu_data)

discount = float(input("請輸入折扣率(0.0 ~ 1.0): "))
process_data(menu_data, discount)
write_json(menu_data, OUTPUT_FILE)