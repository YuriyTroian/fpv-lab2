from ..flight_state import FlightState
from .handler import FlightStateHandler


class WaitingForLandingHandler(FlightStateHandler):
    def handle(self, node) -> None:
        if node.status is None:
            return
        if not node.status.flying:
            node.get_logger().info("Landing completed")
            if node.odometry is not None:
                altitude = node.odometry.pose.pose.position.z
                node.get_logger().info(f"Final Gazebo altitude: {altitude:.2f} m")
            node.state = FlightState.FINISHED
            node.get_logger().info("Flight test completed successfully")
