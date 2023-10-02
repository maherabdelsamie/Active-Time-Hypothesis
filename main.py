import numpy as np
import matplotlib.pyplot as plt


# =================== CLASSICAL SIMULATION =================== #

def S_func(t):
    return np.random.randn() * 0.5 + (np.random.rand() < 0.005) * 10

def G_func(Phi, t):
    return -0.05 * Phi

def A_func(Phi):
    return 0.1 * Phi

def simulate_phi(T, delta_tau, Phi_0, S_function, G_function, A_function):
    n_steps = int(T / delta_tau)
    Phi = np.zeros(n_steps)
    Phi[0] = Phi_0
    t_values = np.linspace(0, T, n_steps)

    for i in range(n_steps - 1):
        t = t_values[i]
        Phi[i+1] = Phi[i] + delta_tau * (1 + A_function(Phi[i])) * (S_function(t) + G_function(Phi[i], t))

    return t_values, Phi

# =================== QUANTUM SIMULATION =================== #

def runge_kutta_evolution(psi, H, dt):
    k1 = -1j * dt * np.dot(H, psi)
    k2 = -1j * dt * np.dot(H, psi + 0.5 * k1)
    k3 = -1j * dt * np.dot(H, psi + 0.5 * k2)
    k4 = -1j * dt * np.dot(H, psi + k3)
    return psi + (k1 + 2*k2 + 2*k3 + k4) / 6

def entanglement_entropy(rho):
    eigenvalues = np.linalg.eigvals(rho)
    eigenvalues = eigenvalues[eigenvalues > 0]
    return -np.sum(eigenvalues * np.log2(eigenvalues))

def simulate_ATH_evolution_qutrit(psi, H_A, H_B, S_t_values, T, dt):
    states = [psi]
    times = np.arange(0, T, dt)
    
    for idx, t in enumerate(times):
        f = S_t_values[idx]
        H_ATH = f * np.kron(np.diag([1, 0, -1]), np.diag([-1, 0, 1]))
        H_total = H_A + H_B + H_ATH
        psi_new = runge_kutta_evolution(psi, H_total, dt)
        states.append(psi_new)
        psi = psi_new
    
    return times, states

# =================== ENHANCED DRIVER FUNCTION =================== #

def run_unified_sim_advanced(params):
    T = params.get("T", 10)
    delta_tau = params.get("delta_tau", 0.01)
    Phi_0 = params.get("Phi_0", 0)
    dt = params.get("dt", 0.01)
    psi = params.get("psi", np.kron(np.array([1, 0, 0], dtype=complex), np.array([1, 0, 0], dtype=complex)))
    H_A = params.get("H_A", np.kron(np.diag([1, 2, 3]), np.eye(3, dtype=complex)))
    H_B = params.get("H_B", np.kron(np.eye(3, dtype=complex), np.diag([1, 2, 3])))
    
    assert T > 0, "T must be positive"
    assert delta_tau > 0, "delta_tau must be positive"
    assert dt > 0, "dt must be positive"
    
    t, Phi = simulate_phi(T, delta_tau, Phi_0, S_func, G_func, A_func)
    S_t = [S_func(val) for val in t]
    
    times, states = simulate_ATH_evolution_qutrit(psi, H_A, H_B, S_t, T, dt)
    entropies_qutrit = [entanglement_entropy(np.outer(state.conj(), state)) for state in states[:-1]]
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    ax1.plot(t, Phi, color='red', label='Φ(t) (Classical)')
    ax1.set_ylabel('Φ(t)')
    ax1.legend(loc='upper right')
    ax1.set_title('Classical Evolution of Φ(t)')
    ax2.plot(times, np.real(entropies_qutrit), color='blue', label='Entanglement Entropy (Quantum)')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Entanglement Entropy')
    ax2.legend(loc='upper right')
    ax2.set_title('Quantum Entanglement Entropy')
    
    fig.tight_layout()
    plt.show()
    
    return t, Phi, times, np.real(entropies_qutrit)

# =================== INITIALIZE QUANTUM VARIABLES =================== #

psi_A_qutrit = np.array([1, 0, 0], dtype=complex)
psi_B_qutrit = np.array([1, 0, 0], dtype=complex)
psi_AB_qutrit = np.kron(psi_A_qutrit, psi_B_qutrit)
H_A_qutrit = np.kron(np.diag([1, 2, 3]), np.eye(3, dtype=complex))
H_B_qutrit = np.kron(np.eye(3, dtype=complex), np.diag([1, 2, 3]))

# =================== UPDATED PARAMETER DICTIONARY =================== #

simulation_params = {
    "T": 10,
    "delta_tau": 0.01,
    "Phi_0": 0,
    "dt": 0.01,
    "psi": psi_AB_qutrit,
    "H_A": H_A_qutrit,
    "H_B": H_B_qutrit
}

# To run the simulation, use:
_ = run_unified_sim_advanced(simulation_params)
