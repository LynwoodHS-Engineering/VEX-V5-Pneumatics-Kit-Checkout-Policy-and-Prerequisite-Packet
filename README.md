# VEX V5 Pneumatics Kit Checkout Policy and Prerequisite Packet

## Purpose

VEX V5 pneumatics kits are shared, limited team resources. This policy ensures that each team has demonstrated safe, purposeful, and technically informed use of pneumatic components before receiving a current VEX V5 pneumatics kit. It is designed to reduce lost parts, prevent avoidable damage, improve design decisions, and keep kits available to all teams.

A team earns access to a V5 pneumatics kit by completing the prerequisite process below with a legacy pneumatics kit, documenting its engineering decisions, and returning the legacy kit complete and organized.

---

## Policy Summary

A team may check out a VEX V5 pneumatics kit only after it has:

1. Completed the pneumatic skills demonstration using a legacy kit.
2. Researched and explained the benefits and tradeoffs of pneumatics compared with motor-driven linear-actuation alternatives.
3. Produced a detailed pneumatic-system concept sketch and a detailed alternative concept sketch.
4. Completed a weighted decision matrix comparing the two concepts.
5. Presented the work for approval.
6. Checked the legacy pneumatics kit back in, complete and organized.

Completion of the written work alone does not guarantee approval. The team must also demonstrate responsible handling, sound engineering reasoning, and a complete legacy-kit return.

---

## Eligibility and Checkout Rules

### Who may request a kit

- A currently active team may submit one V5 pneumatics-kit request at a time.
- The request must identify a designated team equipment lead and at least one additional responsible team member.
- Both students must be present during checkout and check-in unless the coach approves another arrangement.
- A team must have a specific robot mechanism or prototype purpose for the kit. “We want to try pneumatics” is not sufficient without a documented concept.

### Checkout conditions

- The team must submit all required artifacts in the team repository or designated submission location.
- The coach or equipment manager must review and approve the prerequisites before checkout.
- The legacy kit must be returned and inventoried before the V5 kit is issued.
- The receiving team accepts responsibility for the issued inventory from checkout until check-in.
- The kit may not be transferred, loaned, or combined with another team’s kit without explicit approval.
- Components must remain in the labeled kit container when not installed on the robot or actively being tested.

### Use expectations

- Use only approved VEX components, fittings, tubing, and operating procedures.
- Do not modify, drill, cut, glue, permanently mark, or force pneumatic components.
- Cut tubing only as needed, use clean square cuts, and retain reusable tubing lengths.
- Keep fittings, caps, adapters, and small hardware in labeled compartments.
- Depressurize the system before changing tubing, fittings, cylinders, or other pneumatic components.
- Report missing, damaged, leaking, or malfunctioning components immediately. Prompt reporting is expected and will be considered more responsible than concealing a problem.
- Store the kit securely; do not leave it unattended in a competition pit, classroom, vehicle, or shared workspace.

### Check-in conditions

- The team must return the kit by the agreed return date or when requested for program needs.
- The team must return every issued component clean, dry, depressurized, and organized in its assigned location.
- The team must participate in a check-in inventory with the coach or equipment manager.
- Missing or damaged items must be documented before the checkout record is closed.

---

## Required Prerequisites

All prerequisites must be completed using a legacy pneumatics kit before a V5 pneumatics kit is issued.

### 1. Pneumatic skills demonstration

The team must build and program a controlled pneumatic mechanism using:

- A legacy pneumatic cylinder.
- The legacy pneumatic control hardware needed to extend and retract the cylinder.
- The VEX V5 Brain.
- At least one sensor selected by the team.

The program must use sensor input to control cylinder behavior. The cylinder may not simply run on a timed loop with no sensor-based decision.

#### Minimum demonstration requirements

The demonstration must show all of the following:

- The program initializes the motor/sensor ports and pneumatic output correctly.
- The sensor produces a readable input that the program uses in a decision.
- The cylinder extends only when a clearly defined sensor condition is met.
- The cylinder retracts when the condition is no longer met, when a second condition is met, or through another clearly documented safe state.
- The mechanism avoids rapid uncontrolled cycling.
- The team can explain the program logic and identify the sensor condition that causes each pneumatic state.
- The team can safely depressurize and disconnect the system after testing.

#### Acceptable sensor examples

Teams may select any appropriate VEX-compatible sensor, including:

- Bumper switch or limit switch.
- Distance Sensor.
- Optical Sensor.
- Rotation Sensor.
- Inertial Sensor.
- Controller button input, if the team also explains why a manual command is the appropriate sensor/input for its intended mechanism.

#### Required code submission

Submit:

- The complete source code.
- A short README that identifies the selected sensor, ports, sensor threshold or trigger condition, and expected cylinder behavior.
- A brief video, live demonstration, or coach-observed test showing the mechanism operating.

#### Example behavior specification

This is an example only; teams may design a different valid control scheme.

> When the Distance Sensor detects an object within 100 mm, the cylinder extends. When the object is farther than 130 mm, the cylinder retracts. The separate extend/retract thresholds create hysteresis so small sensor fluctuations do not cause rapid cycling.

The team should explain why its logic is safe and how it prevents undesirable repeated actuation.

---

### 2. Research: pneumatics versus motor-driven linear actuation

The team must research why a pneumatic mechanism might be chosen instead of a motor-driven linear actuator or motor-powered linkage, and when the motor-driven alternative would be better.

The research must be written in the team’s own words and include sources. A recommended length is 1–2 pages or the equivalent in a well-organized engineering notebook entry.

#### Required research topics

Address each topic below:

| Topic | Questions to answer |
|---|---|
| Force and speed | What kind of motion can pneumatics provide? How do force, speed, stroke length, and pressure affect the design? How does this compare with a motor-driven mechanism? |
| Control and positioning | Is the mechanism primarily two-position, or does it need accurate intermediate positioning? What control advantages or limitations do pneumatics and motor-driven mechanisms have? |
| Weight and packaging | How much robot space and mass are required for cylinders, tubing, valves, tank(s), compressor, motors, gears, linkages, and structural supports? |
| Power and energy | What energy source does each system use? How does available air capacity or electrical power affect repeated use during a match? |
| Complexity and reliability | What can leak, bind, stall, overheat, loosen, or fail? What maintenance and troubleshooting does each option require? |
| Rules and safety | What competition rules, legal-component requirements, operating limits, and safety practices affect the design? |
| Match strategy | Does the mechanism need a fast action, a holding force, repeatable positioning, variable speed, frequent cycling, or a long travel distance? |

#### Required conclusion

End the research with a claim that directly answers:

> For our proposed mechanism, should we use pneumatics or the motor-driven alternative, and why?

The conclusion must cite evidence from the research and connect to the team’s own concepts and decision matrix.

---

### 3. Detailed concept sketches

The team must produce two detailed concept sketches for the same robot task:

1. A concept that uses the pneumatic system.
2. An alternative concept that uses a motor-driven linear actuator, motor-driven linkage, or other non-pneumatic motorized method.

The concepts must solve the same functional problem. For example, if the pneumatic concept deploys an intake, the alternative must also deploy an intake; it should not solve a different robot task.

#### Required labels on each sketch

Each sketch must include:

- Mechanism name and intended robot function.
- Direction of movement, travel path, and approximate range of motion.
- Major structural members and pivot points.
- Expected game-object contact point(s), if applicable.
- Approximate mounting location on the robot.
- Major components and hardware.
- Potential interference or packaging concerns.
- Notes describing the sequence of operation.

#### Additional requirements for the pneumatic concept

Clearly label:

- Cylinder location, mounting points, and rod-end connection.
- Valve/solenoid location.
- Tubing routing.
- Air tank/compressor or air source location, as applicable.
- Extend and retract directions.
- End-of-stroke or mechanical-stop considerations.
- Service access for fittings, tubing, and maintenance.

#### Additional requirements for the motor-driven alternative

Clearly label:

- Motor location and proposed gear ratio, linkage, winch, rack-and-pinion, lead-screw, or other actuation method.
- Motion-transmission path from the motor to the output.
- Expected limits, mechanical stops, or sensor feedback points.
- Likely load path and areas where the mechanism could stall, flex, or bind.

Hand sketches are acceptable if they are neat, legible, photographed/scanned clearly, and sufficiently detailed. CAD screenshots or annotated digital sketches are encouraged.

---

### 4. Weighted decision matrix

The team must prepare a weighted decision matrix comparing the pneumatic and motor-driven concepts. The matrix must include both concept sketches or direct links/embedded images of them.

The matrix should use criteria relevant to the team’s mechanism rather than generic criteria only. The team must explain its weights and scores.

#### Scoring method

Use this scale unless the coach approves another one:

- 1 = Poor fit for the design goal.
- 2 = Below average fit.
- 3 = Acceptable fit.
- 4 = Strong fit.
- 5 = Excellent fit.

For each criterion:

\[
\text{Weighted score} = \text{Weight} \times \text{Rating}
\]

For each concept:

\[
\text{Total score} = \sum \text{Weighted scores}
\]

Weights must total 100 percent.

#### Required decision criteria

Include at least the following criteria, adding others as appropriate:

- Ability to meet the required robot function.
- Speed or response time.
- Force capacity under expected load.
- Control and repeatability.
- Weight and packaging.
- Reliability and failure risk.
- Ease of construction, adjustment, and repair.
- Rules compliance and safety.
- Resource cost and impact on other robot systems.

#### Decision matrix template

| Criterion | Weight (%) | Pneumatic rating (1–5) | Pneumatic weighted score | Motor-driven rating (1–5) | Motor-driven weighted score | Evidence/justification |
|---|---:|---:|---:|---:|---:|---|
| Required function |  |  |  |  |  |  |
| Speed/response time |  |  |  |  |  |  |
| Force capacity |  |  |  |  |  |  |
| Control/repeatability |  |  |  |  |  |  |
| Weight/packaging |  |  |  |  |  |  |
| Reliability/failure risk |  |  |  |  |  |  |
| Build/repair difficulty |  |  |  |  |  |  |
| Rules/safety |  |  |  |  |  |  |
| Resource cost/system impact |  |  |  |  |  |  |
| Additional team-specific criterion |  |  |  |  |  |  |
| **Total** | **100** |  |  |  |  |  |

#### Required decision statement

Below the matrix, include a short engineering decision statement that:

- Identifies which concept scored higher.
- Explains whether the team will follow the matrix result or intentionally choose the lower-scoring option.
- Identifies the strongest evidence behind the decision.
- Names at least one risk or uncertainty that still needs prototyping or testing.

A high score does not automatically mean the pneumatic option is appropriate. The team must show that it understands the operational, reliability, and resource consequences of using pneumatics.

---

## Submission Package

Before requesting V5 kit checkout, submit one organized package containing:

- Team name, team number, date, and names of responsible equipment leads.
- Pneumatic skills demonstration code and README.
- Demonstration video link or request for a live demonstration.
- Pneumatics-versus-motor-actuation research with sources.
- Detailed pneumatic concept sketch.
- Detailed motor-driven alternative concept sketch.
- Completed weighted decision matrix with sketches embedded or linked.
- Final engineering decision statement.
- Proposed V5 kit checkout date and expected return date.

Suggested repository organization:

```text
pneumatics-qualification/
├── README.md
├── code/
│   └── pneumatic_sensor_control.cpp
├── demonstration/
│   └── demo-video-link.txt
├── research/
│   └── pneumatics-vs-motor-actuation.md
├── concepts/
│   ├── pneumatic-concept-sketch.pdf
│   └── motor-driven-alternative-sketch.pdf
├── decision/
│   └── weighted-decision-matrix.xlsx
└── inventory/
    └── legacy-kit-return-checklist.md
```

A physical engineering notebook may be used instead if it contains the same content in an organized, reviewable format.

---

## Review and Approval Process

1. The team submits the complete prerequisite package.
2. The coach or equipment manager checks the package for completeness.
3. The team completes a live pneumatic skills demonstration or submits an approved video demonstration.
4. The reviewer may ask the team questions about its code, sensor logic, safety procedures, research, sketches, and decision matrix.
5. The team checks the legacy kit back in and completes the legacy-kit inventory.
6. If the legacy kit is complete and the team meets the standard, the reviewer approves V5 kit checkout.
7. The team signs the V5 kit checkout record and receives the assigned kit.

Teams should plan for review time. A kit may not be issued immediately before a meeting, event, or competition simply because a team delayed the prerequisite process.

---

## Approval Rubric

| Category | Meets standard | Revision required when… |
|---|---|---|
| Controlled pneumatic demonstration | Sensor input clearly controls safe, intentional cylinder motion; team can explain the code and system | The cylinder is only timed, the sensor is unused or unreliable, code is unexplained, or operation is unsafe/uncontrolled |
| Research quality | Explains meaningful advantages, limitations, and tradeoffs with sources and a mechanism-specific conclusion | Writing is generic, lacks sources, omits tradeoffs, or does not connect to the team’s mechanism |
| Pneumatic concept sketch | Clearly communicates a buildable pneumatic design, component locations, motion, and integration concerns | Major pneumatic parts, motion details, mounting, routing, or packaging are missing |
| Motor-driven alternative sketch | Shows a credible non-pneumatic way to perform the same function | The alternative performs a different task or lacks sufficient detail to compare |
| Decision matrix | Has justified weights, ratings, calculations, and evidence connected to the sketches/research | Weights do not total 100 percent, scores are unsupported, calculations are incomplete, or the decision is unexplained |
| Legacy-kit return | Kit is complete, clean, organized, depressurized, and inventoried | Parts are missing, damaged, mixed with other equipment, or not returned |
| Team responsibility | Team communicates promptly and follows checkout procedures | Team has unresolved equipment issues, misses return commitments, or transfers equipment without permission |

---

## Checkout Record

### Team information

| Field | Entry |
|---|---|
| Team name / number |  |
| Responsible equipment lead |  |
| Additional responsible member |  |
| Coach/equipment manager |  |
| Intended mechanism |  |
| Submission/repository link |  |
| Requested checkout date |  |
| Expected return date |  |

### Prerequisite verification

| Requirement | Complete | Reviewer initials/date |
|---|---|---|
| Sensor-controlled legacy pneumatic demonstration completed | Yes / No |  |
| Source code and README reviewed | Yes / No |  |
| Research document reviewed | Yes / No |  |
| Pneumatic concept sketch reviewed | Yes / No |  |
| Motor-driven alternative concept sketch reviewed | Yes / No |  |
| Weighted decision matrix reviewed | Yes / No |  |
| Final engineering decision statement reviewed | Yes / No |  |
| Legacy kit returned, inventoried, and organized | Yes / No |  |
| V5 kit checkout approved | Yes / No |  |

### V5 kit issue inventory

Record the contents of the assigned kit below or attach the official kit inventory sheet.

| Item | Quantity issued | Quantity returned | Condition/notes |
|---|---:|---:|---|
| Assigned V5 pneumatics kit container |  |  |  |
| Pneumatic cylinders |  |  |  |
| Solenoids/valves |  |  |  |
| Tubing |  |  |  |
| Fittings/adapters |  |  |  |
| Tank(s)/air-storage components |  |  |  |
| Compressor/air-source components, if included |  |  |  |
| Electronics/cables, if included |  |  |  |
| Other |  |  |  |

### Acknowledgment

We understand that this is shared team equipment. We will use it responsibly, keep it organized, report issues promptly, return it on time, and complete the check-in inventory.

| Role | Name | Signature | Date |
|---|---|---|---|
| Equipment lead |  |  |  |
| Additional responsible member |  |  |  |
| Coach/equipment manager |  |  |  |

---

## Legacy Kit Return Checklist

Before requesting V5 checkout, the team confirms that the legacy kit has been returned in the following condition:

- All cylinders, valves, fittings, tubing, and accessories are present or any issue has been reported.
- The pneumatic system is depressurized.
- Tubing is removed from temporary prototypes unless otherwise approved.
- Reusable tubing is coiled neatly; unusable scraps are disposed of as directed.
- Small fittings and adapters are returned to labeled compartments.
- Components are clean and free of tape, labels, debris, or unapproved modification.
- The kit container is closed and returned to its assigned storage location.
- The coach or equipment manager has completed the inventory check.

---

## Consequences for Noncompliance

The purpose of this policy is accountability and resource stewardship, not punishment. However, a team that does not follow checkout expectations may lose or delay access to pneumatic equipment.

Possible consequences include:

- Checkout delayed until missing prerequisites or inventory issues are resolved.
- Temporary suspension of V5 pneumatics checkout privileges.
- Requirement to complete an additional inventory, cleanup, repair, or training task.
- Priority given to teams that have met return dates and maintained equipment responsibly.

The coach or equipment manager will consider circumstances, communication, and the team’s history when determining next steps.

---

## Team Design Reminder

Pneumatics are a design choice, not an automatic upgrade. A successful team selects them when their fast, simple extend/retract action and packaging advantages fit the robot task better than a motor-driven alternative. A motor-driven system may be the better choice when the mechanism needs precise positioning, variable motion profiles, long travel, continuous control, or reduced dependency on pneumatic resources.

The goal of this qualification process is for teams to make that choice intentionally, document it clearly, and care for the shared equipment that makes experimentation possible.
