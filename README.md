# Computational Modeling of Classical Conditioning in Fruit Flies Using Cybernetic Automata

## Overview
This project explores how fruit flies (Drosophila melanogaster) form odor-associated avoidance memories by using a **cybernetic automaton model**—a mathematical system that adapts through feedback. By replicating behavioral neuroscience protocols computationally, the project aims to reduce reliance on live animal testing while offering a scalable, mechanistic perspective on learning and memory.

## Objectives
- Simulate **first-order and second-order conditioning** protocols (Paired–Paired, Paired–Unpaired, Unpaired–Paired).
- Model the role of conditioned stimuli (CS1, CS2) and an unconditioned stimulus (UCS) in avoidance learning.
- Compare simulation results with published **biological experiments** to validate the model.
- Explore how **feedback-driven systems** can shed light on decision-making and adaptive behavior.

## Methods
- **Simulation Setup:** 100 virtual flies divided into two groups of 50.
- **Training Protocols:**
  - **P–P (Paired–Paired):** UCS paired with CS1; CS2 linked with CS1.
  - **P–U (Paired–Unpaired):** UCS paired with CS1; CS2 dissociated.
  - **U–P (Unpaired–Paired):** UCS dissociated from CS1; CS2 paired with CS1.
- **Analysis:** Performance Index (PI) values calculated to quantify avoidance responses.
- **Implementation:** Python (with standard libraries for data structures, math, and visualization).

## Results (Highlights)
- **P–P protocol:** Strong conditioning of CS1 and transferable learning for CS2.
- **P–U protocol:** Negative PI values for CS2, suggesting failed learning due to disassociation.
- **U–P protocol:** Negative PI values for both CS1 and CS2, indicating disrupted associations.

These results qualitatively replicate key behavioral signatures but highlight the need for further refinement to match biological data quantitatively.

## Future Work
- Investigate why PI values diverge in P–U and U–P protocols.
- Analyze how model dynamics and stimulus timing contribute to discrepancies.
- Extend the framework to broader questions in **cognitive science** (e.g., decision-making under uncertainty, multi-step reinforcement learning).
- Explore applications in **computational neuroscience** and **bio-inspired machine learning**.

## Repository Structure
