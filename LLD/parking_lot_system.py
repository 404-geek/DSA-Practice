from abc import ABC, abstractmethod
from enum import Enum
from time import time
from typing import List, Optional, Dict


class GateStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    NON_FUNCTIONAL = "non_functional"


class PaymentStatus(Enum):
    PAID = "paid"
    UNPAID = "unpaid"


class VehicleType(Enum):
    TWO_WHEELER = "two_wheeler"
    FOUR_WHEELER = "four_wheeler"
    TRUCK = "truck"


class SlotStatus(Enum):
    FREE = "free"
    OCCUPIED = "occupied"


class Vehicle:
    def __init__(self, plate_no: str, vehicle_type: VehicleType):
        self.plate_no = plate_no
        self.vehicle_type = vehicle_type


class ParkingSlot:
    def __init__(self, slot_id: str, slot_type: VehicleType):
        self.slot_id = slot_id
        self.slot_type = slot_type
        self.status = SlotStatus.FREE
        self.vehicle: Optional[Vehicle] = None

    def can_fit(self, vehicle: Vehicle) -> bool:
        return self.status == SlotStatus.FREE and self.slot_type == vehicle.vehicle_type

    def assign_vehicle(self, vehicle: Vehicle):
        if not self.can_fit(vehicle):
            raise Exception("Vehicle cannot be assigned to this slot")

        self.vehicle = vehicle
        self.status = SlotStatus.OCCUPIED

    def remove_vehicle(self):
        self.vehicle = None
        self.status = SlotStatus.FREE


class Ticket:
    def __init__(self, ticket_id: str, vehicle: Vehicle, slot: ParkingSlot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.slot = slot
        self.payment_status = PaymentStatus.UNPAID
        self.start_time = time()
        self.end_time: Optional[float] = None
        self.amount = 0

    def close_ticket(self, amount: float):
        self.end_time = time()
        self.amount = amount
        self.payment_status = PaymentStatus.PAID


class Gate:
    def __init__(self, gate_id: str):
        self.gate_id = gate_id
        self.status = GateStatus.CLOSED

    def open_gate(self):
        if self.status == GateStatus.NON_FUNCTIONAL:
            raise Exception("Gate is not functional")
        self.status = GateStatus.OPEN

    def close_gate(self):
        if self.status == GateStatus.NON_FUNCTIONAL:
            raise Exception("Gate is not functional")
        self.status = GateStatus.CLOSED


class Level:
    def __init__(self, level_no: int):
        self.level_no = level_no
        self.slots: List[ParkingSlot] = []

    def add_slot(self, slot: ParkingSlot):
        self.slots.append(slot)

    def get_available_slot(self, vehicle: Vehicle) -> Optional[ParkingSlot]:
        for slot in self.slots:
            if slot.can_fit(vehicle):
                return slot
        return None


class PricingService:
    RATE_PER_HOUR = {
        VehicleType.TWO_WHEELER: 20,
        VehicleType.FOUR_WHEELER: 50,
        VehicleType.TRUCK: 100,
    }

    def calculate_amount(self, ticket: Ticket) -> float:
        end_time = time()
        duration_seconds = end_time - ticket.start_time
        duration_hours = max(1, int(duration_seconds // 3600) + 1)

        rate = self.RATE_PER_HOUR[ticket.vehicle.vehicle_type]
        return duration_hours * rate


class ParkingLotSystem(ABC):

    @abstractmethod
    def book_slot(self, vehicle: Vehicle) -> Ticket:
        pass

    @abstractmethod
    def free_slot(self, ticket_id: str) -> float:
        pass

    @abstractmethod
    def add_slot(self, level_no: int, slot: ParkingSlot):
        pass


class SimpleParkingLotSystem(ParkingLotSystem):
    def __init__(self):
        self.levels: List[Level] = []
        self.tickets: Dict[str, Ticket] = {}
        self.pricing_service = PricingService()
        self.ticket_counter = 1

    def add_level(self, level: Level):
        self.levels.append(level)

    def book_slot(self, vehicle: Vehicle) -> Ticket:
        for level in self.levels:
            slot = level.get_available_slot(vehicle)

            if slot:
                slot.assign_vehicle(vehicle)

                ticket_id = f"TICKET-{self.ticket_counter}"
                self.ticket_counter += 1

                ticket = Ticket(ticket_id, vehicle, slot)
                self.tickets[ticket_id] = ticket

                return ticket

        raise Exception("No available slot for this vehicle type")

    def free_slot(self, ticket_id: str) -> float:
        ticket = self.tickets.get(ticket_id)

        if not ticket:
            raise Exception("Invalid ticket ID")

        if ticket.payment_status == PaymentStatus.PAID:
            raise Exception("Ticket already closed")

        amount = self.pricing_service.calculate_amount(ticket)

        ticket.slot.remove_vehicle()
        ticket.close_ticket(amount)

        return amount

    def add_slot(self, level_no: int, slot: ParkingSlot):
        for level in self.levels:
            if level.level_no == level_no:
                level.add_slot(slot)
                return

        raise Exception("Level not found")

    def get_available_slots_count(self) -> int:
        count = 0

        for level in self.levels:
            for slot in level.slots:
                if slot.status == SlotStatus.FREE:
                    count += 1

        return count

    def get_occupied_slots_count(self) -> int:
        count = 0

        for level in self.levels:
            for slot in level.slots:
                if slot.status == SlotStatus.OCCUPIED:
                    count += 1

        return count


if __name__ == "__main__":
    parking_system = SimpleParkingLotSystem()

    level1 = Level(1)
    level1.add_slot(ParkingSlot("L1-S1", VehicleType.TWO_WHEELER))
    level1.add_slot(ParkingSlot("L1-S2", VehicleType.FOUR_WHEELER))
    level1.add_slot(ParkingSlot("L1-S3", VehicleType.TRUCK))

    level2 = Level(2)
    level2.add_slot(ParkingSlot("L2-S1", VehicleType.FOUR_WHEELER))
    level2.add_slot(ParkingSlot("L2-S2", VehicleType.TWO_WHEELER))

    parking_system.add_level(level1)
    parking_system.add_level(level2)

    vehicle1 = Vehicle("KA-01-1234", VehicleType.FOUR_WHEELER)
    vehicle2 = Vehicle("KA-02-5678", VehicleType.TWO_WHEELER)

    ticket1 = parking_system.book_slot(vehicle1)
    print("Ticket created:", ticket1.ticket_id, "Slot:", ticket1.slot.slot_id)

    ticket2 = parking_system.book_slot(vehicle2)
    print("Ticket created:", ticket2.ticket_id, "Slot:", ticket2.slot.slot_id)

    print("Available slots:", parking_system.get_available_slots_count())
    print("Occupied slots:", parking_system.get_occupied_slots_count())

    amount = parking_system.free_slot(ticket1.ticket_id)
    print("Amount paid:", amount)

    print("Available slots:", parking_system.get_available_slots_count())
    print("Occupied slots:", parking_system.get_occupied_slots_count())