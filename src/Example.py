"""
Author: James Kinley

Example of using the TuringMachine module!
"""

from TuringMachine import TM, TMState, TMStateType, TMDirection

# Define states
states = [
    TMState("start", TMStateType.START)
        .add_transition('a', 'one_a', 'a', TMDirection.RIGHT),
    TMState("one_a")
        .add_transition('b', 'one_b', 'b', TMDirection.RIGHT),
    TMState("one_b")
        .add_transition('a', 'one_b', 'a', TMDirection.RIGHT)
        .add_transition('_', 'accept', '_', TMDirection.RIGHT),
    TMState("accept", TMStateType.ACCEPTING)
]

tm = TM(
    states=states,
    tape=['a', 'b', 'a'],
    implicit_reject=True
)

accepted = tm.run(verbose=True)
print("Final: ", tm.current_state, "Accepted:", accepted)