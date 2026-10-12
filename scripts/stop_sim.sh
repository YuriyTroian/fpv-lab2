#!/usr/bin/env bash
# Зупиняє всі процеси симуляції (Gazebo, SITL, DDS-агент, MAVProxy)
pkill -f "gz sim" || true
pkill -f gz || true
pkill -f arducopter || true
pkill -f micro_ros_agent || true
pkill -f mavproxy || true
sleep 2
echo "Simulation processes stopped."
