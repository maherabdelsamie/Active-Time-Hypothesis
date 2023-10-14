# Reimagining Quantum Non-Locality: Simulating Entangled Systems with the Active Time Hypothesis

Dr. Maher Abdelsamie<br>maherabdelsamie@gmail.com<br>


## Abstract

**Background**: Time, traditionally viewed as a passive backdrop against which events unfold, finds a transformative interpretation in the Active Time Hypothesis (ATH), positioning it as an active agent in the cosmos with properties of being generative, directive, and adaptive. 

**Objectives**: This research seeks to explore the implications of the ATH, contrasting it with conventional conceptions of time, and examining its repercussions in both philosophical and physical realms.

**Methods**: Utilizing a dual-layered approach, the study employed classical and quantum simulations. The classical simulation modeled the evolution of a physical quantity $`\Phi`$ under the influence of active time's properties. The quantum simulation focused on the evolution of entangled qutrit systems, gauging the effect of active time on quantum dynamics and entanglement.

**Results**: The classical simulation revealed an unpredictable and fluctuating nature of $`\Phi(t)`$, influenced by time's generative property. The quantum simulation demonstrated varying degrees of entanglement entropy, suggesting the potential of the ATH to modify quantum correlations.

**Conclusions**: The ATH challenges traditional perspectives, proposing time as a dynamic entity actively influencing events. The interplay between classical stochasticity and quantum entanglement raises profound questions about causality, determinism, and the very nature of reality. The ATH introduces the possibility that quantum non-locality may arise from time's intrinsic non-local agency rather than spatial connections.



## 1. Introduction

Throughout human history, our understanding and interpretation of time have been shaped by a confluence of philosophy, religion, and, more recently, physics. Historically, the dominant perspective has been that time serves as a passive backdrop against which events unfold, acting merely as a parameter in the equations of motion.

However, in this article, we propose and explore a radical departure from this view: the Active Time Hypothesis (ATH). Instead of perceiving time as a passive observer, the ATH envisions it as an active participant in the cosmos, endowed with properties that can directly influence the unfolding of events. This approach attributes three distinct properties to time: Generative, Directive, and Adaptive.

The implications of the ATH are profound and wide-reaching. Philosophically, an active conception of time challenges our notions of causality, destiny, and the very essence of reality. On the physical front, the ATH opens up intriguing avenues for exploration. Could some of the quirks of quantum mechanics, or the enigmatic nature of dark matter, be manifestations of time's active role?

In the ensuing sections of this article, we embark on a comprehensive exploration of the ATH, contrasting it with traditional conceptions of time, and probing its potential repercussions in both the philosophical and physical realms.

---
## 2. Active Time Hypothesis: A Theoretical Overview

The fabric of time, traditionally viewed as a passive parameter, is envisioned in a transformative light under the Active Time Hypothesis (ATH). Delving deeper into its constructs, we find that the ATH attributes three distinct properties to time: Generative, Directive, and Adaptive. These properties, while novel, are grounded in mathematical formulations, each encapsulating a unique aspect of time's newfound agency.

2.1 **Generative Property of Time and its Mathematical Representation:**

The generative property postulates that time can spontaneously bring forth or influence phenomena in the universe. Akin to a cosmic muse, it suggests that time is not merely a canvas but a creator in its own right. Mathematically, this can be represented by the equation:


$$
\frac{\partial \Phi}{\partial t} = S(t)
$$

Where $\Phi$ is a generic physical quantity, and $S(t)$ is a time-dependent source term. The function $S(t)$ captures the inherent unpredictability and spontaneity of time's generative nature.

2.2 **Directive Property of Time and its Mathematical Representation:**

The directive property suggests that time can guide or influence the evolution of systems. Much like a conductor leading an orchestra, this property imbues time with the ability to steer the course of events, lending direction to the otherwise chaotic dance of the cosmos. It is mathematically represented as:

$$
\frac{\partial \Phi}{\partial t} = S(t) + G(\Phi, t)
$$

Here, $G(\Phi, t)$ is a term that captures the directive influence of time based on the state of the system and time itself.

2.3 **Adaptive Property of Time and its Mathematical Representation:**

The adaptive property introduces a radical idea: time itself can change its flow in response to the state of the universe. This suggests that time is not a rigid framework but a fluid entity, adapting and morphing in response to the cosmos's ever-changing states. This property can be captured by:


$$
\frac{d\tau}{dt} = 1 + A(\Phi)
$$

Where $\tau$ represents an "active time" parameter, and $A(\Phi)$ is an adaptive term that modulates the flow of time based on the state $\Phi$ of the universe.

2.4 **Implications on Causality, Determinism, and Temporal Flow:**

The ATH, with its newfound properties of time, ushers in profound philosophical and physical questions. If time can generate, direct, and adapt, then our conventional understanding of causality is challenged. Does the future have an influence on the present just as the past does? The deterministic view of the universe, where events unfold in a preordained sequence, may also need reevaluation. Perhaps the universe is a dynamic interplay of events, guided and shaped by an active temporal agent. Finally, the linear flow of time, a cornerstone of our experiential reality, might itself be an oversimplification. With the adaptive property, time could ebb and flow, accelerate or decelerate, painting a far richer and more intricate picture of temporal dynamics.

---

## 3. Classical Simulation of Active Time

The classical simulation is conceived as a way to computationally explore the Active Time Hypothesis (ATH). The ATH posits that time is not merely a passive backdrop to the universe's events but has properties that actively influence physical quantities. The simulation's design is based on modeling the evolution of a physical quantity $\Phi$ under the impact of three distinct properties of active time: generative, directive, and adaptive.

### 3.1  Mapping mathematical equations to code functions:

#### Generative term $`S(t)`$ and its simulation representation:

The generative term represents the spontaneous creation or influence of phenomena in the universe due to time. It is mathematically depicted by:

$$
\frac{\partial \Phi}{\partial t} = S(t)
$$

In the simulation, this term is emulated by the `S_func(t)` function. This function produces a combination of Gaussian noise and a random spike, capturing the unpredictable and spontaneous nature of time's generative property.

#### Directive term $`G(\Phi, t)`$ and its simulation representation:

The directive term encapsulates how time can guide or steer the behavior of systems. It is represented mathematically as:

$$
\frac{\partial \Phi}{\partial t} = S(t) + G(\Phi, t)
$$

Within the simulation, this directive property is modeled by the `G_func(Phi, t)` function. This function provides a negative feedback based on $\Phi$'s current value, ensuring that $\Phi$ decays over time, thus indicating time's directive influence on the system.

#### Adaptive term $`A(\Phi)`$ and its simulation representation:

The adaptive term highlights the concept that the flow of time can adjust or change based on the state of the universe. It's represented mathematically as:

$$
\frac{d\tau}{dt} = 1 + A(\Phi)
$$

In the simulation, this adaptive property is captured by the `A_func(Phi)` function. This function either amplifies or dampens the flow of active time $\tau$ based on the state $\Phi$ of the universe.

#### - Discretization for computational purposes:

Given the continuous nature of the equations that describe the behavior of $\Phi$ under the influence of active time, they need to be discretized to be suitable for computational simulations. This discretization process essentially involves breaking down time into discrete steps and approximating the evolution of $\Phi$ at each of these steps.

The core loop in the function `simulate_phi` implements this discretized equation:

$$
\Phi_{i+1} = \Phi_i + \Delta \tau \left(1 + A(\Phi_i)\right) \left[ S(t_i) + G(\Phi_i, t_i) \right]
$$

This equation allows the simulation to visualize the evolution of $\Phi$ under the influence of active time across a series of discrete time intervals.

---

## 4. Quantum Simulation of Active Time

The quantum simulation provides a comprehensive investigation of the impact of active time, as proposed by the Active Time Hypothesis (ATH), on quantum systems. Specifically, the focus is on the evolution of quantum states (particularly a system of two qutrits) and the entanglement between them. The simulation offers a deep dive into the potential modifications to quantum dynamics due to the active properties of time. The design integrates the classical generative term $S(t)$ into the quantum dynamics, ensuring intertwined classical and quantum explorations.

### 4.1 Mathematical foundations:

#### Schrödinger equation for quantum dynamics:

The evolution of quantum systems is traditionally governed by the time-dependent Schrödinger equation:

$$
i \hbar \frac{\partial |\psi(t)\rangle}{\partial t} = H |\psi(t)\rangle
$$

Here, $|\psi(t)\rangle$ represents the quantum state at time $t$, $\hbar$ is the reduced Planck constant, and $H$ is the Hamiltonian governing the system's dynamics.

#### Incorporation of active time influence through $`H_{ATH}`$:

The influence of active time on quantum systems is captured through an interaction Hamiltonian, $H_{ATH}$. This interaction term is directly influenced by the generative property of active time, represented by $S(t)$. Mathematically, the $H_{ATH}$ can be written as:

$$
H_{ATH} = f(t) \otimes \text{diag}([1, 0, -1]) \otimes \text{diag}([-1, 0, 1])
$$

In this expression, $f(t)$ is a function modulated by $S(t)$, and the tensor products represent interactions between the two qutrits.

#### Calculating entanglement entropy:

Entanglement entropy, $S$, serves as a measure of quantum entanglement in a system. For a given density matrix $\rho$, the entanglement entropy is calculated as:

$$
S(\rho) = -\text{Tr}[\rho \log_2(\rho)]
$$

Here, $\rho$ is the density matrix of the quantum system, and $\text{Tr}[]$ denotes the trace operation.

### 4.2 Observing quantum effects of active time:

The simulation tracks the evolution of a quantum system (specifically, two qutrits) under the influence of active time. Observables such as the entanglement entropy are monitored over time, providing insights into the quantum system's behavior under the ATH. The goal is to understand how the active properties of time, especially its generative aspect, might modify quantum correlations and lead to novel or altered quantum phenomena.

---

## 5. Connecting Theory to Simulation Code

#### 5.1 Theoretical foundations and their code representation:

**Temporal Agency**:

Temporal agency, as implied by the Active Time Hypothesis (ATH), suggests that time isn't just a passive backdrop against which events unfold; instead, it has an active role in shaping the universe. In the provided simulation code, temporal agency is primarily showcased through the `S_func(t)` function. This function, which models the generative property of time, spontaneously generates or influences phenomena in the universe, capturing the unpredictable and potentially active nature of time. The stochastic nature of `S_func(t)`, especially with its occasional spikes, embodies the idea that time can, at moments, take on an assertive role in influencing events.

**Cause and Effect**:

Traditional views of time suggest a linear progression of cause and effect. However, the ATH, as reflected in the simulation, brings a richer dynamics to this. The function `G_func(Phi, t)`, which represents the directive property of time, can be seen as time's way of directing or influencing how systems evolve. The damping effect introduced by this function suggests that time might have a guiding or stabilizing influence on systems, adding depth to our understanding of causality in a universe influenced by active time.

**Perception of Time**:

While humans perceive time linearly, the ATH introduces the intriguing idea that time might adapt based on the state of the universe. This adaptive nature of time is encapsulated in the `A_func(Phi)` function, which modulates the flow of active time $`\tau`$ based on the universe's state $`\Phi`$. This function, by amplifying or dampening the flow of time, suggests that our linear perception might just be an averaged-out experience of deeper, more intricate temporal dynamics.

#### 5.2 Mathematical formulation and its translation to code:

The code representation is deeply intertwined with the theoretical underpinnings of the ATH. The core equations of the hypothesis are:

1. Generative Property:

$$
\frac{\partial \Phi}{\partial t} = S(t)
$$

3. Directive Property:

$$
\frac{\partial \Phi}{\partial t} = S(t) + G(\Phi, t)
$$

5. Adaptive Property:

$$
\frac{d\tau}{dt} = 1 + A(\Phi)
$$

These mathematical formulations find their direct counterparts in the code as `S_func(t)`, `G_func(Phi, t)`, and `A_func(Phi)` respectively. The discrete-time implementation, especially the equation:

$$
\Phi_{i+1} = \Phi_i + \Delta \tau \left(1 + A(\Phi_i)\right) \left[ S(t_i) + G(\Phi_i, t_i) \right]
$$

is a computational representation of these continuous equations, enabling the study of ATH's implications in a simulated environment.

---

## 6. Detailed Analysis of the Simulation Code

The simulation serves as a computational framework to explore the theoretical constructs of the Active Time Hypothesis (ATH). By integrating classical and quantum simulations, the code seeks to provide insights into the potential behaviors and implications of a universe influenced by active time.

#### 6.1 Classical Simulation Detailed Analysis

- Generative Property $`S(t)`$:

  The function `S_func(t)` models the generative property of active time, which spontaneously influences phenomena in the universe. It uses Gaussian noise combined with random spikes to represent unpredictable events or generation of phenomena based on the progress of time.

```python

def S_func(t):

    return np.random.randn()  0.5 + (np.random.rand() < 0.005)  10

```

- Directive Property $`G(\Phi, t)`$:

  The directive influence of time on the evolution of the universe is captured by `G_func(Phi, t)`. This function, through its negative feedback based on $`\Phi`$, guides or directs the system to decay over time.

```python

def G_func(Phi, t):

    return -0.05 * Phi

```

- Adaptive Property $`A(\Phi)`$:

  Time's adaptive nature, as proposed by the ATH, is represented by `A_func(Phi)`. This function modulates the flow of active time based on the current state $`\Phi`$ of the universe.

```python

def A_func(Phi):

    return 0.1 * Phi

```

- Time Discretization and System Evolution:

  The function `simulate_phi` serves as the main loop for the classical simulation. It takes the continuous representation of the equations and converts them into a discrete form suitable for numerical simulations. This function provides a tangible platform to observe how the universe evolves under the influence of the generative, directive, and adaptive properties of active time.


```python

for i in range(n_steps - 1):

    t = t_values[i]

    Phi[i+1] = Phi[i] + delta_tau  (1 + A_function(Phi[i]))  (S_function(t) + G_function(Phi[i], t))

```


#### 6.2 Quantum Simulation Detailed Analysis

- Quantum Dynamics Implementation:

  Quantum systems' evolution is governed by the Schrödinger equation, which is numerically solved using the Runge-Kutta method in the `runge_kutta_evolution` function. This method provides a way to understand how quantum states evolve based on their Hamiltonian, an essential component in quantum mechanics.

- Incorporating Active Time:

  The active time's influence on quantum dynamics is integrated through the interaction Hamiltonian $`H_{ATH}`$, which is dynamically adjusted based on the classical generative term $`S(t)`$. This ensures that the classical and quantum simulations are intertwined, bringing cohesion to the entire simulation process.

- Entanglement Entropy:

  Quantum entanglement is a fundamental phenomenon in quantum mechanics, and the `entanglement_entropy` function quantifies this. By calculating the entanglement entropy of the system's density matrix, one can understand how active time potentially influences quantum correlations.

#### 6.3 Enhanced Driver Function

- Unified Simulation:

The `run_unified_sim_advanced` function integrates both classical and quantum simulations, providing a comprehensive view of the ATH's implications. It also serves as the primary function for visualization, allowing users to visualize how $`\Phi(t)`$ and quantum entanglement evolve under the ATH.

#### 6.4 Initialization and Parameters

- Quantum Initialization:

  Before executing the simulation, the quantum variables, including the initial states of the qutrits and their Hamiltonians, must be initialized to ensure accurate and meaningful results.

- Parameter Customization:

  The `simulation_params` dictionary acts as a centralized configuration for the simulation. By adjusting values within this dictionary, users can customize and tailor the simulation to investigate various scenarios under the ATH.

---

## 7. Simulation Results and Discussion

Our advanced unified simulation provides an integrative insight into both classical and quantum dynamics. The simulation was conducted over a time span $`T = 10`$ units with a time step $`\Delta \tau = 0.01`$.

**Classical Dynamics**:
The classical part of the simulation is predominantly focused on the evolution of the function $`\Phi(t)`$. The function is affected by stochastic terms, evident by its fluctuating nature. The sudden spikes observed in $`\Phi(t)`$ are a result of the probabilistic impulse perturbations introduced by the function $`S(t)`$, which occasionally gives rise to significant perturbations.

**Quantum Dynamics**:
The quantum portion of our simulation captures the entanglement entropy over time. Entanglement entropy is a measure of quantum correlations between subsystems, and its evolution provides vital information about the dynamics of the system. The observed entropy indicates the varying degree of entanglement the qutrit system undergoes during its evolution. The entanglement entropy, as seen, fluctuates and demonstrates the intricate dance of entanglement and disentanglement events as the system evolves.

**Discussion**:
In standard quantum theory, non-local correlations exhibited in entangled systems seem perplexing. When two particles interact and become entangled, measuring one particle instantly affects the other, even when separated by large distances. This leads to correlations that appear to violate locality in space, with information seemingly transmitted faster than light. 

The usual interpretation is that entangled particles maintain some kind of non-local connection or "shared state" even when spatially separated. But the mechanism behind how they coordinate in this non-local way remains unclear in conventional quantum theory.

The Active Time Hypothesis provides an alternative conceptual perspective - rather than a spatial non-local link between particles, the non-locality may be temporally engendered. Time itself, through its proposed generative and directive capabilities, may actively induce quantum entanglements by configuring particles into shared states in a non-local manner.

In this view, time is responsible for establishing the correlations, with its intrinsic coordination properties entangling particles independent of space. Quantum measurement collapses could reflect time operating unhindered across space, instantly affecting entangled states. 

The non-local quantum effects may thus arise from time's ability to act non-locally, spontaneously and coherently placing particles into correlated joint states. This reimagining of temporal agency could provide new angles when theorizing about perplexing quantum phenomena.

While standard quantum theory proposes spatial non-local connections to explain correlations in entanglement, the Active Time Hypothesis suggests time itself as the coordinating agent acting non-locally to generate such correlations. Formalizing and testing these ideas could uncover new insights on the nature of quantum non-locality.


## 8. Visualization

The visualizations offer a consolidated view of both classical and quantum dynamics. 

In the **upper subplot**:
- The red curve represents the evolution of $`\Phi(t)`$, a classical parameter. The fluctuating nature of $`\Phi(t)`$ is evident, highlighting the stochasticity in the system. The pronounced spikes showcase the occasional strong perturbations introduced by the stochastic function $`S(t)`$.

In the **lower subplot**:
- The blue curve illustrates the entanglement entropy of the quantum system over time. It provides a means to comprehend the quantum correlations present in the system. The entropy's variations indicate periods where the system experiences a higher degree of entanglement and other moments where this entanglement diminishes.

The juxtaposition of these plots underscores the integrative nature of the simulation, bridging the classical and quantum realms. The dynamics captured here present a rich tapestry of phenomena, opening avenues for further exploration in understanding the interplay between stochastic classical dynamics and quantum entanglement.

![Plot1](https://github.com/maherabdelsamie/Active-Time-Hypothesis/assets/73538221/b4d63294-9670-463d-ba30-106139cf1c69)


---

## Conclusion:

In this study, we ventured into the uncharted territory of the Active Time Hypothesis (ATH), a perspective that positions time not as a passive observer, but an active participant influencing the cosmos. Our dual-simulation approach, bridging classical and quantum realms, illuminated the profound implications of such a temporal agency.

The classical simulations showcased the unpredictable nature of phenomena influenced by time's generative property. This spontaneity, combined with the directive and adaptive properties, challenges our conventional understanding of causality, determinism, and linear temporal flow.

On the quantum frontier, the entanglement entropy dynamics revealed potential modifications to quantum correlations under the ATH. This raises intriguing questions: Could quantum non-locality be a manifestation of time's inherent non-local agency rather than spatial connections? Could time itself, with its generative and directive capabilities, be the orchestrator of quantum entanglements?

---

 # Installation
The simulation is implemented in Python and requires the following libraries:
- numpy
- matplotlib

You can install these libraries using pip:

```
pip install numpy
pip install matplotlib
```

### Usage
Run the simulation by executing the `main.py` file. You can modify the parameters of the simulation by editing the `main.py` file.

```
python main.py
```
## Run on Google Colab

You can run this notebook on Google Colab by clicking on the following badge:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/13S4-HLKC7k4KLPHdVIBQbkyOA4fVJ7NH?usp=sharing)

## License
This code is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. - see the LICENSE.md file for details.

## Citing This Work

If you use this software in your research, please cite it using the information provided in the `CITATION.cff` file available in this repository.
