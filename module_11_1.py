import matplotlib.pyplot as plt
import glob
from PIL import Image

"""
Matplotlib — это библиотека для визуализации данных в Python. Она используется для создания любых видов графиков: 
линейных, круговых диаграмм, построчных гистограмм и других — в зависимости от задач.
Вот пример линейного графика с водяным
"""
x = [2.9, 3.5, 4.1, 2.6, 4.4, 2.9]
y = [2, 13, 2, 9.1, 9.1, 2]
(fig, ax) = plt.subplots()
ax.grid()
ax.text(0.5, 0.5, 'сделано для Urban', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation=30)
plt.plot(x, y, marker='1')
plt.title('Линейный график "Да это звезда"')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

"""
Библиотека Pillow добавляет много различных возможностей для работы с изображениями: чтение различных 
форматов, обработка, редактирование, конвертирование, изменение размера и ориентации,  и т.д. 
Например пакетная обработка. Операцию можно применять к нескольким файлам изображений. Все изображения 
PNG в текущем каталоге конвертируются и сохраняться в формате JPEG с пониженным качеством.
"""


def compress_image(source_path: str, dest_path: str) -> None:
    with Image.open(source_path) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(dest_path, "JPEG", optimize=True, quality=80)


paths = glob.glob("*.png")
for path in paths:
    compress_image(path, path[:-4] + ".jpg")


