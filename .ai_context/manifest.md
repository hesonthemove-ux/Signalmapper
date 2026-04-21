# SignalMapper Pro | Caledonia TX Engineering Manifest
## Version: 2.0.4 (Spatial Ingest Build)
## Status: Deployment Ready

### 1. MISSION PROFILE
- **Primary Function:** Mobile RF Audit & GIS Gap Analysis for DAB/SS-DAB Multiplexes.
- **Region:** Scotland (West Coast / Central Belt focus).
- **Targeting:** Official Ofcom-licensed transmitter sites and polygons.

### 2. HARDWARE SPECIFICATION
- **Host:** Lenovo m710q (Compact Node).
- **RF Engine:** RTL-SDR (High-stability TCXO).
- **Positioning:** USB GNSS Receiver (/dev/ttyUSB0).
- **Status Monitoring:** Real-time hardware handshake (GNSS & SDR Status LEDs).

### 3. CORE FUNCTIONAL LOGIC
- **Data Ingest:** Automated fetch of Ofcom TxParams CSV.
- **Smart Proximity Filter:** SS-DAB sites filtered based on +20 mile crow-fly buffer from polygon boundaries.
- **Spatial Zones:** - **Green (100%):** Official Ofcom Licensed Polygon.
  - **Blue (+20%):** Engineering Buffer / Primary Overspill.
  - **Grey (+40%):** Secondary Overspill / Tropospheric Analysis Zone.

### 4. USER INTERFACE & NAVIGATION
- **HUD:** Live Bit Error Rate (BER), Transmitter Identification Info (TII), and Satellite Constellation Lock.
- **SatNav:** Postcode-to-Coordinate routing with multi-lane guidance for M8/M74 and TTS directions.
- **Mission Setup:** Purpose-driven initialization (Business Audit vs. Personal).

### 5. AI INSPECTION PROTOCOL
- **Context Injection:** This directory (.ai_context) must be read before any code modification.
- **Build Consistency:** All updates must respect the hardware constraints and Ofcom-driven GIS layers.
