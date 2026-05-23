---
title: "Why We Can’t Stop Asking Why"
date: 2026-05-23
source: medium
canonical_url: https://medium.com/@leitingting08/why-we-cant-stop-asking-why-f76453743a0a
tags: ["cognitive-science", "artificial-intelligence", "machine-learning", "psychology", "philosophy"]
---

![](https://cdn-images-1.medium.com/max/1024/1*ZOXTlo8yPLEc-kScE9lDvA.png)

There is a question we ask almost every day, yet rarely stop to examine its underlying logic: why.

Kahneman observed in _Thinking, Fast and Slow_ that the human brain is a storytelling machine. System 2 instinctively constructs causal narratives to justify what System 1 has already felt and decided — even when those narratives are fabricated after the fact. Our drive to seek causes runs deeper than habit. It is embedded in cognition itself.

Yet the tools of science took a different path. Statistics excels at describing correlation while remaining cautious about causal claims. The result is a peculiar mismatch: human intuition relentlessly asks _why_ , while the language of science keeps responding with _correlated but not causal_. This gap is not merely philosophical. It leaves many problems that could be intervened upon stuck at the level of description.

In _The Book of Why: The New Science of Cause and Effect_ , Judea Pearl set out to bridge this gap — to give “why” a rigorous methodology, and transform it from intuition into a usable tool.

### **The Ladder of Causation**

Pearl argues that anyone who wants to reason about cause and effect must master three distinct levels of cognition: the ability to _see_ , the ability to _do_ , and the ability to  _imagine_.

He maps these onto what he calls the Ladder of Causation.

The first rung is **association** : What do we observe? X and Y tend to appear together. This is pure observation — and it is where traditional statistics and most machine learning remain.

The second rung is **intervention** : What happens if I change X? This requires stepping outside the data and actively acting on the system.

The third rung is **counterfactual** : What would have happened if things had been different? This is among the most complex and distinctly human of cognitive capacities.

There is an unbridgeable gap between these rungs that no amount of data can cross. No matter how many observations we accumulate, we cannot climb from the first rung to the second without introducing a causal model.

This is Pearl’s central claim: causal structure does not live in the data. It lives in our assumptions. We must first have a model of the world before we can meaningfully ask why.

### **Where Does AI Stand on the Ladder?**

A question once circulated online: I want to get my car washed. The car wash is only 50 meters away. Should I walk or drive?

Most AI systems recommended walking.

This answer is obviously wrong. If you walk, the car stays behind — and the whole point was to wash the car. But why does AI make such a seemingly elementary mistake? Because it never stably connected “car wash” with the implicit constraint that _the car must be present_.

This is a failure of the second rung: **intervention reasoning**. Answering this question requires mentally simulating the consequences of the action “walk there” — and that requires a causal model of the physical world.

Large language models do not possess a stable, explicit, verifiable causal world model. What they have instead is something closer to implicit structure that emerges from massive statistical compression. They learned the world as humans described it in writing — but the most basic human assumptions about the world, like _the car needs to be there to get washed_ , are precisely the things too obvious to ever write down. The simpler the shared understanding, the less likely it is to appear in training data. This is a structural blind spot of language-trained systems.

By Pearl’s framework, current AI remains largely on the first rung. It touches the edges of the second in certain tasks. The third rung — genuine counterfactual reasoning — has not yet been stably reached.

### **Priors, Bayes, and the Self-Fulfilling Belief**

Pearl’s causal models must be set by humans. This means subjectivity is inescapable. We cannot extract causal structure from data alone — we can only enter the world carrying assumptions, then update them against reality.

This way of thinking — bring a model in, revise it as you go — has something in common with Bayesian inference.

The basic Bayesian structure is: prior belief + new evidence → updated belief. The posterior becomes the new prior for the next round of reasoning. Cognition is this loop, running without end. But the loop has a condition: the prior must remain open to revision.

When a prior becomes too strong, new evidence loses its power to update it. We begin selectively noticing what confirms our expectations and filtering out what doesn’t. The prior reinforces itself, and the system closes.

A common Chinese saying goes: _belief makes things appear real._

This is usually treated as mysticism. But it describes a very exact cognitive mechanism: the brain does not passively record reality — it interprets reality through its existing models. The filtering apparatus of the mind finds what it is already looking for. No mysterious force is required.

The logic extends widely. Astrology, religion, the law of attraction, even certain scientific hypotheses: Any sufficiently vague system can seem self-confirming once belief enters the loop. The question is never simply whether to believe, but how strong the prior is, and whether it remains permeable to reality.

Pearl’s causal framework is, in this sense, an attempt to go beyond what Bayesian inference describes — updating beliefs — and into the harder problem of modeling the structure of intervention itself.

### **The Same Problem, Encoded Differently**

This trap exists in AI as well. It is, in fact, one of the root causes of hallucination.

An AI model’s priors come from its training data. Biases encoded in that data become priors, which the model cannot perceive in itself. LLM internalizes whatever statistical regularities the internet contains — not by choice, but by construction. And unlike humans, it has no continuous self-correction mechanism. Its updates are discrete, externally driven, and far less fluid than the ongoing revision a person undergoes simply by living.

The cognitive trap of _believe and it exists_ operates in AI with a rigidity humans rarely experience. We can be confronted by reality and forced to revise. Once training ends, the model’s priors are largely fixed.

Pearl’s ladder implies something deep about what intelligence actually is: genuine understanding means being able to imagine worlds that do not exist, and to reason within them. This capacity — to detach from present sensory input and run mental simulations of hypothetical scenarios — is what human evolution produced, and what allows us to intervene in the world rather than merely react to it.

What AI currently does is powerful compression and association. It has encoded nearly everything humans have written. But it lacks a stable mechanism for asking why any of it is true. It can generate explanations — but those explanations do not necessarily point toward how the world actually works.

And “why” is where everything begins.

### **The Question That Separates Us**

Every animal can learn associations. A dog salivates when a bell rings because bell and food appeared together. But only humans ask: why does food follow the bell? And if the bell rings but no food comes — does the salivation still make sense?

Counterfactual reasoning is what distinguishes human cognition from every other form of intelligence we know. It lets us imagine what never happened, trace the paths not taken, and use those imagined alternatives to act more precisely in the world we actually inhabit.

Maintaining the vitality of our priors — keeping them genuinely open to revision rather than just nominally so — may matter more than finding any particular correct answer.

Perhaps the endpoint of asking “why” is not the discovery of a final causal chain. Perhaps it is the ongoing discipline of watching your own model — knowing it is there, knowing it filters, and letting reality correct it when necessary.
