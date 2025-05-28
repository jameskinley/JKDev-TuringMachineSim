Author: James Kinley

Example of using the TuringMachine module!

<a id="Example.TM"></a>

## TM

<a id="Example.TMState"></a>

## TMState

<a id="Example.TMStateType"></a>

## TMStateType

<a id="Example.TMDirection"></a>

## TMDirection

<a id="Example.states"></a>

#### states

<a id="Example.tm"></a>

#### tm

<a id="Example.accepted"></a>

#### accepted

Module: JKDev Turing Machine
Author: James Kinley

This module provides a basic implementation of a deterministic Turing Machine.
It includes classes for states, transitions, and the machine itself, and is designed to be extensible for various Turing Machine configurations.

<a id="TuringMachine.List"></a>

## List

<a id="TuringMachine.Optional"></a>

## Optional

<a id="TuringMachine.Enum"></a>

## Enum

<a id="TuringMachine.tqdm"></a>

## tqdm

<a id="TuringMachine.TMError"></a>

## TMError Objects

```python
class TMError(Exception)
```

Base class for exceptions in this module.

<a id="TuringMachine.TMDirection"></a>

## TMDirection Objects

```python
class TMDirection(Enum)
```

Enum for Turing Machine head movement direction.

<a id="TuringMachine.TMDirection.LEFT"></a>

#### LEFT

<a id="TuringMachine.TMDirection.RIGHT"></a>

#### RIGHT

<a id="TuringMachine.TMDirection.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

<a id="TuringMachine.TMDirection.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

<a id="TuringMachine.TMStateType"></a>

## TMStateType Objects

```python
class TMStateType(Enum)
```

Enum for Turing Machine state types.

<a id="TuringMachine.TMStateType.START"></a>

#### START

<a id="TuringMachine.TMStateType.ACCEPTING"></a>

#### ACCEPTING

<a id="TuringMachine.TMStateType.REJECTING"></a>

#### REJECTING

<a id="TuringMachine.TMStateType.NORMAL"></a>

#### NORMAL

<a id="TuringMachine.TMStateType.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

<a id="TuringMachine.TMStateType.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

<a id="TuringMachine.TMState"></a>

## TMState Objects

```python
class TMState()
```

Class representing a state in a Turing Machine.

<a id="TuringMachine.TMState.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: str, state_type: TMStateType = TMStateType.NORMAL)
```

Initializes a Turing Machine state.
:param name: Name of the state.
:param state_type: Type of the state (START, ACCEPTING, REJECTING, NORMAL).

<a id="TuringMachine.TMState.add_transition"></a>

#### add\_transition

```python
def add_transition(symbol, new_state, new_symbol, direction)
```

Adds a transition to the state.
:param symbol: Input symbol that triggers the transition.
:param new_state: Name of the state to transition to.
:param new_symbol: Symbol to write on the tape.
:param direction: Direction to move the tape head (LEFT or RIGHT).
:return: self for method chaining.

<a id="TuringMachine.TMState.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

<a id="TuringMachine.TMState.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

<a id="TuringMachine.TMTransition"></a>

## TMTransition Objects

```python
class TMTransition()
```

Class representing a transition in a Turing Machine.

<a id="TuringMachine.TMTransition.__init__"></a>

#### \_\_init\_\_

```python
def __init__(state: TMState, symbol: str, new_state: str, new_symbol: str,
             direction: TMDirection)
```

Initializes a Turing Machine transition.
:param state: The state this transition belongs to.
:param symbol: Input symbol that triggers the transition.
:param new_state: Name of the state to transition to.
:param new_symbol: Symbol to write on the tape.
:param direction: Direction to move the tape head (LEFT or RIGHT).

<a id="TuringMachine.TM"></a>

## TM Objects

```python
class TM()
```

Class representing a Turing Machine.

<a id="TuringMachine.TM.__init__"></a>

#### \_\_init\_\_

```python
def __init__(states: List[TMState],
             tape: List[str] = [],
             empty_symbol: Optional[str] = '_',
             implicit_reject: bool = False)
```

Initializes a Turing Machine.
:param states: List of TMState objects defining the machine's states.
:param tape: Initial tape content as a list of symbols.
:param empty_symbol: Symbol representing an empty cell on the tape.
:param implicit_reject: If True, the machine will implicitly reject if it reaches a state without transitions.

<a id="TuringMachine.TM.run"></a>

#### run

```python
def run(max_steps=1000, verbose=False, show_progress=False)
```

Runs the Turing Machine for a specified number of steps or until it reaches an accepting or rejecting state.
:param max_steps: Maximum number of steps to run the machine.
:param verbose: If True, prints the current configuration of the machine at each step.
:param show_progress: If True, shows a progress bar for the number of steps.
:return: True if the machine accepts the input, False if it rejects.

<a id="TuringMachine.TM.step"></a>

#### step

```python
def step()
```

Performs a single step of the Turing Machine.
This method reads the current symbol under the tape head, finds the appropriate transition,
updates the tape, moves the head, and changes the current state.

Note that in this implementation, the tape is extended with the empty symbol if the head position exceeds the current tape length,
and if the head moves left from the first position, a new empty symbol is added at the start of the tape.

:raises TMError: If no valid transition is found or if the transition leads to a non-existent state.

<a id="TuringMachine.TM._config_repr"></a>

#### \_config\_repr

```python
def _config_repr()
```


