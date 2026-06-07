from abc import ABC, abstractmethod
from enum import Enum

class Status(Enum):
    MOVING = 'moving'
    STOPPED = 'stopped'
    DOORS_OPEN = 'doors_open'
    NOT_AVAILABLE = 'not_available'

class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    NONE = 'none'

class elevator:

    def __init__(self, id):
        self.id = id
        self.current_floor = 0
        self.direction = Direction.NONE
        self.up_floors = set()
        self.down_floors = set()
        self.status = Status.STOPPED

    def is_idle(self):
        return self.direction == Direction.NONE

    def add_stop(self, floor, direction):
        if direction == Direction.UP:
            self.up_floors.add(floor)
        elif direction == Direction.DOWN:
            self.down_floors.add(floor)

        if self.direction == Direction.NONE:
            self.direction = direction
            self.status = Status.MOVING

    def move(self):
        if self.direction == Direction.UP:
            self.current_floor += 1
            self.status = Status.MOVING

            if self.current_floor in self.up_floors:
                self.up_floors.remove(self.current_floor)
                self.status = Status.DOORS_OPEN
                print(f"Elevator {self.id} opened at floor {self.current_floor}")

        elif self.direction == Direction.DOWN:
            self.current_floor -= 1
            self.status = Status.MOVING

            if self.current_floor in self.down_floors:
                self.down_floors.remove(self.current_floor)
                self.status = Status.DOORS_OPEN
                print(f"Elevator {self.id} opened at floor {self.current_floor}")

        self._update_direction()

    def _update_direction(self):
        if self.direction == Direction.UP:
            if any(f > self.current_floor for f in self.up_floors):
                self.direction = Direction.UP
            elif self.down_floors:
                self.direction = Direction.DOWN
            else:
                self.direction = Direction.NONE
                self.status = Status.STOPPED

        elif self.direction == Direction.DOWN:
            if any(f < self.current_floor for f in self.down_floors):
                self.direction = Direction.DOWN
            elif self.up_floors:
                self.direction = Direction.UP
            else:
                self.direction = Direction.NONE
                self.status = Status.STOPPED


class ElevatorSystem(ABC):

    def __init__(self):
        self.elevators = []

    def add_elevator(self, elevator):
        self.elevators.append(elevator)
    
    @abstractmethod
    def request_elevator(self, floor, direction):
        pass

    @abstractmethod
    def move_elevator(self, elevator_id):
        pass


class classic_elevator_system(ElevatorSystem):

    def get_all_idle_elevators(self):
        return [elevator for elevator in self.elevators if elevator.is_idle() and not elevator.status == Status.NOT_AVAILABLE]
    
    def get_all_elevators_moving_in_direction(self, direction):
        return [elevator for elevator in self.elevators if elevator.direction == direction and not elevator.status == Status.NOT_AVAILABLE]
    

    def request_elevator(self, floor, direction):
        # Logic to find the best elevator to serve the request
        best_elevator = None
        min_distance = float('inf')

        idle_elevators = self.get_all_idle_elevators()
        moving_elevators = self.get_all_elevators_moving_in_direction(direction)

        for elevator in moving_elevators:
            if direction == Direction.UP and elevator.current_floor < floor:
                distance = floor - elevator.current_floor
                if distance < min_distance:
                    min_distance = distance
                    best_elevator = elevator
            elif direction == Direction.DOWN and elevator.current_floor > floor:
                distance = elevator.current_floor - floor
                if distance < min_distance:
                    min_distance = distance
                    best_elevator = elevator
        
        if not best_elevator and idle_elevators:
            best_elevator = min(idle_elevators, key=lambda e: abs(e.current_floor - floor))

        if best_elevator:
            if direction == Direction.DOWN:
                best_elevator.down_floors.add(floor)
            else:
                best_elevator.up_floors.add(floor)
            return best_elevator
        else:
            return None  # No available elevator at the moment
        
    def move_elevator(self, elevator):
        elevator.move()


if __name__ == "__main__":
    system = classic_elevator_system()
    system.add_elevator(elevator(1))
    system.add_elevator(elevator(2))
    system.add_elevator(elevator(3))

    a = system.request_elevator(5, Direction.UP) 
    a.add_stop(5, Direction.UP)
    a.add_stop(3, Direction.DOWN)
    b = system.request_elevator(3, Direction.DOWN)

    while a.status != Status.STOPPED:
        system.move_elevator(a)