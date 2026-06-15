#Project Structure
The project consists of seven Python files that simulate a healthcare IoT environment and demonstrate the impact of ransomware attacks on connected medical devices.
#Project Directory
│
├── i_pump.py                # Infusion Pump simulation
├── pacemaker.py             # Pacemaker simulation
├── monitor.py               # Patient Monitoring System simulation
├── imaging.py               # Imaging System simulation
├── server.py                # Central Hospital Server
├── ransomware_sim.py        # Ransomware attack 
├──decrypt.py                # Decryption simulation
└── README.md                # Project documentation

#File Descriptions
1. i_pump.py--Simulates an IoT-enabled infusion pump used for medication delivery.
2. 2. pacemaker.py--Simulates a pacemaker device connected to the healthcare network.
3. monitor.py--Simulates a patient monitoring system.
4. imaging.py--Simulates an imaging system such as MRI or CT scanners.
5. server.py--Represents the central hospital management server.
6. ransomware_sim.py--Simulates ransomware attack behavior within the healthcare IoT environment.
7. decrypt.py--Simulates decryption code to unlock the files attacked by the ransomware_sim
   
#Simulation Workflow
Hospital Server
       │
       ▼
Connected IoT Devices
├── Infusion Pump
├── Pacemaker
├── Monitoring System
└── Imaging System
       │
       ▼
Ransomware Simulation
       │
       ▼
Device Compromise
       │
       ▼
Data Encryption
       │
       ▼
Risk Assessment
       │
       ▼
Decryption & Recovery

#Running the Simulation
Step 1: Start the Hospital Server
---------python server.py

Step 2: Start the IoT Devices
---------python i_pump.py
---------python pacemaker.py
---------python monitor.py
---------python imaging.py

Step 3: Launch the Ransomware Simulation
---------python ransomware_sim.py

Step 4: Launch decryption code
---------decrypt.py

Step 5: Observe Results
The simulation will demonstrate:
#Device communication with the server
#Ransomware infection process
#Simulated data encryption
#Device compromise scenarios
#Recovery and decryption process
