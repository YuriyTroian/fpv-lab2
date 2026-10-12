from functools import partial

from ..flight_state import FlightState
from .handler import FlightStateHandler


class LandingHandler(FlightStateHandler):
    def handle(self, node) -> None:
        if not node.request_in_progress:
            node.call_mode_switch(
                node.LAND_MODE,
                partial(self.land_mode_callback, node),
            )

    def land_mode_callback(self, node, future) -> None:
        node.request_in_progress = False
        try:
            response = future.result()
        except Exception as error:
            node.fail(f"LAND mode request failed: {error}")
            return
        if not response.status or response.curr_mode != node.LAND_MODE:
            node.fail(
                f"Could not enable LAND mode, current mode: "
                f"{response.curr_mode}"
            )
            return
        node.get_logger().info("LAND mode enabled")
        node.state = FlightState.WAITING_FOR_LANDING
