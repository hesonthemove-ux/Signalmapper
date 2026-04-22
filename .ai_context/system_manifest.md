SignalMapper Pro — System Manifest
Version: 2.1
Status: Engineering Specification (Authoritative)
1. Core Functional Requirements (Invariant)
The following functions are mandatory system capabilities and must remain operational in all builds.
1. Hardware Handshake
The system must continuously verify the availability of:
GNSS receiver

/dev/ttyUSB0
and RTL-SDR device.
Visual indicators must expose hardware status:
Component
Status
GNSS
Green = Locked / Red = No Fix
SDR
Green = Active / Red = Offline
Loss of hardware connectivity must trigger a visible UI warning.
2. Dynamic SS-DAB Site Filtering
The system must dynamically filter SS-DAB transmitter sites using Ofcom coverage polygons supplied by Ofcom.
Filtering rule:

Sites must fall within a +20 mile crow-flight buffer
from the licensed Ofcom coverage polygon.
Example coverage areas include:
Paisley
Greenock
Central Belt multiplex regions
3. Hybrid Signal Search
SignalMapper must support two scan modes:
Standard Mode
Automatic scanning of known DAB multiplex blocks.
Manual Mode
User-entered frequency scan.
Manual mode must display a hardware capability warning if the requested frequency is outside the supported SDR range.
4. Mission Control
The UI must support mission-based initialization.
Mission types:
Business
Used for RF auditing and engineering analysis.
Personal
Used for non-commercial exploration.
UI control toggles must include:
Satellite map layer
Street map layer
Terrain map layer
5. SatNav System
Navigation must support:
Postcode → coordinate resolution
Route guidance including:
lane guidance
turn prompts
motorway optimisation (M8 / M74 corridor)
Voice guidance must be generated using Text-to-Speech.
6. GIS Signal Reporting
Signal coverage visualisation must follow the defined spatial model:
Zone
Meaning
Green
100% Ofcom licensed coverage
Blue
+20% engineering buffer
Grey
+40% overspill / propagation analysis
These zones must remain consistent across:
backend spatial logic
UI overlays
exported reports.
7. AI Modification Rules
AI assistants interacting with this repository must follow these rules.
Allowed actions:
improve documentation
optimise performance
enhance UI readability
add optional analytics
AI must not:
remove any feature listed in this manifest
modify hardware interfaces
alter spatial zone definitions
change GNSS device paths
rewrite the SDR ingest pipeline.
If a requested change conflicts with this manifest, the manifest takes precedence.
8. Code Preservation Rule
Existing working functionality must never be removed.
Enhancements must be:
additive
backward compatible
non-destructive.
If uncertainty exists, the current implementation must be preserved.
9. Authoritative Specification
This manifest is the source of truth for system behaviour.
All contributors — human or AI — must ensure that:
system requirements remain satisfied
RF engineering logic remains intact
Ofcom-derived GIS models remain unchanged.
