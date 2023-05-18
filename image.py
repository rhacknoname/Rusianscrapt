import requests
from PIL import Image
from io import BytesIO

# URL gambar yang akan diunduh
image_url = "https://www1.fips.ru/Archive2//PAT/1924-1993/msur192439/DOC/DOCUSUA1/DOC000V1/D00000D1/00000001/00000001.tif"

# Mengunduh gambar dari URL
response = requests.get(image_url)
image_data = response.content

# Membuka gambar menggunakan PIL
image = Image.open(BytesIO(image_data))

# Menampilkan gambar
image.show()