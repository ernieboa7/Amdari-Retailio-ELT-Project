import os, csv, random, string
from datetime import date, timedelta





NEW_PRODUCTS = 100
NEW_SALES = 100

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")

PRODUCTS_PATH = os.path.join(DATA_DIR, "products.csv")
SALES_PATH    = os.path.join(DATA_DIR, "sales.csv")


def r(n):
    return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

def ensure_file_has_header(path, header):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(header)

def count_rows(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return 0
    with open(path, "r", newline="", encoding="utf-8") as f:
        return sum(1 for _ in f) - 1  # minus header

def append_rows(path, header, rows):
    ensure_file_has_header(path, header)
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writerows(rows)

def gen_products(n):
    header = [
        "Product ID","Product Name","Product Category","Product Description","Price","Stock Quantity",
        "Warranty Period","Product Dimensions","Manufacturing Date","Expiration Date","SKU","Product Tags",
        "Color/Size Variations","Product Ratings"
    ]
    names = ["Laptop","Smartphone","Headphones","Monitor","Tablet","Camera","Keyboard","Mouse"]
    cats  = ["Electronics","Office","Home Appliances"]
    colors = ["Green/Large","Red/Small","Blue/Medium","Black/Large"]

    today = date.today()
    rows = []
    for _ in range(n):
        mfg = today - timedelta(days=random.randint(30, 900))
        exp = today + timedelta(days=random.randint(365, 1500))
        rows.append({
            "Product ID": r(8),
            "Product Name": random.choice(names),
            "Product Category": random.choice(cats),
            "Product Description": f"Product_{r(5)}",
            "Price": round(random.uniform(20, 800), 2),
            "Stock Quantity": random.randint(0, 300),
            "Warranty Period": random.choice([0,1,2,3]),
            "Product Dimensions": f"{random.randint(5,20)}x{random.randint(5,20)}x{random.randint(5,20)} cm",
            "Manufacturing Date": mfg.isoformat(),
            "Expiration Date": exp.isoformat(),
            "SKU": f"SKU-{r(6)}",
            "Product Tags": f"{r(3)},{r(3)}",
            "Color/Size Variations": random.choice(colors),
            "Product Ratings": random.randint(1,5),
        })
    return header, rows

def gen_sales(product_ids, n):
    header = [
        "Row ID","Order ID","Order Date","Ship Date","Ship Mode","Customer ID","Customer Name","Segment",
        "Country","City","State","Postal Code","Region","Product ID","Category","Sub-Category","Product Name",
        "Sales","Quantity","Discount","Profit"
    ]
    ship_modes = ["First Class","Second Class","Standard Class","Same Day"]
    segments = ["Consumer","Corporate","Home Office"]
    locs = [("Dublin","Dublin","D01","West"), ("Cork","Cork","T12","South"), ("Galway","Galway","H91","West")]
    cats = [("Furniture","Chairs"),("Technology","Phones"),("Office Supplies","Paper")]

    today = date.today()
    start_row_id = count_rows(SALES_PATH) + 1

    rows = []
    for row_id in range(start_row_id, start_row_id + n):
        od = today - timedelta(days=random.randint(0, 6))
        sd = od + timedelta(days=random.randint(1, 5))
        qty = random.randint(1, 8)
        disc = random.choice([0,0,0,0.1,0.2,0.3])
        unit = round(random.uniform(10, 1200), 2)
        sales = round(unit * qty * (1 - disc), 2)
        profit = round(sales * random.uniform(-0.2, 0.35), 4)

        city, st, pc, region = random.choice(locs)
        cat, sub = random.choice(cats)

        rows.append({
            "Row ID": row_id,
            "Order ID": f"ORD-{today.strftime('%Y%m%d')}-{r(6)}",
            "Order Date": f"{od.month}/{od.day}/{od.year}",
            "Ship Date": f"{sd.month}/{sd.day}/{sd.year}",
            "Ship Mode": random.choice(ship_modes),
            "Customer ID": f"{r(2)}-{random.randint(10000,99999)}",
            "Customer Name": f"Customer_{r(5)}",
            "Segment": random.choice(segments),
            "Country": "Ireland",
            "City": city,
            "State": st,
            "Postal Code": pc,
            "Region": region,
            "Product ID": random.choice(product_ids),
            "Category": cat,
            "Sub-Category": sub,
            "Product Name": f"{sub} Item {r(4)}",
            "Sales": sales,
            "Quantity": qty,
            "Discount": disc,
            "Profit": profit,
        })
    return header, rows


if __name__ == "__main__":
    os.makedirs(DATA_DIR, exist_ok=True)

    # 1) products
    p_header, p_rows = gen_products(NEW_PRODUCTS)
    append_rows(PRODUCTS_PATH, p_header, p_rows)
    product_ids = [x["Product ID"] for x in p_rows]

    # 2) sales
    s_header, s_rows = gen_sales(product_ids, NEW_SALES)
    append_rows(SALES_PATH, s_header, s_rows)

    print(f" Added {NEW_PRODUCTS} products to {PRODUCTS_PATH}")
    print(f" Added {NEW_SALES} sales rows to {SALES_PATH}")
