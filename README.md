# Smart Grid Fault Detection System

## Research Question
Does incorporating physics-informed synthetic 
data generation improve LSTM fault classifier 
accuracy in data-scarce rural Kenyan grid 
infrastructure contexts?

## Hypothesis
A PINN-augmented training approach will 
outperform purely data-driven LSTM methods 
by a minimum of 15% classification accuracy 
under low-data conditions (fewer than 500 
labeled fault events).

## Target
KSEF 2027 Regional → KSEF National → ISEF 2027

## Project Overview
A low-cost embedded AI system for monitoring 
rural power grid infrastructure in Kenya. 
The system uses an ESP32-S3 microcontroller 
with current and voltage sensors (SCT-013 
and ZMPT101B) to detect fault conditions in 
real time. Detected faults trigger SMS alerts 
via a SIM800L GSM module.

The core research contribution addresses the 
low-data problem common to rural grid 
infrastructure: insufficient labeled fault 
event data for training accurate machine 
learning classifiers. A Physics-Informed 
Neural Network (PINN) generates synthetic 
fault signatures grounded in real 
electromagnetic and circuit physics, 
augmenting the limited real dataset used to 
train an LSTM classifier.

## Hardware
- ESP32-S3 microcontroller (MicroPython)
- SCT-013-000 current sensor
- ZMPT101B voltage sensor
- SIM800L GSM module (SMS alerts)
- Solar panel + 18650 battery (off-grid power)

## Software Stack
- MicroPython (on-device firmware)
- Python + PyTorch (model training)
- TensorFlow Lite (on-device inference)
- PINN (synthetic fault data generation)

## Progress Log

### Foundation (Python fluency)
- [x] Ex1: Multi-reading fault detector — 
      average current, threshold detection
- [x] Ex2: Multi-condition fault classifier — 
      current + voltage, 4 classification states
- [x] Ex3: Random sensor simulator — 
      generates synthetic current readings
- [x] Ex4: Fault logger — writes detection 
      results to text file
- [x] Ex5: Multi-sensor fault confirmation — 
      3-sensor agreement logic
- [x] Ex6: 24-hour CSV simulation — 1440 
      minute-by-minute readings logged to CSV

### Hardware and foundation continuation(August 2026)
- [ ] Ex7: CSV fault analysis — hour with 
      most faults, longest streaks 
- [ ] Ex8: Timestamps in CSV (00:00-23:59 format)
- [ ] Ex9: Multiple fault types with 
      probability weights
- [ ] Ex10: Multi-zone grid simulation
- [ ] Ex11: Fault report summary across zones
- [ ] Ex12: MicroPython syntax bridge exercise
- [ ] Ex13: NumPy — RMS calculation
- [ ] Ex14: NumPy — FFT frequency analysis
- [ ] Ex15: Matplotlib — 24hr data visualization
- [ ] Ex16: Matplotlib — fault distribution by hour
- [ ] Ex17: Power factor calculation 
      (voltage + current together)
- [ ] Ex18: Harmonic distortion detection
- [ ] Ex19: Synthetic fault signature generation 
      (PINN groundwork)
- [ ] Ex20: Threshold vs statistical detection 
      comparison
- [ ] ESP32-S3 setup and MicroPython flashed
- [ ] SCT-013 sensor connected and reading
- [ ] Real current data collection begins
- [ ] Threshold-based fault detection on 
      real hardware

### AI/Research (November-December 2026)
- [ ] PyTorch LSTM classifier training
- [ ] PINN synthetic fault data generation
- [ ] Comparative study: real-data-only vs 
      synthetic-augmented LSTM accuracy
- [ ] TensorFlow Lite deployment to ESP32-S3
- [ ] SMS alert integration
- [ ] Solar power integration
- [ ] Field deployment (target: Nov 30, 2026)

### Documentation (Jan-Feb 2027)
- [ ] Field data collection (3+ weeks)
- [ ] Research paper finalized
- [ ] KSEF display board prepared
- [ ] KSEF regional submission (Feb 2027)

## Repository Structure
