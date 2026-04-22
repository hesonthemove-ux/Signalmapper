SignalMapper Pro | Caledonia TX Engineering Manifest
Version: 2.1.0 (AI-Governed Build)
Status: Deployment Ready
1. Mission Profile
Primary Function:
Mobile RF Audit & GIS Gap Analysis for DAB / SS-DAB multiplex networks.
Operating Region:
Scotland — with focus on West Coast and Central Belt RF corridors.
Regulatory Context:
All transmitter data and polygons originate from Ofcom licensed transmitter datasets.
Operational Targeting:
Ofcom-licensed transmitter sites
Official coverage polygons
Overspill engineering zones for RF diagnostics
2. Hardware Specification
Host Node
Lenovo m710q compact compute platform
RF Front-End
RTL-SDR with TCXO stability
Positioning System
USB GNSS receiver
Device Path

/dev/ttyUSB0
Hardware Monitoring
Real-time system checks:
SDR availability
GNSS lock state
hardware heartbeat
Status indicators must expose:
GNSS lock state
SDR operational state
ingest pipeline state
3. Core Functional Logic
Data Ingest
automated retrieval of Ofcom TxParams CSV datasets
scheduled refresh capability
Spatial Filtering
SS-DAB transmitters are filtered using a proximity buffer:

20 mile crow-fly distance
from licensed coverage polygons.
Spatial Zones
Green Zone
100 percent Ofcom licensed coverage polygon
Blue Zone
Engineering buffer (+20 percent)
Grey Zone
Secondary overspill / tropospheric analysis zone (+40 percent)
These zones must remain consistent across UI and backend logic.
4. User Interface & Navigation
Engineering HUD displays:
Bit Error Rate (BER)
Transmitter Identification Information (TII)
GNSS constellation lock
active transmitter multiplex
Navigation System
postcode → coordinate routing
road-aware navigation
motorway lane guidance (M8 / M74 focus)
Audio Interface
text-to-speech navigation prompts
engineering alerts for signal anomalies
Mission Modes
Business Mode
RF audit / regulatory analysis
Personal Mode
non-commercial signal exploration
5. AI Inspection Protocol
AI assistants (including Gemini, Copilot, and ChatGPT) interacting with this repository must follow the inspection protocol below before modifying code.
Mandatory Pre-Read
The following directory must be parsed before any code modification:

.ai_context
Required Understanding
AI systems must understand:
RF ingest pipeline
Ofcom dataset structure
spatial zone definitions
hardware dependencies
If context cannot be determined, no modification should be performed.
6. AI Development Guardrails (Critical)
AI agents modifying this repository must comply with the following rules.
Allowed Actions
AI may:
improve documentation
optimise performance
enhance UI visibility
add optional analytics
extend logging or telemetry
Restricted Actions
AI must NOT:
remove existing functionality
rename core modules
alter RF ingest logic
change spatial zone definitions
modify hardware interface assumptions
Architecture Changes
Any change affecting:
SDR ingest pipeline
GNSS interface
spatial filtering logic
Ofcom data parsing
requires explicit maintainer approval.
7. Code Integrity Rule
All enhancements must be:
Additive
Backward compatible
Non-destructive
Existing system behaviour must remain operational.
If uncertainty exists, AI must:
preserve current implementation
propose enhancements separately.
8. Build Consistency Requirements
All builds must remain compatible with the deployed hardware stack:
Host platform
Lenovo m710q
RF device
RTL-SDR (TCXO)
GNSS interface

/dev/ttyUSB0
Breaking compatibility with this hardware profile is not permitted.
9. Repository Governance
This repository prioritises:
engineering stability
regulatory accuracy
reproducible RF measurements
AI assistants must treat this manifest as the authoritative engineering specification.
