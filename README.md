# unkothink for ros2

[![test unkothink](https://github.com/hide4096/unkothink_for_ros2/actions/workflows/test.yml/badge.svg)](https://github.com/hide4096/unkothink_for_ros2/actions/workflows/test.yml)

課題1で製作した[unkothink](https://github.com/hide4096/robosys2022#unkothink)コマンドをros2に移植しました。

## Requirement
- ROS2 Humble

次の環境で動作を確認しています
- Ubuntu 22.04
- ROS2 Humble

## Installation
- このリポジトリをクローンして、ビルドします
    ```
    cd ~/ros2_ws/src
    git clone https://github.com/hide4096/unkothink_for_ros2.git
    rosdep install -i --from-path src --rosdistro humble -y
    cd ~/ros2_ws && colcon build
    source ~/ros2_ws/install/setup.bash
    ```

## Usage

```
$ ros2 launch unkothink unko_hello.py
[INFO] [launch]: All log files can be found below /home/hide/.ros/log/2023-01-07-13-01-24-914985-f79c6fa430e7-11362
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [sayhello-1]: process started with pid [11363]
[INFO] [listen_unko-2]: process started with pid [11365]
[listen_unko-2] [INFO] [1673096486.203036336] [oshiri]:
[listen_unko-2]  --------
[listen_unko-2] | Hello! |
[listen_unko-2]  --------
[listen_unko-2]   @
[listen_unko-2]     @
[listen_unko-2]     人
[listen_unko-2]    (__)
[listen_unko-2]   (____)
[listen_unko-2]  (______)
[listen_unko-2]
```

- /unkothinkトピックにメッセージを直接送ってうんこを表示することもできます。

  ```
  $ ros2 topic pub --once /unkothink std_msgs/String "data: unchi"
  publisher: beginning loop
  publishing #1: std_msgs.msg.String(data='unchi')
  ```

  ```
  $ ros2 run unkothink listen_unko
  [INFO] [1673096677.601601504] [oshiri]:
   -------
  | unchi |
   -------
    @
      @
      人
     (__)
    (____)
   (______)
 
  ```

## Description
![rqt](https://user-images.githubusercontent.com/87698678/211152444-3c3d97b0-e95d-49c2-9eb4-7b6036b68dd8.png)
- /sayhello
  - "Hello!"というメッセージをString型で1秒おきに、/unkothinkへ送信します
- /oshiri
  - /unkothinkに来たメッセージを元に、うんこが考え事をしているアスキーアートをコンソールに出力します

## License
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2023 Aso Hidetoshi
