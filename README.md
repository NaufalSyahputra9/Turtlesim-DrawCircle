## Cara Memulai dan Menguji Node

### Prasyarat

Pastikan Anda telah menginstal ROS2 di sistem Anda. Ikuti panduan [instalasi resmi ROS2](https://docs.ros.org/en/rolling/Installation.html) sesuai dengan sistem operasi Anda.

## Create Package

Masuk ke folder _workspace_, lalu ke folder _~/workspace/src_

Buat package dengan perintah berikut.

```bash
ros2 pkg create --build-type ament_python --node-name pub_draw draw_circle
```

### Struktur Folder

Berikut adalah struktur folder dari proyek ini:

```
README.md
draw_circle/
	LICENSE
	package.xml
	setup.cfg
	setup.py
	draw_circle/
		__init__.py
		pub_draw.py
	resource/
		draw_circle
	test/
		test_copyright.py
		test_flake8.py
		test_pep257.py
```

### Langkah-Langkah Memulai dan Menguji

1. **Instal Dependensi**:
   Pastikan semua dependensi telah terinstal. Jika belum, instal menggunakan perintah berikut:

   ```bash
   colcon build
   ```

![Workflow](https://github.com/NaufalSyahputra9/Turtlesim-DrawCircle/blob/main/source/run_turtle.png?raw=true)

2. **Source Workspace**:
   Setelah proses build selesai, source file setup:

   ```bash
   source install/setup.bash
   ```

![Workflow](https://github.com/NaufalSyahputra9/Turtlesim-DrawCircle/blob/main/source/run_node.webm?raw=true)

3. **Jalankan Node**:
   Gunakan perintah berikut untuk menjalankan node `pub_draw`:

   ```bash
   ros2 run draw_circle pub_draw
   ```

![Workflow](https://github.com/NaufalSyahputra9/Turtlesim-DrawCircle/blob/main/source/set_param.webm?raw=true)

4. **Atur Parameter**:
   Dapat mengatur parameter `radius` untuk mengontrol ukuran lingkaran. Contohnya:

   ```bash
   ros2 param set /turtle_circle radius:=3.0
   ```

5. **Uji Node**:
   - Pastikan simulator `turtlesim` berjalan:

   ```bash
   ros2 run turtlesim turtlesim_node
   ```

   - Amati turtle bergerak dalam lintasan melingkar.
