from abc import ABC
from typing import List, Dict
from collections import deque
import datetime


# Helper class to store time slot
class TimeSlot:
    def __init__(self, start_time: str, end_time: str):
        self.start_time = datetime.datetime.strptime(start_time, "%H:%M")
        self.end_time = datetime.datetime.strptime(end_time, "%H:%M")

    def duration_valid(self) -> bool:
        return (self.end_time - self.start_time).seconds == 30 * 60  # 30 minutes

    def within_business_hours(self) -> bool:
        return self.start_time.hour >= 9 and self.end_time.hour <= 21

    def __str__(self):
        return f"{self.start_time.strftime('%H:%M')}-{self.end_time.strftime('%H:%M')}"


# Doctor class
class Doctor:
    def __init__(self, name: str, specialty: str):
        self._name = name
        self._specialty = specialty
        self._appointments = {}  # Booking ID -> Slot
        self._waitlist = {}  # Slot -> List of Patients waiting for that slot
        self._available_slots = []  # Available time slots

    def get_name(self) -> str:
        return self._name

    def get_specialty(self) -> str:
        return self._specialty

    def get_available_slots(self) -> List['TimeSlot']:
        return self._available_slots

    def add_slot(self, slot: TimeSlot):
        # Add a slot to available slots
        self._available_slots.append(slot)

    def remove_slot(self, slot: TimeSlot):
        # Remove a slot from available slots (after booking or cancellation)
        self._available_slots.remove(slot)

    def add_appointment(self, booking_id: str, slot: TimeSlot):
        # Add an appointment to the doctor’s record
        self._appointments[booking_id] = slot

    def remove_appointment(self, booking_id: str):
        # Remove the appointment from the doctor's record
        if booking_id in self._appointments:
            del self._appointments[booking_id]

    def is_slot_booked(self, start_time: str) -> bool:
        # Check if the slot is booked by any patient
        for slot in self._appointments.values():
            if slot.start_time.strftime("%H:%M") == start_time:
                return True
        return False

    def add_to_waitlist(self, slot: TimeSlot, patient_name: 'Patient', booking_id: int):
        if slot not in self._waitlist:
            self._waitlist[slot] = deque()
        self._waitlist[slot].append((patient_name, booking_id))

    def has_waitlist_for_slot(self, slot: TimeSlot) -> bool:
        # Check if there are any patients on the waitlist for this slot
        return slot in self._waitlist and len(self._waitlist[slot]) > 0

    def get_first_waitlist_patient_for_slot(self, slot: TimeSlot):
        # Return the first patient from the waitlist for a particular slot
        if slot in self._waitlist and len(self._waitlist[slot]) > 0:
            return self._waitlist[slot][0]
        return None

    def remove_from_waitlist(self, slot: TimeSlot, patient_name: 'Patient', booking_id: int):
        # Remove a patient from the waitlist for a particular slot
        if slot in self._waitlist and patient_name in self._waitlist[slot]:
            self._waitlist[slot].remove((patient_name, booking_id))



# Patient class
class Patient:
    def __init__(self, name: str):
        self.name = name
        self.appointments = {}

    def add_appointment(self, booking_id: int, slot: TimeSlot):
        self.appointments[booking_id] = slot

    def remove_appointment(self, booking_id: int):
        if booking_id in self.appointments:
            del self.appointments[booking_id]

    def get_name(self):
        return self.name


# Repository to store data in memory
class InMemoryRepository:
    def __init__(self):
        self._doctors = {}
        self._patients = {}
        self._bookings = {}
        self._waitlists = {}

    def add_doctor(self, doctor: Doctor):
        self._doctors[doctor.get_name()] = doctor

    def get_doctor(self, name: str) -> Doctor:
        return self._doctors.get(name)

    def add_patient(self, patient: Patient):
        self._patients[patient.name] = patient

    def get_patient(self, name: str) -> Patient:
        return self._patients.get(name)

    def add_booking(self, booking: Dict) -> int:
        booking_id = len(self._bookings) + 1
        self._bookings[booking_id] = booking
        return booking_id

    def get_booking(self, booking_id: int) -> Dict:
        return self._bookings.get(booking_id)

    def remove_booking(self, booking_id: int):
        if booking_id in self._bookings:
            del self._bookings[booking_id]

    def add_to_waitlist(self, doctor_name: str, patient_name: str, slot: TimeSlot, booking_id: int):
        doctor = self.get_doctor(doctor_name)
        if doctor:
            doctor.add_to_waitlist(slot, patient_name, booking_id)
    def remove_from_waitlist(self, doctor_name: str, patient_name: str, slot: TimeSlot):
        doctor = self.get_doctor(doctor_name)
        if doctor:
            doctor.remove_from_waitlist(slot, patient_name)

    def get_waitlist(self, doctor_name: str) -> Dict:
        doctor = self.get_doctor(doctor_name)
        if doctor:
            return doctor.waitlist
        return {}


# DoctorService (abstract class)
class DoctorService(ABC):
    def register_doc(self, name: str, specialty: str) -> str:
        pass

    def mark_doc_avail(self, doctor_name: str, slots: List[str]) -> str:
        pass

    def show_avail_by_specialty(self, specialty: str) -> List[str]:
        pass


# DoctorServiceImpl (concrete class)
class DoctorServiceImpl(DoctorService):
    def __init__(self, repository: InMemoryRepository):
        self._repository = repository

    def register_doc(self, name: str, specialty: str) -> str:
        doctor = Doctor(name, specialty)
        self._repository.add_doctor(doctor)
        return f"Welcome Dr. {name} !!"

    def mark_doc_avail(self, doctor_name: str, slots: List[str]) -> str:
        doctor = self._repository.get_doctor(doctor_name)
        if not doctor:
            return f"Doctor {doctor_name} is not registered."

        for slot in slots:
            start, end = slot.split("-")
            new_slot = TimeSlot(start, end)
            if not new_slot.duration_valid():
                return f"Sorry Dr. {doctor_name}, slots are 30 mins only."
            if not new_slot.within_business_hours():
                return f"Sorry Dr. {doctor_name}, slots must be between 9:00 AM and 9:00 PM."
            doctor.add_slot(new_slot)

        return "Done Doc!"

    def show_avail_by_specialty(self, specialty: str) -> List[str]:
        available = []
        for doctor in self._repository._doctors.values():
            if doctor.get_specialty() == specialty:
                for slot in doctor.get_available_slots():
                    available.append(f"{doctor.get_name()}: {slot}")
        return available


# PatientService (abstract class)
class PatientService(ABC):
    def register_patient(self, name: str) -> str:
        pass


# PatientServiceImpl (concrete class)
class PatientServiceImpl(PatientService):
    def __init__(self, repository: InMemoryRepository):
        self._repository = repository

    def register_patient(self, name: str) -> str:
        patient = Patient(name)
        self._repository.add_patient(patient)
        return f"Welcome {name} !!"


# BookingService (abstract class)
class BookingService(ABC):
    def book_appointment(self, patient_name: str, doctor_name: str, start_time: str) -> str:
        pass

    def cancel_booking(self, booking_id: int) -> str:
        pass

    def view_appointments(self, patient_name: str) -> str:
        pass


# BookingServiceImpl (concrete class)
class BookingServiceImpl(BookingService):
    def __init__(self, repository: InMemoryRepository):
        self._repository = repository

    def _find_slot_for_time(self, doctor: Doctor, start_time: str) -> TimeSlot:
        # Helper function to find a slot for the given time
        for slot in doctor.get_available_slots():
            if slot.start_time.strftime("%H:%M") == start_time:
                return slot
        return None

    def book_appointment(self, patient_name: str, doctor_name: str, start_time: str) -> str:
        # Fetch the doctor and patient from the repository
        patient = self._repository.get_patient(patient_name)
        doctor = self._repository.get_doctor(doctor_name)
        if not patient or not doctor:
            return "Doctor or Patient not found."
        
        # Check if the slot is available for booking
        slot = self._find_slot_for_time(doctor, start_time)
        if not slot:
            return "Slot not available."

        # Check if the slot is already booked
        if doctor.is_slot_booked(start_time):
            # If slot is already booked, check if the patient should be added to waitlist
            booking_id = self._repository.add_booking({'patient': patient, 'doctor': doctor, 'slot': slot})
            doctor.add_to_waitlist(slot, patient, booking_id)
            return f"Slot is booked, you have been added to the waitlist. Booking ID: {booking_id}"
        
        # Slot is available, proceed with booking
        booking_id = self._repository.add_booking({
            "patient": patient,
            "doctor": doctor,
            "slot": slot
        })

        # Update doctor and patient
        doctor.add_appointment(booking_id, slot)
        patient.add_appointment(booking_id, slot)
        
        return f"Booked. Booking ID: {booking_id}"

    def cancel_booking(self, booking_id: str) -> str:
        # Fetch the booking from the repository
        booking = self._repository.get_booking(booking_id)
        if not booking:
            return f"Booking {booking_id} not found."
        
        patient = booking['patient']
        doctor = booking['doctor']
        slot = booking['slot']
        
        # Cancel the appointment
        patient.remove_appointment(booking_id)
        doctor.remove_appointment(booking_id)
        
        # Make the slot available again
        doctor.add_slot(slot)  # Re-add the slot to available slots
        
        # Remove from waitlist if any patient is waiting for this slot
        if doctor.has_waitlist_for_slot(slot):
            # Get the first patient from the waitlist for this slot
            next_patient, booking_id = doctor.get_first_waitlist_patient_for_slot(slot)
            # Remove the patient from the waitlist
            doctor.remove_from_waitlist(slot, next_patient, booking_id)
            
            # Update both the doctor and patient's objects
            doctor.add_appointment(booking_id, slot)
            next_patient.add_appointment(booking_id, slot)

            return f"Appointment cancelled. The next patient in waitlist has been assigned the slot. New booking ID: {booking_id}"

        return f"Appointment cancelled. Slot is now available."

    def view_appointments(self, patient_name: str) -> str:
        patient = self._repository.get_patient(patient_name)
        if not patient:
            return f"Patient {patient_name} is not registered."

        appointments = []
        for booking_id, slot in patient.appointments.items():
            booking = self._repository.get_booking(booking_id)
            appointments.append(f"booking id: {booking_id}, doctor: {booking['doctor'].get_name()}, slot: {slot}")
        return "\n".join(appointments) if appointments else "No appointments."


# System class
class System:
    def __init__(self):
        self._repository = InMemoryRepository()
        self._doctor_service = DoctorServiceImpl(self._repository)
        self._patient_service = PatientServiceImpl(self._repository)
        self._booking_service = BookingServiceImpl(self._repository)

    def register_doc(self, name: str, specialty: str) -> str:
        return self._doctor_service.register_doc(name, specialty)

    def mark_doc_avail(self, name: str, slots: List[str]) -> str:
        return self._doctor_service.mark_doc_avail(name, slots)

    def show_avail_by_specialty(self, specialty: str) -> List[str]:
        return self._doctor_service.show_avail_by_specialty(specialty)

    def register_patient(self, name: str) -> str:
        return self._patient_service.register_patient(name)

    def book_appointment(self, patient_name: str, doctor_name: str, start_time: str) -> str:
        return self._booking_service.book_appointment(patient_name, doctor_name, start_time)

    def cancel_booking(self, booking_id: int) -> str:
        return self._booking_service.cancel_booking(booking_id)

    def view_appointments(self, patient_name: str) -> str:
        return self._booking_service.view_appointments(patient_name)


if __name__ == "__main__":
    system = System()

    # Example usage in the main block
    print(system.register_doc("Curious", "Cardiologist"))
    print(system.mark_doc_avail("Curious", ["09:30-10:00", "12:30-13:00", "16:00-16:30"]))  # Valid slots

    print(system.register_doc("Dreadful", "Dermatologist"))
    print(system.mark_doc_avail("Dreadful", ["09:30-10:00", "12:30-13:00", "16:00-16:30"]))  # Valid slots

    # Register patients
    print(system.register_patient("PatientA"))
    print(system.register_patient("PatientB"))

    # Show availability for Cardiologists
    availabilities = system.show_avail_by_specialty("Cardiologist")
    for availability in availabilities:
        print(availability)

    # Book an appointment for PatientA with Dr. Curious
    print(system.book_appointment("PatientA", "Curious", "12:30"))

    # Show availability after booking
    availabilities = system.show_avail_by_specialty("Cardiologist")
    for availability in availabilities:
        print(availability)

    # Cancel the appointment
    print(system.cancel_booking(1000))

    # Show availability after canceling the appointment
    availabilities = system.show_avail_by_specialty("Cardiologist")
    for availability in availabilities:
        print(availability)

    # Book another appointment for PatientB with Dr. Curious
    print(system.book_appointment("PatientB", "Curious", "12:30"))

    print(system.view_appointments("PatientA"))
    print(system.view_appointments("PatientB"))  

    #After Cancelling patientA's appointment with Dr. Curious, appointment should be shown in PatientB
    print(system.cancel_booking(1))
    print(system.view_appointments("PatientA"))
    print(system.view_appointments("PatientB"))  

    # Register another Dermatologist
    print(system.register_doc("Daring", "Dermatologist"))
    print(system.mark_doc_avail("Daring", ["11:30-12:00", "14:00-14:30"]))  # Valid slots
