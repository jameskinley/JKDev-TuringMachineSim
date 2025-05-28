# JKDev Turing Machine Module Documentation

> Note: this documentation was automatically generated from pydoc strings using Claude Sonnet 4!

**Author:** James Kinley  
**Module:** JKDev Turing Machine

## Overview

This module provides a basic implementation of a deterministic Turing Machine. It includes classes for states, transitions, and the machine itself, and is designed to be extensible for various Turing Machine configurations.

## Classes

### TMError

```python
class TMError(Exception)
```

Base class for exceptions in this module. Inherits from the standard Python `Exception` class.

**Purpose:** Used to raise specific errors related to Turing Machine operations and configurations.

---

### TMDirection

```python
class TMDirection(Enum)
```

Enum for Turing Machine head movement direction.

**Values:**
- `LEFT = -1` - Move tape head left
- `RIGHT = 1` - Move tape head right

**Methods:**
- `__str__()` - Returns the name of the direction
- `__repr__()` - Returns formatted representation as `TMDirection.{name}`

---

### TMStateType

```python
class TMStateType(Enum)
```

Enum for Turing Machine state types.

**Values:**
- `START = 0` - Starting state of the machine
- `ACCEPTING = 1` - State that accepts input
- `REJECTING = 2` - State that rejects input
- `NORMAL = 3` - Regular computation state

**Methods:**
- `__str__()` - Returns the name of the state type
- `__repr__()` - Returns formatted representation as `TMStateType.{name}`

---

### TMState

```python
class TMState
```

Class representing a state in a Turing Machine.

#### Constructor

```python
__init__(name: str, state_type: TMStateType = TMStateType.NORMAL)
```

Initializes a Turing Machine state.

**Parameters:**
- `name` (str): Name of the state
- `state_type` (TMStateType, optional): Type of the state. Defaults to `TMStateType.NORMAL`

#### Methods

##### add_transition()

```python
add_transition(symbol, new_state, new_symbol, direction) -> TMState
```

Adds a transition to the state.

**Parameters:**
- `symbol`: Input symbol that triggers the transition
- `new_state`: Name of the state to transition to
- `new_symbol`: Symbol to write on the tape
- `direction`: Direction to move the tape head (LEFT or RIGHT)

**Returns:** `self` for method chaining

##### String Representations

- `__str__()` - Returns the state name
- `__repr__()` - Returns formatted representation showing name and type

#### Attributes

- `name` (str): The name of the state
- `state_type` (TMStateType): The type of the state
- `transitions` (list): List of transitions from this state

---

### TMTransition

```python
class TMTransition
```

Class representing a transition in a Turing Machine.

#### Constructor

```python
__init__(state: TMState, symbol: str, new_state: str, new_symbol: str, direction: TMDirection)
```

Initializes a Turing Machine transition.

**Parameters:**
- `state` (TMState): The state this transition belongs to
- `symbol` (str): Input symbol that triggers the transition
- `new_state` (str): Name of the state to transition to
- `new_symbol` (str): Symbol to write on the tape
- `direction` (TMDirection): Direction to move the tape head

#### Attributes

- `state` (TMState): Source state of the transition
- `symbol` (str): Triggering input symbol
- `new_state` (str): Target state name
- `new_symbol` (str): Symbol to write
- `direction` (TMDirection): Head movement direction

---

### TM

```python
class TM
```

Class representing a Turing Machine.

#### Constructor

```python
__init__(states: List[TMState], tape: List[str] = [], empty_symbol: Optional[str] = '_', implicit_reject: bool = False)
```

Initializes a Turing Machine.

**Parameters:**
- `states` (List[TMState]): List of TMState objects defining the machine's states
- `tape` (List[str], optional): Initial tape content as a list of symbols. Defaults to empty list
- `empty_symbol` (Optional[str], optional): Symbol representing an empty cell on the tape. Defaults to '_'
- `implicit_reject` (bool, optional): If True, the machine will implicitly reject if it reaches a state without transitions. Defaults to False

**Raises:**
- `TMError`: If there isn't exactly one start state
- `TMError`: If there are no accepting states
- `TMError`: If there are no rejecting states and `implicit_reject` is False

#### Methods

##### run()

```python
run(max_steps=1000, verbose=False, show_progress=False) -> bool
```

Runs the Turing Machine for a specified number of steps or until it reaches an accepting or rejecting state.

**Parameters:**
- `max_steps` (int, optional): Maximum number of steps to run the machine. Defaults to 1000
- `verbose` (bool, optional): If True, prints the current configuration of the machine at each step. Defaults to False
- `show_progress` (bool, optional): If True, shows a progress bar for the number of steps. Defaults to False

**Returns:**
- `bool`: True if the machine accepts the input, False if it rejects

##### step()

```python
step()
```

Performs a single step of the Turing Machine.

This method reads the current symbol under the tape head, finds the appropriate transition, updates the tape, moves the head, and changes the current state.

**Behavior:**
- If the head position exceeds the current tape length, the tape is extended with the empty symbol
- If the head moves left from the first position, a new empty symbol is added at the start of the tape

**Raises:**
- `TMError`: If no valid transition is found
- `TMError`: If the transition leads to a non-existent state

##### _config_repr()

```python
_config_repr() -> str
```

Private method that returns a string representation of the current machine configuration.

**Returns:** String showing tape contents, head position, and current state name

#### Attributes

- `empty_symbol` (str): Symbol representing empty tape cells
- `tape` (List[str]): Current tape contents
- `states` (List[TMState]): All states in the machine
- `implicit_reject` (bool): Whether to implicitly reject on missing transitions
- `head_pos` (int): Current position of the tape head
- `current_state` (TMState): Currently active state
- `accepting_states` (List[TMState]): List of accepting states
- `rejecting_states` (List[TMState]): List of rejecting states

## Usage Examples

### Basic Turing Machine Setup

```python
from turing_machine import TM, TMState, TMStateType, TMDirection

# Create states
start_state = TMState("q0", TMStateType.START)
accept_state = TMState("qaccept", TMStateType.ACCEPTING)
reject_state = TMState("qreject", TMStateType.REJECTING)

# Add transitions
start_state.add_transition('0', 'qaccept', '1', TMDirection.RIGHT)
start_state.add_transition('1', 'qreject', '0', TMDirection.LEFT)

# Create and run machine
states = [start_state, accept_state, reject_state]
machine = TM(states, tape=['0', '1', '0'])
result = machine.run(verbose=True)
```

### Method Chaining for Transitions

```python
state = TMState("q1").add_transition('a', 'q2', 'b', TMDirection.RIGHT)\
                     .add_transition('c', 'q3', 'd', TMDirection.LEFT)
```

## Dependencies

- `typing.List`
- `typing.Optional`
- `enum.Enum`
- `tqdm.tqdm` (for progress bars)

## Error Handling

The module uses the custom `TMError` exception for all Turing Machine-related errors, including:
- Invalid state configurations
- Missing transitions
- Non-deterministic behavior
- Invalid state references

## Notes

- This implementation is designed for deterministic Turing Machines only
- The tape can extend infinitely in both directions
- Progress tracking is available through the `tqdm` library integration
- The module enforces proper Turing Machine constraints through validation