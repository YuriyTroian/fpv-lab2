#!/usr/bin/env bash
# Запуск програми польоту до цілі (варіант 50: dx=5.8, dy=0.5; висота 4 м над стінами)
# Додаткові параметри можна передати так:  bash run_flight.sh -p target_dx:=6.4
source /opt/ros/humble/setup.bash
source ~/ardu_ws/install/setup.bash
source ~/fpv_labs/install/setup.bash
LOG=~/fpv_labs/logs/flight_$(date +%Y%m%d_%H%M%S).log
ros2 run fpv_lab2 flight_test --ros-args \
  -p takeoff_altitude:=4.0 -p target_dx:=5.8 -p target_dy:=0.5 "$@" 2>&1 | tee "$LOG"
echo "Log saved to $LOG"
