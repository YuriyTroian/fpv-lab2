# Лабораторна робота №2: політ до заданої точки (Gazebo + ArduPilot SITL + ROS 2)

Пакет `fpv_lab2`: політ дрона до цілі зі зміщенням (dx=5.8, dy=0.5) від старту і автоматична посадка.

##Структура
- `scripts/` — скрипти швидкого запуску: `run_sim.sh` (симуляція), `run_flight.sh` (політ), `stop_sim.sh` (зупинка).
- `logs/` — логи запусків.
- `src/fpv_lab2/` — ROS 2 Python-пакет з кодом польоту:
  - `flight_test_node.py` — вузол ROS 2 (підписки, сервіси, команди швидкості);
  - `handlers/` — по одному класу на кожен етап польоту (перевірка, режим, arm, зліт, зависання, посадка);
  - `handlers/navigating.py` — власний алгоритм польоту до цілі.

## Запуск
1. `bash scripts/run_sim.sh` - запуск симуляції
2. `bash scripts/run_flight.sh` - політ варіант 50, лог зберігається в ~/fpv_labs/logs
3. `bash scripts/stop_sim.sh` - зупинка всього

Збірка пакета: `colcon build --symlink-install --packages-select fpv_lab2`

