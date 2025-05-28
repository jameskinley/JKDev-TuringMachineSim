"""
Author: James Kinley

Unit tests for the Turing Machine implementation.
"""

import pytest
from ..src.TuringMachine import TMError, TMDirection, TMStateType, TMState, TMTransition, TM

def test_direction_str_repr():
    assert str(TMDirection.LEFT) == 'LEFT'
    assert repr(TMDirection.RIGHT) == 'TMDirection.RIGHT'

def test_statetype_str_repr():
    assert str(TMStateType.ACCEPTING) == 'ACCEPTING'
    assert repr(TMStateType.REJECTING) == 'TMStateType.REJECTING'

def test_state_str_repr_and_add_transition():
    s = TMState('A', TMStateType.NORMAL)
    assert str(s) == 'A'
    assert repr(s) == 'TMState(name=A, type=NORMAL)'
    returned = s.add_transition('x', 'B', 'y', TMDirection.RIGHT)
    assert returned is s
    assert s.transitions and isinstance(s.transitions[0], TMTransition)

def test_transition_properties():
    s = TMState('X', TMStateType.START)
    t = TMTransition(s, 'a', 'X', 'b', TMDirection.LEFT)
    assert t.state is s
    assert t.symbol == 'a'
    assert t.new_state == 'X'
    assert t.new_symbol == 'b'
    assert t.direction == TMDirection.LEFT

def test_init_errors_missing_states():
    with pytest.raises(TMError, match="exactly one start state"): TM([], [])
    start = TMState('S', TMStateType.START)
    accepting = TMState('A', TMStateType.ACCEPTING)
    rejecting = TMState('R', TMStateType.REJECTING)
    with pytest.raises(TMError, match="exactly one start state"): TM([accepting, rejecting], [])
    with pytest.raises(TMError, match="at least one accepting state"): TM([start, rejecting], [])
    with pytest.raises(TMError, match="at least one rejecting state"): TM([start, accepting], [])

def test_config_repr():
    start = TMState('S', TMStateType.START)
    acc = TMState('A', TMStateType.ACCEPTING)
    rej = TMState('R', TMStateType.REJECTING)
    m = TM([start, acc, rej], ['0'], empty_symbol='0')
    expected = "Tape: ['0'], Head Position: 0, Current State: S"
    assert m._config_repr() == expected

def test_run_accept_and_reject():
    start = TMState('S', TMStateType.START)
    acc = TMState('A', TMStateType.ACCEPTING)
    rej = TMState('R', TMStateType.REJECTING)
    start.add_transition('_', 'A', '_', TMDirection.RIGHT)
    m1 = TM([start, acc, rej], [], empty_symbol='_')
    assert m1.run() is True
    start2 = TMState('S2', TMStateType.START)
    start2.add_transition('_', 'R', '_', TMDirection.RIGHT)
    m2 = TM([start2, acc, rej], [], empty_symbol='_')
    assert m2.run() is False

def test_no_transitions_raises_error():
    start = TMState('S', TMStateType.START)
    accepting = TMState('A', TMStateType.ACCEPTING)
    rejecting = TMState('R', TMStateType.REJECTING)
    m = TM([start, accepting, rejecting], [], empty_symbol='_')
    with pytest.raises(TMError, match="No possible transition"): m.run()

def test_multiple_transitions_error():
    s = TMState('S', TMStateType.START)
    a = TMState('A', TMStateType.ACCEPTING)
    r = TMState('R', TMStateType.REJECTING)
    s.add_transition('_', 'A', '_', TMDirection.RIGHT)
    s.add_transition('_', 'R', '_', TMDirection.RIGHT)
    m = TM([s, a, r], [], empty_symbol='_')
    with pytest.raises(TMError, match="No possible transition"): m.step()

def test_transition_to_nonexistent_state_error():
    s = TMState('S', TMStateType.START)
    a = TMState('A', TMStateType.ACCEPTING)
    r = TMState('R', TMStateType.REJECTING)
    s.add_transition('_', 'X', '_', TMDirection.RIGHT)
    m = TM([s, a, r], [], empty_symbol='_')
    with pytest.raises(TMError, match="non-existent state"): m.step()

def test_tape_extension_and_right_movement():
    s = TMState('S', TMStateType.START)
    a = TMState('A', TMStateType.ACCEPTING)
    r = TMState('R', TMStateType.REJECTING)
    s.add_transition('_', 'A', '1', TMDirection.RIGHT)
    m = TM([s, a, r], [], empty_symbol='_')
    assert m.run() is True
    assert m.tape == ['1']
    assert m.head_pos == 1

def test_left_insertion_at_start():
    s = TMState('S', TMStateType.START)
    a = TMState('A', TMStateType.ACCEPTING)
    r = TMState('R', TMStateType.REJECTING)
    s.add_transition('_', 'S', '0', TMDirection.LEFT)
    # single step
    m = TM([s, a, r], [], empty_symbol='_')
    m.step()
    assert m.tape == ['_', '0']
    assert m.head_pos == 0

def test_head_movement_left_nonzero():
    s = TMState('S', TMStateType.START)
    a = TMState('A', TMStateType.ACCEPTING)
    r = TMState('R', TMStateType.REJECTING)
    s.add_transition('x', 'S', 'y', TMDirection.LEFT)
    m = TM([s, a, r], ['x', 'x'], empty_symbol='_')
    m.head_pos = 1
    m.states = [s, a, r]
    m.current_state = s

    m.step()

    assert m.tape == ['x', 'y']
    assert m.head_pos == 0
