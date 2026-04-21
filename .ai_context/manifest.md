# SignalMapper Pro | Caledonia TX Engineering Manifest
## Version: 2.0.4 (Spatial Ingest Build)
## Date: 2026-04-21

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
- **Hybrid Tuning:** Manual frequency entry (MHz) with software-enforced hardware resonance warnings.

### 4. USER INTERFACE & NAVIGATION
- **Views:** Toggle between Satellite, Street, and Topographic (Terrain) overviews.
- **HUD:** Live Bit Error Rate (BER), Transmitter Identification Info (TII), and Satellite Constellation Lock Status.
- **SatNav:** - Postcode-to-Coordinate routing.
  - Multi-lane guidance for complex interchanges (e.g., M8/M74).
  - TTS (Text-to-Speech) spoken directions.
- **Mission Setup:** Purpose-driven initialization (Business Audit vs. Personal).

### 5. AI INSPECTION PROTOCOL
- **Context Injection:** This directory (.ai_context) must be read before any code modification.
- **Build Consistency:** All updates must respect the hardware constraints and Ofcom-driven GIS layers.
