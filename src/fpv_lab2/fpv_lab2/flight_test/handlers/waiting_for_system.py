from ..flight_state import FlightState
from .handler import FlightStateHandler


class WaitingForSystemHandler(FlightStateHandler):
    def handle(self, node) -> None:
        if node.status is None or node.odometry is None:
            return
        if not node.services_ready():
            return
        node.get_logger().info("ArduPilot and all services are available")
        node.state = FlightState.PREARM_CHECK
