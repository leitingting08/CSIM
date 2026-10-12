# Interaction Models — Session 1: Interaction, XR & Embodiment

## 2. What is interaction?

### 2.1 Definitions (Crawford, 2003)

- The reference point is always **person-to-person communication**.
- **Interaction as conversation**: "a cyclic process in which two actors alternately **listen, think and speak**."
- **In HCI**: "a cyclic process in which two actors alternately **receive an input, process it and generate an output**."

### 2.2 Three levels of communication (Rafaeli, 1988; diagram after Bongers, 2000)

U = user, C = computer, M1…M6 = successive messages

| Type            | What each new message takes into account                                                            | Example from the diagram                 |
| --------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **Two-way**     | Nothing earlier: messages simply alternate                                                          | M3 does not refer to M1 or M2            |
| **Reactive**    | Only the **immediately previous** message                                                           | C answers M3 with reference to [M3] only |
| **Interactive** | The **whole history** of the exchange, including how earlier messages referred to even earlier ones | C answers M5 with reference to [M1…M5]   |

- Rafaeli's definition: **interactivity** is the extent to which any third (or later) message relates to the degree to which previous exchanges referred to even earlier messages.
- In short: real interaction has **memory** and builds on accumulated context. Just responding is only reactive.

### 2.3 Milestones in the history of interaction

- **Database systems + GUIs + WIMP** (windows, icons, menus, pointer), with comments by Alan Kay
- **CAD**: Ivan Sutherland's **Sketchpad (1963)**
- **HMD-based VR**: architectural walkthroughs
- **Multi-touch**: Jeff Han
- **Media art**: _Interactive Plant Growing_, Christa Sommerer & Laurent Mignonneau
- **Video games**: Wii Tennis

---

## 3. eXtended Reality (XR)

### 3.1 Reality–virtuality continuum (Milgram et al., 1994)

Real environment → **Augmented Reality (AR)** → **Augmented Virtuality (AV)** → Virtual environment

- **Mixed Reality (MR)**, in Milgram's sense, is everything between the two extremes: "real world and virtual world objects presented together within a single display".

### 3.2 The course's practical definitions

Key question: what can the **system** and the **user** each do with **digital stimuli** and with the **physical world**?

| Type                                                                 |        | Digital stimuli        | Physical world                                                            |
| -------------------------------------------------------------------- | ------ | ---------------------- | ------------------------------------------------------------------------- |
| **Virtual Reality**                                                  | system | Generates and controls | Not considered                                                            |
|                                                                      | user   | Interacts with         | Not considered                                                            |
| **Augmented Virtuality** (physical world laid over digital stimuli)  | system | Generates and controls | **Detects** elements but cannot affect them                               |
|                                                                      | user   | Interacts with         | Can **use it to interact** with the digital stimuli                       |
| **Augmented Reality** (digital stimuli laid over the physical world) | system | Generates and controls | Uses it to **adapt** the digital stimuli, but cannot control or affect it |
|                                                                      | user   | Interacts with         | Can **perceive** it but cannot interact with it                           |
| **Mixed Reality** (both mixed with equal importance)                 | system | Generates and controls | Can **perceive and control** it                                           |
|                                                                      | user   | Interacts with         | Interacts with                                                            |

- ⚠️ **VR is not restricted to HMDs.** A projection-based experience with only digital stimuli is also VR.
- Course stance: in theory there are four categories; in practice the boundaries blur, so the umbrella term is **XR**.

### 3.3 In-class exercise: classify the applications

| Application                                                 | Classification              | Why                                                                                                                |
| ----------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Funky Forest** (Design I/O)                               | Augmented Virtuality        | The system detects children's bodies and physical objects and uses them as input, but cannot change them           |
| **Laparoscopic Simulator** (MedVision)                      | VR / AV (both tables shown) | Purely digital scene, but operated through physical surgical instruments that the system tracks                    |
| **Messa di Voce** (Golan Levin & Zachary Lieberman)         | Virtual Reality             | Projected digital graphics driven by voice; the physical world is not part of the content. Shows that VR ≠ HMD     |
| **AR Magic Lanterns**, Barcino (Roman Barcelona), FuBIntLab | Augmented Reality           | Digital reconstructions adapted to the real ruins; the user cannot interact with the ruins themselves              |
| **Puppet Parade** (Design I/O), for the hand users only     | Virtual Reality             | The hand-operators control digital puppets only                                                                    |
| **Kobito Virtual Brownies** (Tokyo Institute of Technology) | Mixed Reality               | Virtual creatures push a **real** physical tea caddy; the system both perceives and **affects** the physical world |

_The Laparoscopic Simulator slide shows both the VR and the AV table, so the classification was probably left open for discussion. The reasons column is my reading of the slides._

---

## 4. Interaction models and communication

### 4.1 The course's central question

How can we explain to a user the **mediation** of an XR experience? → **Virtual Subjectiveness (VS)** (Parés & Parés, 2001; read for S3).

### 4.2 Communication theory

- **Shannon's model**: source → transmitter → channel (noise) → receiver → destination. It describes **transmission**.
- **Terry Winograd (2006)**: "the success of the communication depends on the real intelligence on the part of the listener". **Interaction is based on communication.**
- **Umberto Eco (1976)**: in semiotics, **communication occurs only when there is interpretation**.
  - **Transfer process**: a signal goes from emitter to receiver with its content unaltered, regardless of meaning.
  - **Communication process**: the signal **demands an interpretative answer** from the receiver.
- **Design implication**: carefully evaluate how users **construct meaning** during the interaction and how they **interpret** the experience afterwards.
- **Winograd on HCI**: "No medium is right for everything."
- **Marshall McLuhan (1967)**: "We look at the present through a rear-view mirror. We march backwards into the future." New media are first understood through the old ones.

---

## 5. Embodied cognition and embodied interaction

### 5.1 Embodied cognition: what it looks at

- How we perceive the world
- How we conceptualise experience
- How we build a model of the world
- How the body "gets in the way" of, that is **mediates**, our understanding of the world

### 5.2 From Cartesian dualism to the lived body

- **Cartesian dualism**: body and mind are separate; consciousness is the source of knowledge.
- **Merleau-Ponty (1940s)** challenges this and reintroduces the body as a **skilled subjectivity** that helps construct knowledge: "**The body is our general medium for having a world.**"
- **Contemporary view**: every individual is a **"lived body"**; the body **mediates** between mind and world.
- Related fields: physiology, phenomenology, ecology of perception, developmental psychology (constructivism, constructionism), embodied metaphors, activity theory, situated cognition.

### 5.3 Key thinkers

| Field                             | Who                       | Core idea                                                                                                                             |
| --------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Philosophy                        | **Merleau-Ponty**         | Every individual is a "lived body"                                                                                                    |
| Psychology                        | **J. J. Gibson**          | The human body affects human understanding                                                                                            |
| Social psychology                 | **Barsalou & Niedenthal** | Experiments show knowledge is **grounded** in bodily states and in the brain's modality-specific systems                              |
| Cognitive science                 | **Barsalou**              | Brain structures link motor areas with cognitive processing                                                                           |
| Neurophysiology                   | **Gallese**               | **Mirror neurons** are involved in perceiving communicative action, imitation, basic mind reading and empathy                         |
| Cognitive linguistics             | **Lakoff & Johnson**      | **Embodied metaphor theory**: abstract concepts rest on **image schemas** derived from physical action                                |
| Developmental psychology          | **Piaget**                | People construct knowledge from **active experience**                                                                                 |
| Developmental psychology          | **Vygotsky**              | Inter-psychological processes (in the physical and social world) are needed to develop intra-psychological ones → **internalisation** |
| Philosophy, biology, neuroscience | **Varela et al.**         | Knowledge about the world cannot be separated from our **standpoint in the world**                                                    |

### 5.4 Gibson: ecological perception and affordances (1979)

- **Ambient optic array**: perceiving is **active exploration** of the environment; perceptual systems evolved in organisms **on the move**.
- **Affordance**: all action possibilities are latent in the environment and objectively measurable, independent of whether the individual recognises them, but always **relative to an agent** and its capabilities.
- Direction of influence: environment → living being. The body shapes understanding.

### 5.5 Dourish (2001): _Where the Action Is_

- **Phenomenology**:
  - Thinking does not happen separately from being and acting.
  - Perception starts with **what is experienced**, not with what is expected.
  - Key concepts: **perception and action**.
- **Embodiment**:
  - Based on how we experience the everyday world: we understand our environment because we have a body that can act on it.
  - It is about the **relationship between action and meaning**.
  - **Embodiment ≠ physical reality.**
  - It has a **participative status**: things are embedded in the world, and their reality depends on that embedding. We are integral parts of the world and society.
- **Embodied interaction**:
  - Interaction is tied to the setting where it happens → a **situated perspective**.
  - No abstract users or settings: **real users in real settings doing real work**.
  - Embodied interaction = **tangible computing + social computing** (physical artifacts and social interaction).

### 5.6 Three areas of embodied cognition

| Relation                      | Aspects                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------- |
| **With one's own body**       | Proprioception, kinaesthesia, gestures                                            |
| **With space** (body ↔ space) | Navigation, point of view, scale and proportion…                                  |
| **Social** (person ↔ person)  | Face-to-face interaction, non-verbal communication, facial expressions, emotions… |

---

## Key terms and references

Crawford (2003) · Rafaeli (1988) · Bongers (2000) · Sutherland, Sketchpad (1963) · Milgram et al. (1994) · Shannon · Winograd (2006) · Eco (1976) · McLuhan (1964, 1967) · Merleau-Ponty · Gibson (1979) · Barsalou · Gallese · Lakoff & Johnson · Piaget · Vygotsky · Varela · Dourish (2001) · Parés & Parés (2001), Virtual Subjectiveness
