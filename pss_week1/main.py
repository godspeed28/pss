from fastapi import FastAPI

# Inisialisasi FastAPI
app = FastAPI()

# Data dummy sementara (pengganti database)
items = [
    {"id": 1, "name": "Buku Python", "price": 50000},
    {"id": 2, "name": "Kabel Type-C", "price": 25000}
]

# Endpoint untuk membaca data (GET)
@app.get("/")
def read_root():
    return {"message": "Halo, selamat datang di backend API Python!"}

# Endpoint untuk mengambil semua item (GET)
@app.get("/items")
def get_items():
    return {"data": items}

@app.get("/items/{id}/id")
def get_item(id: int):
    for item in items:
        if item["id"] == id:
            return {"data": item}
    
    return {"message": "Item tidak ditemukan"}

# Endpoint untuk menambah data baru (POST)
@app.post("/items")
def create_item(name: str, price: int):
    new_id = len(items) + 1
    new_item = {"id": new_id, "name": name, "price": price}
    items.append(new_item)
    return {"message": "Item berhasil ditambahkan", "data": new_item}
