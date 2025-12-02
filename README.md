# CREATE — Add Records

## Create Specialties
<pre> 
``` 
cardiology = Specialty(name="Cardiology")
dentistry = Specialty(name="Dentistry")

session.add_all([cardiology, dentistry])
session.commit() 
```
</pre>
## Create Doctors
doc_john = Doctor(name="Dr. John", specialty=cardiology)
doc_mary = Doctor(name="Dr. Mary", specialty=dentistry)

session.add_all([doc_john, doc_mary])
session.commit()

## Create Patients
pat_sam = Patient(name="Sam Tomashi")
pat_jane = Patient(name="Jane Doe")

session.add_all([pat_sam, pat_jane])
session.commit()

## Create Appointments
appt1 = Appointment(
    doctor=doc_john,
    patient=pat_sam,
    date="2025-01-01",
    description="General heart check"
)

appt2 = Appointment(
    doctor=doc_mary,
    patient=pat_jane,
    date="2025-02-10",
    description="Teeth cleaning"
)

session.add_all([appt1, appt2])
session.commit()

# READ — Fetch Records

## Get all doctors
doctors = session.query(Doctor).all()
for d in doctors:
    print(d.id, d.name, d.specialty.name)

## Get all patients
patients = session.query(Patient).all()
for p in patients:
    print(p.id, p.name)

## Get all appointments with full details
appointments = session.query(Appointment).all()
for a in appointments:
    print(a.id, a.doctor.name, a.patient.name, a.date, a.description)

# UPDATE — Modify Records

## Update a patient name
patient = session.query(Patient).filter_by(name="Jane Doe").first()
patient.name = "Jane Smith"
session.commit()

## Update an appointment description
appointment = session.query(Appointment).first()
appointment.description = "Updated checkup details"
session.commit()

# DELETE — Remove Records
## Delete an appointment
appt = session.query(Appointment).first()
session.delete(appt)
session.commit()
