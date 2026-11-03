# Sensory Substitution & Augmentation

## 0. The framework

### 0.1 Two ways to remap the senses

|         | **Sensory substitution**                                                                   | **Sensory augmentation**                                                |
| ------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| What    | Carries the information of a **lost or impaired** sense through an **intact** one          | **Adds** information humans don't sense, or **extends** a working sense |
| Example | **BrainPort**: a blind person perceives camera images as electrical patterns on the tongue | **feelSpace** belt: always vibrates on the side facing magnetic north   |
| Goal    | **Restore** access to information                                                          | A **new or wider** sense                                                |

- **The same device can play both roles.** Colour → sound substitutes colour vision for colour-blind users, and adds a sound layer to images for everyone else.
- References: Shull & Damian (2015); Eagleman & Perrotta (2023); Bach-y-Rita & Kercel (2003).

### 0.2 Sources and targets

| Sense                 | What it carries                                   |
| --------------------- | ------------------------------------------------- |
| Vision                | Shape, colour, motion, distance                   |
| Hearing               | Pitch, loudness, direction, speech                |
| Touch                 | Pressure, vibration (≈ 5–400 Hz), temperature     |
| Proprioception        | Joint angles, muscle force                        |
| Vestibular            | Head rotation, acceleration, gravity              |
| Smell                 | Airborne chemicals                                |
| Taste                 | Sweet, salty, sour, bitter, umami                 |
| **Non-human signals** | Magnetic field, infrared, distance (sonar, LiDAR) |

### 0.3 Every mapping is the same loop

**Sensor → feature extraction → encoding (the mapping) → actuator → perception**, and **movement** (pointing, turning the head, walking) changes what the sensor measures. The loop is closed through action.

- Example, **the vOICe** (vision → hearing):
  - head-worn camera → grey levels of each image column
  - encoding: **x → time, y → pitch, brightness → loudness**
  - headphones play one "soundscape" per second
- **The two design decisions**: **features** (what to keep) and **encoding** (which stimulus parameter carries each feature).

### 0.4 Three kinds of mapping

| Type            | Principle                                                                                                                           | Examples                                   |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **Topographic** | **Place → place**: a pixel drives the actuator at the same position; a direction in the world is felt at that direction on the body | TVSS, BrainPort, feelSpace belt            |
| **Parametric**  | **Feature → parameter**: height → pitch, brightness → loudness, tilt → vibration strength                                           | vOICe, balance belt, movement sonification |
| **Symbolic**    | **Recognise → code**: phoneme → tactile pattern; sound → caption or icon                                                            | Phonemic sleeve, sound-awareness glasses   |

- **Rule of thumb: the richer the source and the poorer the target channel, the more processing is needed before mapping.**

### 0.5 What each target sense can carry

| Target         | Coding dimensions                                                     | Main limits                                      |
| -------------- | --------------------------------------------------------------------- | ------------------------------------------------ |
| **Touch**      | Place on the body, frequency (≈ 40–400 Hz), amplitude, rhythm, sweeps | Tactors need cm spacing; adaptation              |
| **Hearing**    | Pitch, loudness, timbre, 3D position, rhythm, speech                  | **Masks real sounds**; fatigue                   |
| **Vision**     | Position, size, colour, motion, text, symbols                         | Occupies the eyes; clutter                       |
| **Vestibular** | Timing and direction of a tilt or motion cue                          | Low rate; galvanic stimulation can be unpleasant |
| **Smell**      | Which odour or pattern, intensity, onset                              | Seconds-slow; lingers; adapts                    |
| **Taste**      | Electric current, frequency, polarity; temperature                    | Mostly sour, salty, bitter; sweet is weak        |

### 0.6 The combination matrix (source → target)

| Source ↓ / Target → | Vision              | Hearing                 | Touch                    | Vestibular     | Taste           |
| ------------------- | ------------------- | ----------------------- | ------------------------ | -------------- | --------------- |
| **Vision**          | prisms              | vOICe, EyeMusic         | TVSS, BrainPort, EyeCane | VR → vibration | AR flavour      |
| **Hearing**         | sound HMD, captions | frequency lowering      | phonemic sleeve, VEST    | —              | sonic seasoning |
| **Touch**           | force display       | Sensor Glove            | relocated feedback       | —              | —               |
| **Proprioception**  | visual feedback     | sonification            | TIKL suit                | —              | —               |
| **Vestibular**      | RGS                 | RGS                     | tilt belt, tongue        | implant        | —               |
| **Smell**           | —                   | —                       | e-nose → trigeminal      | —              | —               |
| **Non-human**       | IR cameras          | hearSpace, colour sound | feelSpace, Haptic Radar  | —              | electric taste  |

- The slide colours each cell as substitution, augmentation or same-sense; "—" means no published work.
- The **Smell target column** is empty for every source, so it is omitted here.
- **Taste as a source** has nothing anywhere.

---

## Part A · Sensory substitution

### A1. Vision → Touch (mostly topographic)

| Year     | Device                 | Key point                                                                                          |
| -------- | ---------------------- | -------------------------------------------------------------------------------------------------- |
| **1966** | **Optacon**            | A hand-held camera scans print; pins under a fingertip of the other hand reproduce each letter     |
| **1969** | **TVSS** (Bach-y-Rita) | **400 vibrators on the back**; blind participants learned to recognise objects                     |
| **1998** | Tongue display         | A 49-point electrotactile array allowed shape recognition; **BrainPort** later uses **400 points** |
| **2014** | **EyeCane**            | One distance reading → vibration; obstacle avoidance after **minutes** of training                 |

- BrainPort mapping: glasses camera → image reduced to the electrode grid → each pixel drives the electrode at the same place on the tongue → **brightness → stimulation strength**.
- Recent devices: _Seeing with the Hands_ (CHI 2025, Pedro Lopes's lab, University of Chicago); Biped NOA mobility harness; WeWalk Smart Cane 2 (detects above-ground obstacles, navigation, vibration and audio); a touch tablet (Field of Vision).
- **"Where is it? Two vibrators are enough"** (Wald et al., CHI 2025)
  - One vibrator per hand, or near each ear. Closer to the target → stronger vibration, like the **loudness difference between our ears**.
  - With just **2 vibrators** (low cost, low computing power), targets **< 30° apart** could be told apart **without training**.
  - New idea: the **hands as "moving ears"** to search for objects.

### A2. Vision → Hearing (parametric)

- Encoding: **y → pitch** (higher = higher frequency), **brightness → loudness**, **x → time** (a scan of ≈ 1 s).
- Devices:
  - **vOICe**: head camera, column scan
  - **PSVA**: pixel grid → frequencies
  - **EyeMusic** (2014): **colour → instrument**
- After training with the vOICe, users could locate and recognise objects (Auvray et al., 2007).
- **EyeMusic**: brain areas related to visual processing in the blind are recruited for "reading". This is evidence of **cross-modal plasticity**.
- ⚠️ **Navigation: app vs plain white cane**. With 7 blind users and 10 h of training, the camera-to-sound app **did not beat** an ordinary cane at avoiding obstacles. **The cane is the baseline any new device must beat.**

### A3. Hearing → Touch

| Strategy              | How                                                                                     | Result                                                                                                              |
| --------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Spectral (place)**  | Filter bank: each frequency band → one tactor; a "**tactile cochlea**" (VEST)           | —                                                                                                                   |
| **Phonemic (symbol)** | Speech → phonemes → each phoneme gets its own pattern of place, frequency and amplitude | **86%** phoneme recognition with 24 forearm tactors coding 39 phonemes, after 1–4 h of training (Reed et al., 2019) |
| **Envelope**          | Speech amplitude envelope → wrist vibration, played alongside a cochlear implant        | **+8.3 points** words recognised in noise by cochlear-implant users (Fletcher et al., 2019)                         |

- **Neosensory Buzz**:
  - Microphones → sound split into **4 frequency bands** → 4 motors (low sounds on one side of the wrist, high on the other); louder → stronger.
  - It grew out of **VEST** (2015: 32 motors on the torso; Eagleman's TED talk); Buzz followed around 2020 with 4 motors on the wrist (cheaper, worn all day).
  - Modes: everyday sounds, music, sleep (alarms).
  - Deaf users learned to identify everyday sounds (Perrotta et al., 2021). It had an **open API**: any data → 4 motors, also used for new senses.
  - ⚠️ **Neosensory shut down in 2025** and sold its technology; users lost the app and support. **Design lesson: plan for the company disappearing** (open formats, offline use).
- **Vibration vests**:
  - Mapping: frequency bands → places on the torso; **beat and rhythm come through well, melody and pitch poorly**.
  - Examples: Not Impossible's vibrotactile suits at concerts; Woojer and SUBPAC (music, games); haptic vests for VR.
  - Pros: large skin area; eyes, ears and hands stay free; a shared concert experience.
  - Cons: bulky, warm, needs charging; low spatial resolution; pitch and timbre are lost.

### A4. Cochlear implants: electric hearing

- A processor behind the ear splits sound into frequency bands → a radio link through the skin → **12–22 electrodes** in the cochlea stimulate the hearing nerve.
- **Place mapping, like the ear**: high frequencies at the base, low at the apex.
- **> 1 million** implants worldwide (NIDCD, 2022).
- Good for speech in quiet; hard in noise and with music (few channels, poor pitch).
- Training helps (+27 points melody recognition, 6 users), and so does touch (+8.3 points words in noise with wrist vibration).

### A5. Hearing → Vision

- Microphone array → **direction of arrival**; classifier → **sound type** (speech, alarm, door); speech recognition → **captions**.
- A head-mounted display shows a direction arrow, the sound's name and a caption (e.g. "doorbell, left"; "Can you pass the salt?").
- 2003: a peripheral sound display on a screen helped deaf users notice office sounds (Ho-Ching et al.).
- 2015: head-mounted direction visualisations evaluated with 24 deaf and hard-of-hearing users (Jain et al.).

### A6. Balance → Touch, Hearing or Vision

**Pipeline**: IMU on the head or trunk → tilt angle → **dead zone** (ignore small sway) → mapping

| Target      | Mapping                                                                                                                         | Evidence                                                                     |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Touch**   | The tactor on the side of the lean vibrates; larger tilt → higher row or faster pulses. Tongue: tilt moves a pattern off-centre | Reduced sway with vestibular loss (Wall 2001; Sienko 2008; Tyler 2003)       |
| **Hearing** | Forward–back sway → pitch; left–right sway → stereo balance                                                                     | Less sway on foam with eyes closed in bilateral vestibular loss (Dozza 2005) |
| **Vision**  | Centre of pressure → a dot on the screen; keep the dot inside a target                                                          | Common in balance training of older adults (Zijlstra 2010)                   |

- **Bilateral vestibular loss**
  - Symptoms: unsteady, worse in the dark or on soft ground; **oscillopsia** (the world jumps when walking); falls and fear of falling.
  - Causes: ototoxic antibiotics (gentamicin), Ménière's disease, meningitis, unknown.
  - **Interventions, from least to most invasive**:
    1. rehabilitation exercises (rely more on vision and proprioception)
    2. substitution (tilt → vibration, tongue or sound)
    3. noisy stimulation
    4. vestibular implant
- **Cheryl Schiltz (2003–2004)**
  - She lost vestibular function after gentamicin and felt she was always falling. An accelerometer on her head drove a pattern on her tongue that moved off-centre when she tilted; she leaned to re-centre it.
  - With the device she could stand and walk steadily.
  - **Residual effect**: after repeated sessions, the benefit outlasted each session (minutes → hours → half a day) (Tyler 2003; Danilov 2007).
  - ⚠️ Caution: small, mostly uncontrolled studies; the device and the exercises done with it can't be separated.
- **Design question**: a device helps while it is worn. Does the brain keep some of the benefit when it is removed?
- **Wearable balance aids**

| Device        | Design                                                        | Result                                                                                  |
| ------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| BalanceBelt   | Waist belt; vibrates on the side the body tilts toward        | 23 of 31 home users improved: score 4.2 → 7.9 / 10 after 1 month (**no control group**) |
| Vertiguard    | Head-worn sensor; vibrators around the trunk during exercises | 15 min/day for 2 weeks; tested against a **sham device** (multicentre)                  |
| Phone trainer | Phone IMU on the trunk + vibrators; exercises at home         | Older adults; randomised pilot with vs without vibration (12 people)                    |

- **Buildable in class**: Grove IMU → tilt → dead zone → vibration motor on the side of the lean.
- **Beyond substitution**
  - **Noisy galvanic stimulation**: electrodes behind the ears deliver a weak random current that isn't felt. **Stochastic resonance**: noise makes weak remaining signals detectable. Less sway standing (2014), steadier walking (2016); **12 of 19 patients** responded, with **31% less sway** on average (Wuehr et al., 2023).
  - **Vestibular implant**: head motion sensors → electrodes on the semicircular-canal nerves. In 8 patients, better posture, gait and quality of life (Chow et al., 2021). Risk: hearing loss in the implanted ear (large in 3 of 8). Geneva–Maastricht prototype: a cochlear array plus three vestibular electrodes.

### A7. Touch and force → Hearing, Vision, Touch

| Mapping            | Example                                                                  | Result                                                  |
| ------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------- |
| → Hearing          | **Sensor Glove**: fingertip microphones → stereo sound in headphones     | Better tactile recognition 12 months after nerve repair |
| → Vision / hearing | Surgery: instrument-tip force → tone pitch or a coloured bar             | Compared during robotic knot tying                      |
| → Touch elsewhere  | Prostheses: fingertip force → vibration or pressure on the residual limb | Better grip control and sense of ownership              |

- **Modality-matched** is better: pressure → pressure feels natural; pressure → vibration is easier to build.

### A8. Smell → Touch (Stanley et al., 2025, _Science Advances_)

- Electronic nose (gas sensor array) → odour code → electrode clip on the **nasal septum** → **trigeminal nerve**, felt as a touch-like sensation.
- Tested with 13 people with normal smell and 52 with smell loss.
  - **Detection worked**: users noticed when an odour was present.
  - **Discrimination was harder**, though most could tell two odours apart.
- It **substitutes but does not restore**: users feel a code for the odour; they don't smell it.

### A9. Gaps and same-sense remapping

- **Little or no research**:
  - taste as a source
  - smell → hearing or vision
  - any sense → taste or smell, as substitution
  - Why: these senses are slow (seconds), adapt fast, and carry very little information.
- In practice, for people without smell: a **symbolic mapping**, such as gas and smoke detectors that sound an alarm or notify the phone.
- **Same-sense remapping**:
  - **Vision**: prisms move part of the image into the remaining visual field (Peli, 2001).
  - **Hearing**: frequency lowering moves high sounds (e.g. "s") into the range still heard.
  - **Touch**: prosthetic feedback relocated to intact skin.

---

## Part B · Sensory augmentation

### B1. Magnetic north → Touch or Hearing

- **feelSpace research belt** (Nagel et al., 2005; Kaspar et al., 2014): the vibrator facing north buzzes. After **weeks of wear**, users reported a **changed sense of space**.
- **naviBelt**: the commercial version, with 16 vibration units; compass and navigation for blind users.
- **hearSpace** (Schumann & O'Regan, 2017): headphones play a sound that always seems to come from the north. Turn right and it moves to your left ear, like a distant church bell.

### B2. Distance and infrared → Touch

- **Haptic Radar (2006)**: range sensors around the head, each driving the vibrator under it (closer → stronger). An "**extended skin**" that feels before contact. **87%** of participants moved to avoid an unseen approaching object.
- **Infrared → touch cortex (2013)**: in rats, infrared detectors drove microstimulation of **S1**. They learned to find infrared light, and whisker touch still worked. Invasive (implanted electrodes).
- Without implants: a **thermal camera** shows infrared as colour (vision → vision).

### B3. Colour → Sound

- Colour under the finger (tablet) → sound: **hue → timbre or pitch; lightness → pitch; saturation → loudness**.
- Coding along **shared cross-modal correspondences** gives better colour memory and object recognition than an arbitrary code (Hamilton-Fletcher et al., 2016).

| Visual feature    | Sound feature        |
| ----------------- | -------------------- |
| Higher in space   | Higher pitch         |
| Brighter, lighter | Higher pitch, louder |
| Larger            | Lower pitch          |
| Sharper shapes    | Brighter timbre      |

- **Neil Harbisson** hears colours through a head-mounted camera antenna.
- **Design rule: follow shared correspondences, and users learn the mapping faster** (Spence, 2011).

### B4. Movement → Touch or Sound

- **TIKL motion-learning suit** (Lieberman & Breazeal, 2007):
  - measures joint-angle error against a teacher's movement
  - the vibrator on the side to move toward fires, with intensity ∝ error
  - rotation → a sweep of vibrators around the limb
  - faster learning than visual instruction alone

| Movement quantity          | Sound parameter   |
| -------------------------- | ----------------- |
| Position                   | Pitch             |
| Velocity                   | Loudness or pitch |
| Left–right location        | Stereo panning    |
| Rhythm of steps or strokes | Tempo, beats      |

- Uses: rowing, cycling, gait and arm rehabilitation. **Fade the sound out so users don't come to depend on it.**

### B5. Taste, flavour and VR motion

- **Vision + smell → taste**: the AR look and smell of another cookie change the perceived taste of a plain one (Narumi et al., 2011).
- **Hearing → taste**: boosting the high frequencies of biting sounds made crisps seem **crisper and fresher** (Zampini & Spence, 2004; "sonic seasoning").
- **Digital → taste**: current, frequency and polarity on the tongue give sour, salty, bitter; sweet is weak (Ranasinghe & Do, 2016).
- **Vision → vestibular**: vibration behind the ear during virtual turns reduced **VR sickness** (Weech et al., 2018).

---

## Part C · Rehabilitation with interfaces

### C1. Why interfaces help

Loop: sensor (camera, IMU, force plate) → movement features → game or VR → feedback → patient moves

| Benefit                 | Explanation                                                                                    |
| ----------------------- | ---------------------------------------------------------------------------------------------- |
| **Repetition**          | Hundreds of movements per session instead of about **32** in conventional sessions (Lang 2009) |
| **Motivation**          | Games give goals, scores and progress; patients train longer                                   |
| **Adaptive difficulty** | Sensors measure performance; the task gets harder as the patient improves                      |
| **Changed perception**  | VR and mirrors show the affected limb moving better, countering **learned non-use**            |
| **Measurement**         | Every movement is recorded; progress becomes visible                                           |
| **Home / tele-rehab**   | Cheap sensors let training continue after the hospital                                         |

- **Key idea: the interface is a sensory mapping designed to make the brain relearn.**

### C2. Rehabilitation Gaming System (RGS)

- A Kinect tracks both arms; virtual arms are seen in **first person**; games: reach, intercept, grasp; **difficulty adapts online**.
- Acute stroke pilot RCT (8 + 8 patients, 12 weeks): faster arm recovery and better Fugl-Meyer and Chedoke scores with RGS.
- From lab to clinic: **Eodyne Systems** (UPF spin-off, 2014); hospital and home versions (RGS@home).
- **RGS as a sensory mapping**:
  - **Core**: arm and finger movement (**proprioception**) → camera + data gloves → virtual arms (**vision**). Targets and scores live in the virtual scene.
  - Hearing for task cues (spoken instructions), which is not a mapping of the movement itself.
  - Extensions: haptic force feedback (other VR systems), sonification of arm position.
  - **Multimodal stimulation**: RGS aims to activate intact neural systems (seeing one's own actions) that drive the motor areas affected by the lesion (Cameirão et al., 2009).
- **Amplified movement**:
  - Problem: **learned non-use**. The affected arm is avoided because it fails.
  - Trick: the **virtual arm reaches further and more accurately** than the real one.
  - Result: more use of the paretic arm, **also after the trick is removed** (20 patients).
  - **RIMT (2016)**: double-blind RCT, 18 chronic patients, 6 weeks.
  - Recovery is still possible **more than 1 year after stroke** (219 patients, 2019).
  - Course link: a sensory mapping with **gain > 1**, like the amplified tilt in the balance belt.

### C3. Mirrors and illusions

- A mirror hides the affected limb and reflects the healthy one, so moving the healthy limb looks like moving the affected one. The illusion engages the motor areas of the affected side. Also used for phantom limb pain.
- **Cochrane review (2018)**: 62 studies, 1,982 participants; **SMD 0.47** better motor function at the end of treatment.
- Open question: does it last? Only 2 trials measured it at 6 months.

### C4. Posture and balance feedback

- Force plate or Wii Balance Board → **centre of pressure** → a dot on the screen; shift weight to the weaker leg; games. This is the same mapping as Balance → Vision in Part A.
- Evidence:
  - force platform (Cochrane): better stance symmetry, but balance and independence not clearly better
  - **Wii Fit** (20 patients): improved as much as conventional therapy, not more
  - robotic gait + VR (Lokomat): adds feedback and motivation, but its own effect isn't yet established
- **Lesson: feedback changes what is trained; check that it transfers to daily life.**

### C5. Commercial and home systems

- **MindMotion PRO** (MindMaze): cameras map movements onto an avatar; FDA 510(k); its RCT was terminated early.
- **SWORD Health**: wearable motion sensors + tablet at home. Low back pain RCT (140): as good as in-person, fewer drop-outs.
- **RGS@home** (Eodyne): RGS games at home, monitored remotely by the therapist.
- At home: more dose and lower cost, but **engagement, supervision and safety** become the design problems.

### C6. What the evidence says

- **Cochrane 2017** (72 studies): VR vs conventional therapy, **not better**; helps **as an add-on**.
- **2025 update** (190 trials): small benefit; moderate as an add-on to usual care.
- **EVREST** (Wii vs card games): the same arm recovery with the same time of recreational activity.
- **Design principles for rehab interfaces**:
  - **Dose**: make many repetitions possible and motivating.
  - **Task**: train movements that matter in daily life; check transfer.
  - **Feedback**: adapt difficulty; use perception tricks (amplification, mirrors) with care.
  - **Evidence**: compare against the **same amount** of conventional practice.
- **In short: the interface helps when it adds well-chosen practice, not by being high-tech.**

### C7. State of the art since 2021

| Year | Event                                                                                | Mapping                               |
| ---- | ------------------------------------------------------------------------------------ | ------------------------------------- |
| 2021 | **Vivistim** FDA-approved: vagus nerve stimulation paired with each arm movement     | Movement → nerve stimulation          |
| 2021 | **IpsiHand** authorised: EEG BCI drives a hand orthosis                              | Intention → own hand movement         |
| 2023 | Spinal cord stimulation restores arm movement in 2 stroke survivors                  | Movement attempt → spinal stimulation |
| 2023 | **InTandem** becomes a prescription device; RCT of 87 people published 2024          | Steps → music tempo                   |
| 2024 | Meta-analyses: BCI with electrical stimulation; VR for balance and walking (43 RCTs) | Intention → muscle; body → vision     |
| 2025 | Cochrane VR update (190 trials); Medicare code for InTandem                          | Evidence and payment                  |

- **Trend: close the loop between intention, stimulation and feedback, and take it home.**
- **Stimulation paired with movement**:
  - **VNS (Vivistim)**: an implanted stimulator gives a burst at each movement repetition, strengthening the circuits used at that moment. 108 people: **5.0 vs 2.4** Fugl-Meyer arm points (VNS vs sham, 6 weeks); clinically meaningful response at 90 days **47% vs 24%** (Dawson et al., 2021).
  - **Spinal cord stimulation** (2023): electrodes over the cervical spinal cord, stimulating while the person tries to move. Better grasp and sense of arm position in 2 people.
  - **Design idea: timing is the interface.** Stimulation is useful when paired with the movement.
- **BCI for recovery**:
  - EEG intention to move → classifier → FES or hand orthosis → the patient feels the movement.
  - Mapping: **intention → proprioception**; it works even with no voluntary movement.
  - SMD 0.50 for arm function (BCI + FES, 10 RCTs, 290 patients, 2024); SMD 0.56 for BCI training (13 RCTs, 258 people, 2022).
  - Limits: small trials, expensive equipment, set-up time each session.
  - In the course framework, the **classifier is the feature extraction** and the **orthosis is the actuator**.
- **Rhythm for walking (InTandem)**:
  - Shoe sensors detect steps → cadence → the music beat adapts → steps follow the beat.
  - 87 people: **0.14 vs 0.06 m/s** faster walking than walking alone; responders **40% vs 13%**.
  - Prescription Class II device (2023); Medicare code (2025).
  - Course link: Movement → Sound in a closed loop, where **the tempo is the adaptive difficulty**.
- **Balance and walking**:
  - VR review (2024): 43 RCTs, 1,136 people with chronic stroke.
  - Pressure under the feet → **vibration gave better** static balance and symmetry than **visual feedback** (24 people, 2022), and keeps the eyes free.
  - Soft exosuit (2023): +22% foot clearance, +22% push-off, ~7% faster (19 people).
- **Home rehab with sensors**: FitMi sensor games vs paper exercises, **8.0 vs 3.0** Fugl-Meyer arm points (subacute stroke).
- **Trends and open questions (2026)**:
  - closed loop timed to each movement or intention
  - real-life measures (wearables count arm use at home)
  - regulation and payment (FDA approvals, Medicare codes)
  - small and often company-funded trials; compare against the same dose of conventional practice

---

## Part D · Glasses and headsets

### D1. Thirteen years of smart glasses

| Year | Device                 | What it added / what happened                                              |
| ---- | ---------------------- | -------------------------------------------------------------------------- |
| 2013 | Google Glass           | Small display + camera; consumer sales stopped 2015, Enterprise ended 2023 |
| 2016 | Microsoft HoloLens     | See-through AR; HoloLens 2 (2019), production ended 2024                   |
| 2016 | Oculus Rift, HTC Vive  | Consumer VR; 2023: Quest 3 and PS VR2 (eye tracking)                       |
| 2018 | Magic Leap One         | See-through AR; Magic Leap 2 (2022) for companies                          |
| 2019 | North Focals           | Everyday-looking display glasses; company bought by Google (2020)          |
| 2023 | Ray-Ban Meta           | Camera, open-ear audio, Meta AI                                            |
| 2024 | Apple Vision Pro       | Video-passthrough MR; Meta shows the Orion AR prototype                    |
| 2025 | Meta Ray-Ban Display   | Display in one lens + EMG wristband; also Galaxy XR, Nuance Audio          |
| 2026 | Android XR, Snap Specs | Gemini AI glasses (audio first); standalone AR Specs at $2,195             |

### D2. Four kinds of glasses

| Kind                                | Adds                                                                             | Examples                                                         |
| ----------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Camera + audio + AI, no display** | A voice that describes, reads and translates what the camera sees                | Ray-Ban Meta, Android XR audio glasses                           |
| **Small head-up display**           | Text, icons and captions in a corner of the view                                 | Google Glass, Meta Ray-Ban Display, Vuzix Blade, caption glasses |
| **See-through AR**                  | Graphics anchored in the room, over the real world                               | HoloLens, Magic Leap, Snap Specs, Meta Orion                     |
| **Video passthrough**               | Cameras film the world, so every pixel can be processed (zoom, contrast, labels) | Apple Vision Pro, Samsung Galaxy XR                              |

- **Google**: Glass offered a hands-free display and camera (Envision built reading and scene description for blind users on it), but met a privacy backlash, had a small display and short battery, and cost $1,500. Android XR (2025–2026): Gemini sees what you see; frames with Warby Parker and Gentle Monster; audio glasses first, a display later; cloud AI and privacy concerns.
- **Meta**:
  - **Ray-Ban Meta**: looks like normal glasses; **Be My Eyes** lets a volunteer see through the glasses for blind users. Downsides: camera privacy, dependence on the phone and Meta's cloud, battery of a few hours.
  - **Ray-Ban Display** ($799): a display in the right lens + **Neural Band EMG wristband** that reads small finger gestures. Reviews put the battery below the claimed 6 h; 69 g.
  - **Orion**: a see-through AR prototype, not for sale.
- **See-through vs passthrough**:
  - **See-through**: the real world is seen directly with no delay, but the field for graphics is small and graphics are faint outdoors.
  - **Passthrough**: every pixel can be changed (Zoom, Live Recognition), but it's heavy (500–650 g), ~2 h battery, isolating and expensive.

### D3. VR headsets

- Screens fill the view and headphones fill the sound, so **vision and hearing are replaced**; head tracking moves the image with the head.
- **Senses in conflict**: the eyes see motion but the inner ear feels none → **cybersickness**. Fixes: teleporting, a narrower view, vibration behind the ear.
- Uses: vestibular rehabilitation (small studies); **prototyping a new sense before building it**.
- **VR is the most complete substitution: it replaces the world for the eyes and ears, but the body keeps its own vestibular and proprioceptive signals.**

### D4. Eye tracking

- **Pupil centre + corneal reflection**:
  1. Infrared LEDs light each eye.
  2. Cameras film the eyes many times per second.
  3. Software finds the pupil centre and the LED reflections.
  4. After calibration (looking at dots), the **vector between them** gives the gaze direction.
- The fovea sees **≈ 2°** sharply (a thumbnail at arm's length); **saccades** are fast jumps, **≈ 3 per second**, between fixations.
- Hard parts: glasses, make-up, eyelids; **latency** (the display must update before the eye lands); drift when the headset moves.
- Devices with eye tracking: Vision Pro (look + pinch as the main input; Optic ID), Galaxy XR, PS VR2, HoloLens 2 / Magic Leap 2, Valve Steam Frame, Meta Orion.
- Devices without: Google Glass, Ray-Ban Meta, Quest 3/3S. Research devices: Tobii, Pupil Labs.
- **Uses**:
  - **Foveated rendering**: full detail only where you look (3.6× faster GPU frame time in a PS VR2 demo)
  - **Gaze as input**: look + pinch; Dwell Control (select by looking alone)
  - **Social presence**: avatars that make eye contact
  - **Accessibility**: gaze typing for people who cannot move (e.g. ALS)
  - **Health and research**: eye movements in vestibular tests; where people look
  - ⚠️ **Privacy risk**: gaze reveals interest, fatigue, emotion and health. Vision Pro gives apps only the tap, not the gaze.

### D5. Glasses built for one sense

| Device                                    | Mapping                                                                              | Pros / cons                                               |
| ----------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| **.lumen**                                | Vision → Touch: cameras + AI find a safe path; vibrations on the forehead steer you  | No cane needed in tests / heavy, price                    |
| **Envision**                              | Vision → Hearing: reads text aloud, describes scenes, calls a helper                 | Works on mainstream glasses / words only, cloud           |
| **Caption glasses** (XRAI Glass, Captify) | Hearing → Vision: speech → subtitles in the lens                                     | Follow conversations, translate / errors, display in view |
| **Nuance Audio**                          | Hearing → Hearing: a hearing aid in the frames (directional mics, open-ear speakers) | Nothing in the ears / mild to moderate loss only          |

### D6. Summary

- Each kind of device trades off: camera + AI (normal look, but privacy); head-up display (glanceable, but small); see-through (real world directly, but narrow graphics); passthrough (full control, but heavy); VR (complete control, but cybersickness); single-sense (one job done well, but niche).
- **Shared problems**:
  - privacy (bystanders and eye data)
  - battery vs weight
  - **dependence on company servers** (Glass, Focals, HoloLens 2 and Neosensory all ended)
  - prescription lenses
  - attention

---

## Design principles for choosing a mapping

1. **Substitute or augment?** Who uses it, and is the information lost or new?
2. **Which mapping type?** Topographic, parametric or symbolic, depending on source richness and target capacity.
3. **Follow cross-modal correspondences**: high ↔ high pitch, bright ↔ loud are learned faster.
4. **Close the loop**: low latency; let users move the sensor and explore.
5. **Match bandwidth, avoid masking**: reduce the data to what the task needs, and keep free the senses the user still relies on.

---

## In-class projects

**A. Design a mapping**: choose a cell in the matrix → choose the mapping type → define the encoding (e.g. tilt → vibration strength) → prototype (Grove IMU → Arduino/ESP32 → motor or sound; Processing for testing) → **test blindfolded** (accuracy and time with vs without the device).

- Substitution idea: trunk tilt → vibration on the side of the lean (a balance belt).
- Augmentation idea: compass heading → vibration or tone (a mini feelSpace).

**B. A rehab game**:

1. **Sense**: IMU on the wrist or trunk → tilt angles
2. **Map**: tilt × **gain** → cursor in Processing (gain > 1 amplifies small movements)
3. **Game**: reach targets; target size and distance set the difficulty
4. **Adapt**: over 80% hits → harder; under 50% → easier
5. **Log**: save repetitions, times and success to CSV; plot progress

- Test: compare gain 1 vs gain 2 on number of repetitions, success rate and reported effort.
- Feedback options: visual score, sound (pitch = tilt), or vibration when on target.

---

## Key references

Bach-y-Rita et al. (1969, 1998) · Bach-y-Rita & Kercel (2003) · Meijer (1992, vOICe) · Auvray et al. (2007) · Abboud et al. (2014, EyeMusic) · Maidenbaum et al. (2014, EyeCane) · Wald et al. (2025) · Reed et al. (2019) · Fletcher et al. (2019) · Novich & Eagleman (2015) · Perrotta et al. (2021) · Tyler et al. (2003) · Danilov et al. (2007) · Wuehr et al. (2023) · Chow et al. (2021) · Stanley et al. (2025) · Nagel et al. (2005) · Schumann & O'Regan (2017) · Cassinelli et al. (2006) · Thomson et al. (2013) · Hamilton-Fletcher et al. (2016) · Spence (2011) · Lieberman & Breazeal (2007) · Narumi et al. (2011) · Zampini & Spence (2004) · Weech et al. (2018) · Cameirão et al. (2009–2011) · Rubio Ballester et al. (2015, 2016) · Thieme et al. (2018) · Laver et al. (2017) · Saposnik et al. (2016) · Dawson et al. (2021) · Powell et al. (2023) · Awad et al. (2024)
