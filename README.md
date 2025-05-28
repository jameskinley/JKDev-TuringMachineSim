# JKDev Turing Machine Simulator

This Python module provides a simple and extensible Turing Machine emulator.

It is designed as an educational tool, and I plan to extend it to feature higher-level implementations (with functions such as seek etc.).

> For more comprehensive documentation, [click here!](./docs/TuringMachine.md)

## Install Dependencies
There aren't many, but just standard procedure:
``` bash
pip install -r requirements.txt
```

## Usage
> This example can be found in `src/Example.py`.

``` python
"""Example of using the TuringMachine module!"""

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
```

## Running Tests (Handy for modifying things)
```
pytest
```

(That's it!)