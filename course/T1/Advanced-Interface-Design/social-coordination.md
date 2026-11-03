# Social Sensorimotor Coordination & Joint Attention

**Today's topic**: interfaces **between people**. How we measure coordination, what we know, and how to design for it.
**Structure**: framework → Part A: coordination → Part B: perceptual crossing → Part C: joint attention → Part D: collaborative interfaces, science games, art → design principles and in-class projects

---

## 0. Framework

### 0.1 Four ways of coordinating with others

| Concept                        | Meaning                                                          | Examples                     |
| ------------------------------ | ---------------------------------------------------------------- | ---------------------------- |
| **Joint action**               | Two or more people act together on a **shared goal**             | Carrying, playing, building  |
| **Interpersonal synchrony**    | Movements fall into a **shared rhythm**                          | Tapping, rowing, dancing     |
| **Joint attention**            | Both attend to the same thing, **and know the other does**       | Looking at the same object   |
| **Participatory sense-making** | **Meaning is created in the interaction**, not only in each head | De Jaegher & Di Paolo (2007) |

References: Sebanz, Bekkering & Knoblich (2006); De Jaegher & Di Paolo (2007); Tomasello (1995).

### 0.2 Social sensorimotor contingencies

- **Individual contingencies** (O'Regan & Noë, 2001): move the eyes and the image shifts. **Perceiving = mastering these laws**, which is also the basis of sensory substitution (last lecture).
- **Social contingencies**: **the other answers to my actions**. A's action → B's sensation, and B's action → A's sensation, so the two people form **one coupled system**.
- Relevant to joint attention, trust, empathy, and human–robot interfaces (EU project socSMCs; Lübbert et al., 2021).

### 0.3 How coordination is measured

| Level          | Measure                               | What it tells                       | Example                |
| -------------- | ------------------------------------- | ----------------------------------- | ---------------------- |
| **Timing**     | Asynchrony (ms), interval variability | How precisely they synchronise      | Tapping, clapping      |
| **Phase**      | Relative phase, phase locking         | In-phase or anti-phase coordination | Swinging, rowing       |
| **Adaptation** | Lag ±1 interval correlations          | **Who corrects for whom**           | Dyadic tapping         |
| **Direction**  | Granger causality, transfer entropy   | **Who leads, who follows**          | String quartet sway    |
| **Body**       | Heart-rate and breathing coupling     | Shared arousal                      | Choirs, fire-walking   |
| **Brain**      | Inter-brain synchrony (EEG, fNIRS)    | Shared attention or engagement      | Classroom, cooperation |

- ⚠️ **Always add a control**: the same task without interaction (or with a recording of the partner). Shared music or shared stimuli **correlate people on their own**.

---

## Part A · Coordination: tapping, playing and moving together

### A1. Tapping to a beat

- **Asynchrony** = tap time − beat time. It is usually **negative**: taps come tens of ms **before** the beat (anticipation).
- **Variability**: the spread of the intervals between taps, a measure of timing precision.
- **Error correction**: after a shifted beat, taps correct both **phase** and **tempo**.
- **Build it**: a force sensor per tapper → Arduino → a metronome Arduino (GEM, 2022).
- References: Repp (2005); Repp & Su (2013); Fink, Alexander & Janata (2022).

### A2. Does coordination need a central clock?

- Examples of synchrony without one: **flashing fireflies, heart pacemaker cells, power grids, audiences clapping**.
- Answer: **coordination needs a common shared medium**, not a central clock.

### A3. The Kuramoto model

- Each individual is an **oscillator** with its own natural frequency, pulled toward the others' phases.
- **Order parameter r** ("how together we are"):
  - **r ≈ 0**: the phase arrows cancel; no shared rhythm.
  - **r = 1**: everyone at the same phase.
- **Feedback, "feeling the crowd"**: each one is pulled by the group with strength **K·r**. More synchrony → a stronger pull → more synchrony.
- **Criticality**: there is a **critical coupling Kc**.
  - Below Kc: r ≈ 0, everyone on their own.
  - Above Kc: a **cluster forms by itself**.
  - The **spread of natural frequencies** matters: Kc = 2γ for the distribution used on the slide, about 1.6σ for a Gaussian.
- **For design**: a group synchronises when **coupling is large compared with its differences**. So either **raise K** (clearer, louder feedback of the others) or **narrow the differences** (a shared, comfortable tempo).
- References: Kuramoto (1975, 1984); Strogatz (2000).

### A4. Tapping together: mutual adaptation

- Partners' intervals lengthen and shorten **in opposite directions**: each corrects toward the other.
- **No leader**: pairs adapt to each other tap by tap (Konvalinka et al., 2010).
- **Without a metronome, pairs speed up more than solo tappers** (Okano et al., 2017).
- **GEM** (Groove Enhancement Machine, 2022): four tappers and a metronome that **adapts to them**.
  - **25–50%** metronome correction gave the best group synchrony.
  - A responsive irregular partner is as easy to follow as a perfect metronome.
  - Adapting **too much** makes it worse and less enjoyable.

### A5. The mirror game (Noy, Dekel & Alon, 2011, _PNAS_)

- Two handles on parallel tracks, moving in 1D, recorded every 20 ms.
- Three stages:
  1. **Leader–follower**: one leads, the other follows.
  2. **Joint improvisation**: nobody leads; the motion is created together.
  3. **Measure**: velocity of both handles, match and jitter.
- Results:
  - **Without a leader**, synchrony reaches **< 40 ms**.
  - A designated **follower** shows **2–3 Hz jitter** (constant micro-corrections).
  - **Co-confident motion**: smooth, complex movement where nobody leads (experts reach it).
- **Design idea: shared leadership can coordinate better than a fixed leader.**
- **Build it**: 2 slide potentiometers → ESP32 → Processing.

### A6. String quartets: who adapts to whom

- Method:
  - a microphone on each instrument
  - tone onsets → asynchronies between every pair
  - fit a model where each player corrects a fraction **α** of each asynchrony
  - body sway from motion capture → Granger causality (2017)
- Findings:
  - **Quartet A, "autocracy"**: the first violin adjusted **less** to the others than they adjusted to her.
  - **Quartet B, "democracy"**: the first violin corrected **as much as** everyone else.
  - **Body sway** (Chang et al., 2017): hidden leaders drive the others' sway; **more coupling → better-rated performance**.
- References: Wing et al. (2014); Chang et al. (2017).

### A7. Groups as networks

- **Violin networks** (Shahal et al., 2020): 16 electric violins; a computer-controlled mixer sets **who hears whom** in each player's headphones, along with coupling strength and delay. Players change tempo and **ignore some partners** to find a stable rhythm.
- **Drum circles** (Dotov et al., 2022): groups of 1, 2, 4 or 8 drummers; a metronome, then muted. **Bigger groups are steadier**, don't speed up, and have no leader.
- **Design idea: who hears whom, how loud, and with what delay are parameters of the interface.**
- An AID project slide shows "**The Haptic Conductor**" (image only, no details).

### A8. Synchrony and cooperation

- **Moving Mandala** (UPF, 2025; Cross, Parés et al.):
  - Four children on a 6 × 6 m interactive floor, each with a tracked LED disc, activate glitter to grow one **shared mandala**.
  - Conditions: asynchronous, synchronous, or synchronous + music (60 children aged 8–9).
  - Afterwards: candy sharing and where they stand (Island Game).
  - Results: after **synchronous movement**, children **stood closer**; after **musical synchrony**, more **pro-social sharing**.
- Infants and children:
  - 14-month-olds **bounced in time** with an adult helped more (Cirelli et al., 2014).
  - 4-year-olds who **made music together** helped more (Kirschner & Tomasello, 2010).
- ⚠️ **Caution**: in a meta-analysis of 60 experiments, when experimenters were **blind** to the condition, the effect was **about 0** (Mogan et al., 2017).

### A9. Playing together over a network

- Two rooms; Max/MSP adds 10, 20 or 40 ms of delay before each pianist hears the other.
  - Average tempo drops as delay grows: **≈ 95 → 92 → 86 bpm**, from a start of about 90 bpm.
  - **Delay makes partners slow down.**
- Thresholds:
  - **25–30 ms** one-way delay: clapping pairs start losing synchrony.
  - **> 60 ms**: coordination generally breaks down.
  - For scale: sound travels about **8 m in 25 ms** on a stage.
- **Latency budget** = sensing + processing + network + audio output. Tools: **JackTrip** for audio, **OSC** for control.

### A10. Brains in sync: hyperscanning

- **Cooperation** (meta-analysis, 2022): 13 fNIRS studies, 890 participants. Synchrony appears in **prefrontal and temporoparietal** cortex.
- **Classroom** (Dikker et al., 2017): 12 students with portable EEG over 11 lessons. More synchrony went with **engagement and closeness**.
- ⚠️ Cautions:
  - Shared music or tasks correlate brains even **without interaction**.
  - Samples are small, and the meta-analysis covers fNIRS only.
  - Always use controls: same stimulus, no interaction.

---

## Part B · Perceptual crossing: how do we recognise that another agent is there?

### B1. The experiment (Auvray, Lenay & Stewart, 2009)

- Two people, each moving along a **1D line** with a mouse. They **feel a vibration** whenever they overlap **anything**. One click means "this is the other".
- Three kinds of object, **all of which feel the same**:
  - **Avatar** (the partner): senses and moves.
  - **Shadow**: moves **exactly like the partner** (at a fixed offset) but **senses nothing**.
  - **Fixed object**: never moves.
- **The question**: can people find the other person when the shadow moves exactly like them?

### B2. Results: recognition emerges from the interaction

- **65.9%** of clicks were on the partner (shadow 23.0%, fixed object 11.0%).
- **52.2%** of touches came from the partner (fixed 32.7%, shadow 15.2%).
- **The number of clicks per touch was the same for all objects.** So people don't detect the partner by some feature of a single touch.
- The partner is found **because the pair keeps meeting**:
  - the avatars cross, both feel the touch, both turn back, and they cross again
  - this is **a stable mutual loop**, in which the partner becomes an **attractor**
  - the shadow can't answer, so the loop never forms with it (Di Paolo, Rohde & Iizuka, 2008)
- **Joint awareness** (Froese et al., 2014): the rated clarity of the other's presence was a **joint achievement** of the pair.
- **Lesson: the other is what answers to me. Recognition lives in the mutual dynamics.**

### B3. Perceptual crossing today

- **2D and team versions**: collaborating partners recognised each other's avatars more often.
- **Co-embodied VR** (ShareYourReality, CHI 2024): 20 pairs share one avatar. Haptics **lowered** the sense of agency in free reaching and **raised** it in a shared task.
- **Autism and agents**: minimal interaction is used to study social difficulties and to design responsive agents.
- **1 bit** of touch is enough to feel another presence, **if the interaction is mutual**.
- Project idea: **no 3D version of perceptual crossing has been built yet.**

---

## Part C · Joint attention: looking together at the same thing

### C1. The social triangle

- Person A – Person B – Object, with **mutual gaze** between the two people.
- **Two forms**:
  - **Responding**: follow the other's gaze or point.
  - **Initiating**: direct the other's attention, by pointing or alternating gaze.
- It develops at **9–18 months**.
- **Why it matters**: it is the **foundation of language and social learning**, and it is often reduced in **autism**, which makes it a target of early intervention (Tomasello, 1995; Mundy & Newell, 2007).

### C2. Talking Heads (1999–2001)

- A pioneering experiment in which situated, embodied agents (cameras) created a **shared vocabulary** through **language games** about real-world scenes.
- In each game one agent was the speaker and the other the hearer; they used words to refer to objects (e.g. a particular colour) and achieve mutual understanding.
- → **Meaning arises from use.** The agents built an ontology and a language through collaborative problem-solving, not from pre-programmed definitions.
- _The Talking Heads experiment was led by Luc Steels; the slide doesn't name him._

### C3. Creating joint attention with technology

- **Gaze-contingent characters**: an eye tracker lets a virtual face **follow or lead** the user's gaze in real time.
- **Dual eye tracking**: two mobile eye trackers record where both partners look (20 sessions).
- **Robots that follow gaze**: people looked back at the robot sooner and **liked it more** (Willemse & Wykowska, 2019).
- **Autism research**: gaze-contingent avatars test initiating and responding to joint attention.
- Course link: eye tracking in headsets (last lecture) makes these setups portable.

### C4. Shared gaze on art

- Each viewer's gaze points are drawn over the artwork, live or accumulated into maps. **Overlapping gaze = joint attention.**
- **5,000+** visitors' gaze combined into maps (National Gallery, 2002).
- Museum installations (Cleveland, ARoS, M Leuven); **How We Gaze** (2022) shows your gaze next to others' in real time.

### C5. The Mutual Wave Machine (Dikker et al.)

- Origin: work with **Marina Abramović** (_The Artist Is Present_, 2010).
- Two people sit face to face in a dome wearing EEG headsets; the **correlation of their signals** is shown as **light and sound**.
- **Research questions**:
  - Does real-time feedback of EEG correlation (neurofeedback) make people **feel more connected** and **increase brain synchrony**?
  - Does the feedback have to be **real**, or is it enough that people **believe** it shows how well they connect?
- About **5,000 participants** across 14 exhibitions (2013–2019).
- **"Seeing is believing"**: synchrony **rose when people believed the light was theirs, even if it was fake**.
- Related: _The Magic of Mutual Gaze_, a video visualising the brain activity of two people making eye contact.

### C6. A family of synchrony-feedback projects

| Signal          | Example projects                                               | Shown back as                               |
| --------------- | -------------------------------------------------------------- | ------------------------------------------- |
| **Brain (EEG)** | Mutual Wave Machine; Mutual Gaze (2011); Hybrid Harmony (2021) | Light and sound; on-screen graphics         |
| **Heart**       | Pulse Room (2006); Intimate Heartbeats (2010); Animo (2017)    | Flashing bulbs; heard heartbeat; smartwatch |
| **Breath**      | Breeze (CHI 2018); DYNECOM in VR (2019)                        | Light, sound, vibration; a shared VR scene  |
| **Movement**    | Mirror game; joint tapping (Part A)                            | What each person sees and hears             |

- General pipeline: sense two people → compute synchrony → show it back → do they feel connected?
- **Key control: fake feedback** shows whether the real signal matters, or only the belief in it.

### C7. Games and robots for social interaction in autism

- **Lands of Fog** (UPF Full-Body Interaction Lab):
  - Two children explore a 6 m floor projection, tracked by 4 cameras; they uncover the fog together and creatures appear.
  - Co-designed with autistic children.
  - First trials with **34 children**: improved engagement and social attitudes.
- **Pico's Adventure**:
  - A Kinect game in which children help the alien Pico. Missions call for social initiation: alone, with an adult, with a peer. Supervised by an adult.
  - **15 boys aged 4–5** made more peer initiations than in free play.
- **Kaspar** (University of Hertfordshire, 2005–):
  - A child-sized robot with a **simple, predictable face**; turn-taking, imitation and shared-gaze games.
  - Children then **collaborated better with people**.
- **Floreo Joint Attention Module (VR)**:
  - A virtual guide asks the child to look and point, while an adult stays with the child.
  - 12 participants, 14 sessions: safe, early gains (2019).
- ⚠️ Caution: these are small studies, often run by the developers.

---

## Part D · Collaborative interfaces, science games and art

### D1. Mutual collaborative interfaces

- **Reactable** (UPF, 2005–): tangible objects on a luminous table; **several performers share one instrument**; a camera tracks markers (reacTIVision).
- **Shimon**, a robot musician: listens, anticipates and improvises with humans; its gestures help coordination.
- **Shared bodies in VR**: two people control one avatar (co-embodiment, 2024).

### D2. Science games: solving problems together

- **Foldit** (2008–): protein folding as a puzzle. Players solved the structure of a retroviral protease in about **ten days** (2011).
- **Borderlands Science**: > 4 million players solved 135 million puzzles to align gut-bacteria DNA.
- **Sea Hero Quest**: > 4 million players generated navigation data for dementia research.
- **Why it works**: human pattern skills + game motivation + many players.

### D3. Art that couples people

Read each one as an interface: **sensor → processing → what the other person perceives**.

| Work                                 | Sensor                   | Processing                         | Output                                                         |
| ------------------------------------ | ------------------------ | ---------------------------------- | -------------------------------------------------------------- |
| **Mutual Wave Machine**              | 2 EEG headsets           | Correlation of the two signals     | Light and sound in a dome                                      |
| **Pulse Room** (Lozano-Hemmer, 2006) | Pulse sensor in the hand | Heartbeat timing                   | A bulb flashes; the last 100 pulses form a collective portrait |
| **The Machine to Be Another**        | Head tracker on the user | Servos turn the performer's camera | The headset shows the performer's view                         |

### D4. BeAnotherLab: born in this master

- **2012: born at UPF, Barcelona.**
  - From CSIM: **Arthur Pointeau** (this master).
  - Also from the digital arts master (Bertrand, González Franco) and the SPECS lab (Cherene).
- **Loop**: the user wears a headset, headphones and a head tracker. The user's head orientation → servos move the **performer's head camera**, so the performer copies the user, and the user sees the performer's view and hears their voice and stories.
- Projects: Gender Swap, Body Swap, Embodied Narratives, Library of Ourselves (360° first-person films in social VR).
- **Still active (2026)**: a workshop at **CHI 2026, Barcelona**; open-source software updated Jan 2026; studies on phenomenology (2020) and a user study (2024).
- **A low-cost social sensorimotor loop** (head tracking → servo camera → a human avatar) from this master, shown worldwide for over ten years.

---

## Design principles for social interfaces

1. **Make the loop mutual**: each person's action must change what the other senses (perceptual crossing, joint tapping).
2. **Respect the latency budget**: **below about 25 ms** for rhythm; longer delays make partners slow down.
3. **Allow shared leadership**: fixed leaders can coordinate worse than co-creation (mirror game).
4. **Make the other perceivable**: show the partner's state through gaze, sway, sound, light or vibration.
5. **Measure, with controls**: asynchrony and direction of influence; control for shared stimuli and expectations.

---

## In-class projects

| Project                 | Hardware                                                  | Procedure                                                                      |
| ----------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Joint tapping**       | 2 Grove buttons → Arduino → Processing                    | Metronome first, then partner only. Measure asynchrony and lag ±1 correlations |
| **Perceptual crossing** | 2 laptops via OSC; a potentiometer + vibration motor each | Partner, shadow and fixed object on a 1D ring. Log clicks: who finds whom?     |
| **Mirror game**         | 2 sliders → Arduino → Processing                          | Record positions every 20 ms. Compare leader rounds vs joint improvisation     |

- **Measure it**:
  - save every event with its timestamp to CSV
  - compute asynchrony and interval correlations
  - for the mirror game, find the **delay that maximises the cross-correlation**

---

## Key references

Sebanz et al. (2006) · De Jaegher & Di Paolo (2007) · Tomasello (1995) · O'Regan & Noë (2001) · Repp (2005); Repp & Su (2013) · Kuramoto (1984); Strogatz (2000) · Konvalinka et al. (2010) · Okano et al. (2017) · Fink et al. (2022, GEM) · Noy, Dekel & Alon (2011) · Wing et al. (2014) · Chang et al. (2017) · Shahal et al. (2020) · Dotov et al. (2022) · Cross, Parés et al. (2025) · Cirelli et al. (2014) · Kirschner & Tomasello (2010) · Mogan et al. (2017) · Washburn et al. (2021) · Czeszumski et al. (2022) · Dikker et al. (2017, 2021) · Auvray et al. (2009) · Di Paolo et al. (2008) · Froese et al. (2014) · Mundy & Newell (2007) · Willemse & Wykowska (2019) · Mora-Guiard et al. (2016, 2017) · Mairena et al. (2019) · Jordà et al. (2007) · Khatib et al. (2011) · Bertrand et al. (2014)
