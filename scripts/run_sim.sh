#!/usr/bin/env bash
# Запуск симуляції: Gazebo (світ maze) + ArduPilot SITL + micro-ROS agent + RViz
# Використання: bash run_sim.sh
bash "$(dirname "$0")/stop_sim.sh"
source /opt/ros/humble/setup.bash
source ~/ardu_ws/install/setup.bash
# Потрібно для sdformat_urdf: пошук моделей ardupilot_gazebo
export GZ_VERSION=harmonic
export SDF_PATH=$HOME/ardu_ws/install/ardupilot_gazebo/share:$HOME/ardu_ws/install/ardupilot_gz_description/share:$SDF_PATH
echo "Starting simulation. Wait ~1-2 min until 'EKF3 ... is using GPS' appears."
ros2 launch ardupilot_gz_bringup iris_maze.launch.py 2>&1 | tee ~/fpv_labs/logs/launch.log
