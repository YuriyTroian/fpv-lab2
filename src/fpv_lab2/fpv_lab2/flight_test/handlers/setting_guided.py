from functools import partial

from ..flight_state import FlightState
from .handler import FlightStateHandler


class SettingGuidedHandler(FlightStateHandler):
    def handle(self, node) -> None:
        if not node.request_in_progress:
            node.call_mode_switch(
                node.GUIDED_MODE,
                partial(self.guided_mode_callback, node),
            )

    def guided_mode_callback(self, node, future) -> None:
        node.request_in_progress = False
        try:
            response = future.result()
        except Exception as error:
            node.fail(f"GUIDED mode request failed: {error}")
            return
        if not response.status or response.curr_mode != node.GUIDED_MODE:
            node.fail(
                f"Could not enable GUIDED mode, current mode: "
                f"{response.curr_mode}"
            )
            return
        node.get_logger().info("GUIDED mode enabled")
        node.state = FlightState.ARMING
