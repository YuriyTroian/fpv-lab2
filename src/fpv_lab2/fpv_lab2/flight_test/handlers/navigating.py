import math
import time

from ..flight_state import FlightState
from .handler import FlightStateHandler


class NavigatingHandler(FlightStateHandler):
    """Політ до цілі: пропорційний регулятор швидкості з обмеженням."""

    SETTLE_TIME = 2.0

    def handle(self, node) -> None:
        if node.status is None or not node.status.armed:
            node.fail("Drone disarmed unexpectedly during navigation")
            return
        if node.odometry is None or node.target_xy is None:
            return

        p = node.odometry.pose.pose.position
        dx = node.target_xy[0] - p.x
        dy = node.target_xy[1] - p.y
        dist = math.hypot(dx, dy)

        # ціль досягнута: зупинка, витримка, звіт, посадка
        if node.reached_at is not None:
            node.send_velocity(0.0, 0.0)
            if time.monotonic() - node.reached_at >= self.SETTLE_TIME:
                log = node.get_logger()
                log.info(f"Start position: ({node.start_xy[0]:.2f}, {node.start_xy[1]:.2f})")
                log.info(f"Target position: ({node.target_xy[0]:.2f}, {node.target_xy[1]:.2f})")
                log.info(f"Actual position before landing: ({p.x:.2f}, {p.y:.2f})")
                log.info(f"Positioning error: {dist:.3f} m")
                node.state = FlightState.LANDING
            return

        if dist <= node.TOLERANCE:
            node.get_logger().info(f"Target reached, distance {dist:.3f} m")
            node.send_velocity(0.0, 0.0)
            node.reached_at = time.monotonic()
            return

        speed = min(node.MAX_SPEED, node.KP * dist)
        speed = max(speed, 0.1)
        node.send_velocity(speed * dx / dist, speed * dy / dist)
        node.get_logger().info(
            f"Distance to target: {dist:.2f} m", throttle_duration_sec=1.0)
