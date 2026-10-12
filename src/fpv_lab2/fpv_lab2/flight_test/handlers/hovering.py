import time

from ..flight_state import FlightState
from .handler import FlightStateHandler


class HoveringHandler(FlightStateHandler):
    def handle(self, node) -> None:
        if node.status is None or not node.status.armed:
            node.fail("Drone disarmed unexpectedly during flight")
            return
        altitude = 0.0
        if node.odometry is not None:
            altitude = node.odometry.pose.pose.position.z
            node.get_logger().debug(f"Gazebo altitude: {altitude:.2f} m")
        elapsed = time.monotonic() - node.hover_started_at
        if elapsed >= node.HOVER_DURATION and (
            altitude >= node.TAKEOFF_ALTITUDE - 0.2
        ):
            if node.navigate:
                node.get_logger().info(
                    f"Hover completed at {altitude:.2f} m, flying to target")
                node.state = FlightState.NAVIGATING
            else:
                node.get_logger().info("Hover completed, starting landing")
                node.state = FlightState.LANDING
