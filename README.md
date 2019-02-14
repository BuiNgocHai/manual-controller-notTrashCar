# Manual Controller and Data for HAUI.notTrashCar
Manual controller and GenData dành cho xe của team HAUI.notTrashCar
## LƯU Ý: Khi push mn nhớ tạo branch riêng nhé
## Điều khiển
- Điều khiển bằng phím lên, xuống, trái, phải,lùi ( thao tác trong pygame windown)
- Controller_ver1 chưa hoàn toàn giống hẳn với Manual của ver2.
- Controller_ver2 is coming soon.

## GenData
- chỉnh sửa đường dẫn để lưu data trong file config trước khi run.
- File labels sẽ được lưu ngay trong file chưa data 

## Need
- Các work cotrol cũng như gendata đã hoạt động tốt tuy nhiên phần gendata file json còn chưa có KEY_STATUS và t quên chưa sửa cho index :v 
## Dependency
- Ubuntu 16.04 or newer
- [Melodic Morenia](http://wiki.ros.org/melodic) version of [ROS](https://ros.org)
```
$ sudo apt-get install ros-melodic-desktop-full
```
Plese follow full instruction at [Melodic Morenia wiki](http://wiki.ros.org/melodic)
- rosbridge-suite
```
$ sudo apt-get install ros-melodic-rosbridge-server
```
- Python 3.6+ (recommend Python 3.6.7)
- numpy, cmake, opencv-python (`pip3 install <package-name>`)
- Unity Simulator from FPT: [ver1](https://drive.google.com/open?id=1q6WtD98eu1qbcwdwIDhraUqSHO6cO0if), [ver2](https://drive.google.com/open?id=1uwi0A-cuLp9Pa1PB9lkmybmbGrxh5sRD), [ver3](https://www.fshare.vn/file/YWG8HGK84MHA?token=1548131191)

## Cách run
- Đầu tiên build lại package `team705`:
```
git clone https://github.com/lamhoangtung/manual-controller-notTrashCar
cd team705
catkin_make
```

- Package được chạy theo hướng dẫn trong file [`team705.launch`](/src/team705/launch/team705.launch), đầu tiên chạy `ros_bridge` khởi tạo kết nối đến simulator sau đó chạy đến [`main.py`](/src/team705/src/main.py) như một node của ROS

``` 
source ./devel/setup.bash
roslaunch team705 team705.launch
```

- Chạy simulator theo hướng dẫn [này](https://drive.google.com/open?id=14vCOzUO6_-6fyv0eypql1owZz3NIRiRY), lưu ý không dùng chế độ Manual của simulator (nếu có) và hãy thay tên team thành `team705`, port là `127.0.0.1:9005`





