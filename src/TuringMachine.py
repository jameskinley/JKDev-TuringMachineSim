"""
Module: JKDev Turing Machine
Author: James Kinley

This module provides a basic implementation of a deterministic Turing Machine.
It includes classes for states, transitions, and the machine itself, and is designed to be extensible for various Turing Machine configurations.
"""

from typing import List, Optional
from enum import Enum
from tqdm import tqdm

class TMError(Exception):
    """Base class for exceptions in this module."""
    pass

class TMDirection(Enum):
    """Enum for Turing Machine head movement direction."""
    LEFT = -1
    RIGHT = 1

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"TMDirection.{self.name}"
    
class TMStateType(Enum):
    """Enum for Turing Machine state types."""
    START = 0
    ACCEPTING = 1
    REJECTING = 2
    NORMAL = 3

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"TMStateType.{self.name}"

class TMState:
    """Class representing a state in a Turing Machine."""

    def __init__(self, name : str, state_type: TMStateType = TMStateType.NORMAL):
        """
        Initializes a Turing Machine state.
        :param name: Name of the state.
        :param state_type: Type of the state (START, ACCEPTING, REJECTING, NORMAL).
        """
        self.name = name
        self.state_type = state_type
        self.transitions = []

    def add_transition(self, symbol, new_state, new_symbol, direction):
        """
        Adds a transition to the state.
        :param symbol: Input symbol that triggers the transition.
        :param new_state: Name of the state to transition to.
        :param new_symbol: Symbol to write on the tape.
        :param direction: Direction to move the tape head (LEFT or RIGHT).
        :return: self for method chaining.
        """
        transition = TMTransition(self, symbol, new_state, new_symbol, direction)
        self.transitions.append(transition)
        return self

    def __str__(self):
        return self.name
    def __repr__(self):
        return f"TMState(name={self.name}, type={self.state_type})"

class TMTransition:
    """Class representing a transition in a Turing Machine."""

    def __init__(self, state: TMState, symbol: str, new_state: str, new_symbol: str, direction: TMDirection):
        """
        Initializes a Turing Machine transition.
        :param state: The state this transition belongs to.
        :param symbol: Input symbol that triggers the transition.
        :param new_state: Name of the state to transition to.
        :param new_symbol: Symbol to write on the tape.
        :param direction: Direction to move the tape head (LEFT or RIGHT).
        """
        self.state = state
        self.symbol = symbol
        self.new_state = new_state
        self.new_symbol = new_symbol
        self.direction = direction

class TM:
    """Class representing a Turing Machine."""

    def __init__(self, states : List[TMState], tape: List[str] = [], empty_symbol: Optional[str] = '_', implicit_reject: bool = False):
        """
        Initializes a Turing Machine.
        :param states: List of TMState objects defining the machine's states.
        :param tape: Initial tape content as a list of symbols.
        :param empty_symbol: Symbol representing an empty cell on the tape.
        :param implicit_reject: If True, the machine will implicitly reject if it reaches a state without transitions.
        """
        self.empty_symbol = empty_symbol
        self.tape = tape
        self.states = states
        self.implicit_reject = implicit_reject
        self.head_pos = 0
        
        start = [s for s in states if s.state_type == TMStateType.START]
        if len(start) != 1:
            raise TMError("There must be exactly one start state.")
        if len(start) == 0:
            raise TMError("There must be a start state.")
        
        self.current_state = start[0]

        self.accepting_states = [s for s in states if s.state_type == TMStateType.ACCEPTING]
        self.rejecting_states = [s for s in states if s.state_type == TMStateType.REJECTING]

        if len(self.accepting_states) == 0:
            raise TMError("There must be at least one accepting state.")
        if not self.implicit_reject and len(self.rejecting_states) == 0:
            raise TMError("There must be at least one rejecting state.")
        
    def run(self, max_steps=1000, verbose=False, show_progress=False):
        """
        Runs the Turing Machine for a specified number of steps or until it reaches an accepting or rejecting state.
        :param max_steps: Maximum number of steps to run the machine.
        :param verbose: If True, prints the current configuration of the machine at each step.
        :param show_progress: If True, shows a progress bar for the number of steps.
        :return: True if the machine accepts the input, False if it rejects.
        """

        iterable = tqdm(range(max_steps), desc=f"Running Turing Machine for at most {max_steps}") if show_progress else range(max_steps)
        for _ in iterable:
            if verbose:
                print(self._config_repr())

            if not self.implicit_reject and self.current_state is None:
                raise TMError("Invalid: Cannot Perform Process Tape input due to missing transitions. Please ensure deterministic TMs are used.")
            elif self.current_state is None:
                return False

            if self.current_state.state_type == TMStateType.ACCEPTING:
                return True
            if self.current_state.state_type == TMStateType.REJECTING:
                return False
            
            self.step()

    def step(self):
        """
        Performs a single step of the Turing Machine.
        This method reads the current symbol under the tape head, finds the appropriate transition,
        updates the tape, moves the head, and changes the current state.

        Note that in this implementation, the tape is extended with the empty symbol if the head position exceeds the current tape length,
        and if the head moves left from the first position, a new empty symbol is added at the start of the tape.

        :raises TMError: If no valid transition is found or if the transition leads to a non-existent state.
        """

        # add empty symbol to tape if there's nothing there
        if self.head_pos >= len(self.tape): self.tape.append(self.empty_symbol)
        
        transitions = [t for t in self.current_state.transitions if t.symbol == self.tape[self.head_pos]] 
        if len(transitions) != 1:
            raise TMError("Invalid: No possible transition was found. Please ensure deterministic TMs are used.")
        
        self.tape[self.head_pos] = transitions[0].new_symbol

        new_states = [s for s in self.states if s.name == transitions[0].new_state]
        if len(new_states) != 1:
            raise TMError("Invalid: Transition to a non-existent state. Please ensure deterministic TMs are used.")

        self.current_state = new_states[0]

        if self.head_pos == 0 and transitions[0].direction == TMDirection.LEFT:
            self.tape.insert(0, self.empty_symbol)
            return
        if transitions[0].direction == TMDirection.LEFT:
            self.head_pos -= 1
            return
        
        self.head_pos += 1

    def _config_repr(self):
        return f"Tape: {self.tape}, Head Position: {self.head_pos}, Current State: {self.current_state.name}"