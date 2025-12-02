from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Specialty(Base):

    __tablename__= 'specialties'

    id=  Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    #relationship
    doctors = relationship('Doctor', back_populates='specialty')

class Doctor(Base):
    __tablename__= 'doctors'
    id= Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialty_id = Column(Integer, ForeignKey('specialties.id'))
    gender=Column(String, nullable=False)

    #relaionship
    specialty = relationship('Specialty', back_populates='doctors')

    #Remember to add the doctor's appointment relationship
    appointments = relationship('Appointment',back_populates='doctor')


class Patient(Base):
    __tablename__='patients'
    id=Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    #Remember to add the appointne relationship
    appointments = relationship('Appointment', back_populates='patient')

class Appointment(Base):
    __tablename__='appointments'
    id=Column(Integer, primary_key=True)
    doctor_id=Column(Integer, ForeignKey('doctors.id'))
    patient_id=Column(Integer, ForeignKey('patients.id'))
    treatment=Column(String, nullable=False)
    appointment_datetime=Column(DateTime, default=datetime.utcnow)

    #Relationships
    doctor= relationship('Doctor', back_populates='appointments')
    patient = relationship('Patient', back_populates='appointments')
    