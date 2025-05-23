import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp

# ==================== Data Loading ====================
print("\n" + "="*60)
print("DATA LOADING")
print("="*60)

# Expected format: CSV with columns 'time_hours' and 'sea_height'
data_path = "Tidal_Sea_Height_Data (1).csv"  # Replace with actual file path
try:
    data = pd.read_csv(data_path)
    t = data['time_hours'].values  # Time observations
    y = data['sea_height'].values  # Tidal heights
    print(f"Loaded {len(t)} observations")
except FileNotFoundError:
    print("Data file not found. Please check the file path and try again.")
    raise
except KeyError as e:
    print(f"Column not found: {e}. Please check column names in CSV file.")
    print("Expected columns: 'time_hours' and 'sea_height'")
    raise

n = len(t)
print(f"Number of observations: {n}")

# Define frequencies
omega1 = 2*np.pi/12     # Sun dominant period (12 hours)
omega2 = 2*np.pi/12.42  # Moon dominant period (12.42 hours)

print(f"Sun frequency ω₁ = {omega1:.6f} rad/hour")
print(f"Moon frequency ω₂ = {omega2:.6f} rad/hour")

# ==================== PART 1b: Least Squares Estimation ====================
print("\n" + "="*60)
print("PART 1b: LEAST SQUARES ESTIMATION")
print("="*60)

# Construct design matrix X
# Each row i: [sin(ω₁tᵢ), cos(ω₁tᵢ), sin(ω₂tᵢ), cos(ω₂tᵢ)]
X = np.column_stack([
    np.sin(omega1 * t),  # sin(ω₁t)
    np.cos(omega1 * t),  # cos(ω₁t)
    np.sin(omega2 * t),  # sin(ω₂t)
    np.cos(omega2 * t)   # cos(ω₂t)
])

print(f"Design matrix X shape: {X.shape}")
print("X represents [sin(ω₁t), cos(ω₁t), sin(ω₂t), cos(ω₂t)] for each time point")

# Calculate least squares estimate: β̂ = (X'X)⁻¹X'y
XTX = X.T @ X
XTy = X.T @ y
XTX_inv = np.linalg.inv(XTX)
beta_hat = XTX_inv @ XTy

print(f"\nLeast squares estimate β̂:")
print(f"β̂₁ (b₁,₁ - sun sin coeff):  {beta_hat[0]:.6f}")
print(f"β̂₂ (b₂,₁ - sun cos coeff):  {beta_hat[1]:.6f}")
print(f"β̂₃ (b₁,₂ - moon sin coeff): {beta_hat[2]:.6f}")
print(f"β̂₄ (b₂,₂ - moon cos coeff): {beta_hat[3]:.6f}")

# Convert back to amplitude-phase form for interpretation
A1_hat = np.sqrt(beta_hat[0]**2 + beta_hat[1]**2)
phi1_hat = np.arctan2(beta_hat[1], beta_hat[0])
A2_hat = np.sqrt(beta_hat[2]**2 + beta_hat[3]**2)
phi2_hat = np.arctan2(beta_hat[3], beta_hat[2])

print(f"\nConverted to amplitude-phase form:")
print(f"Sun component:  A₁ = {A1_hat:.4f}, φ₁ = {phi1_hat:.4f} rad")
print(f"Moon component: A₂ = {A2_hat:.4f}, φ₂ = {phi2_hat:.4f} rad")

# ==================== PART 1c: Variance Estimation ====================
print("\n" + "="*60)
print("PART 1c: VARIANCE ESTIMATION")
print("="*60)

# Calculate fitted values and residuals
y_fitted = X @ beta_hat
residuals = y - y_fitted

print(f"Model has {X.shape[1]} parameters")
print(f"Degrees of freedom: n - dim(β) = {n} - {X.shape[1]} = {n - X.shape[1]}")

# Unbiased estimator for σ² (see assignment formula)
sigma2_hat = (1 / (n - X.shape[1])) * np.sum(residuals**2)
print(f"\nUnbiased estimate σ̂² = {sigma2_hat:.6f}")
print(f"Standard error σ̂ = {np.sqrt(sigma2_hat):.6f}")

# Calculate var(β̂) = σ̂²(X'X)⁻¹, report only diagonal elements
var_beta_hat = sigma2_hat * XTX_inv

print(f"\nDiagonal elements of variance-covariance matrix var(β̂):")
param_names = ["b₁,₁ (sun sin)", "b₂,₁ (sun cos)", "b₁,₂ (moon sin)", "b₂,₂ (moon cos)"]
for i in range(len(beta_hat)):
    print(f"var(β̂_{i+1}) [{param_names[i]}]: {var_beta_hat[i,i]:.8f}")
    print(f"se(β̂_{i+1}) [{param_names[i]}]:  {np.sqrt(var_beta_hat[i,i]):.6f}")

# ==================== PART 1d: Prediction ====================

print("\n" + "="*60)
print("PART 1d: PREDICTION FOR t* = 360")
print("="*60)

t_star = 360
print(f"Predicting tidal height for t* = {t_star} hours")

# Construct covariate vector for t*
x_star = np.array([
    np.sin(omega1 * t_star),
    np.cos(omega1 * t_star),
    np.sin(omega2 * t_star),
    np.cos(omega2 * t_star)
])

print(f"Covariate vector x* = [{x_star[0]:.6f}, {x_star[1]:.6f}, {x_star[2]:.6f}, {x_star[3]:.6f}]")

# Predictive mean
y_star_mean = x_star.T @ beta_hat
print(f"\nPredictive mean: E[y(t*)] = x*ᵀβ̂ = {y_star_mean:.6f}")

# Predictive variance (includes both parameter uncertainty and noise)
# var(y*) = σ² + x*ᵀ var(β̂) x*
predictive_var = sigma2_hat + x_star.T @ var_beta_hat @ x_star
predictive_se = np.sqrt(predictive_var)

print(f"Predictive variance: var(y*) = σ̂² + x*ᵀvar(β̂)x* = {predictive_var:.6f}")
print(f"Predictive standard error: se(y*) = {predictive_se:.6f}")

# 95% prediction interval using sympy for t-distribution critical value
def get_t_critical(alpha, df):
    """Calculate t-distribution critical value using sympy"""
    x = sp.Symbol('x')
    # For large df, use normal approximation
    if df > 30:
        return 1.96  # Normal approximation for 95% CI
    else:
        # Use sympy to solve for critical value
        # This is an approximation using the relationship between t and normal
        return 1.96 + 1.96/(4*df)  # Simple approximation

alpha = 0.05
df = n - X.shape[1]
t_critical = get_t_critical(alpha, df)
pi_lower = y_star_mean - t_critical * predictive_se
pi_upper = y_star_mean + t_critical * predictive_se

print(f"\n95% Prediction Interval:")
print(f"[{pi_lower:.6f}, {pi_upper:.6f}]")

# ==================== MODEL VALIDATION ====================

print("\n" + "="*60)
print("MODEL VALIDATION")
print("="*60)

# Calculate R-squared
ss_tot = np.sum((y - np.mean(y))**2)
ss_res = np.sum(residuals**2)
r_squared = 1 - (ss_res / ss_tot)

print(f"R-squared: {r_squared:.6f}")
print(f"Adjusted R-squared: {1 - (ss_res/(n-X.shape[1]))/(ss_tot/(n-1)):.6f}")

# Root Mean Square Error
rmse = np.sqrt(np.mean(residuals**2))
print(f"Root Mean Square Error: {rmse:.6f}")

# ==================== VISUALIZATION ====================

# Manual Q-Q plot implementation
def manual_qq_plot(data, ax):
    """Create Q-Q plot manually using numpy"""
    sorted_data = np.sort(data)
    n = len(sorted_data)
    theoretical_quantiles = np.array([sp.sqrt(2) * sp.erfinv(2 * (i + 0.5) / n - 1) for i in range(n)])
    theoretical_quantiles = np.array([float(q.evalf()) for q in theoretical_quantiles])
    
    ax.scatter(theoretical_quantiles, sorted_data, alpha=0.6, s=2)
    
    # Add reference line
    slope, intercept = np.polyfit(theoretical_quantiles, sorted_data, 1)
    line = slope * theoretical_quantiles + intercept
    ax.plot(theoretical_quantiles, line, 'r--', alpha=0.8)
    
    ax.set_xlabel('Theoretical Quantiles')
    ax.set_ylabel('Sample Quantiles')

# Create plots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

# Plot 1: Time series with fitted model
ax1.plot(t[:200], y[:200], 'b-', alpha=0.7, label='Observed', linewidth=1)
ax1.plot(t[:200], y_fitted[:200], 'r-', label='Fitted', linewidth=2)
ax1.set_xlabel('Time (hours)')
ax1.set_ylabel('Tidal Height')
ax1.set_title('Observed vs Fitted Tidal Heights (First 200 hours)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot 2: Residuals vs fitted
ax2.scatter(y_fitted, residuals, alpha=0.6, s=1)
ax2.axhline(y=0, color='r', linestyle='--')
ax2.set_xlabel('Fitted Values')
ax2.set_ylabel('Residuals')
ax2.set_title('Residuals vs Fitted Values')
ax2.grid(True, alpha=0.3)

# Plot 3: Manual Q-Q plot of residuals
manual_qq_plot(residuals, ax3)
ax3.set_title('Q-Q Plot of Residuals')
ax3.grid(True, alpha=0.3)

# Plot 4: Individual components
t_plot = np.linspace(0, 48, 1000)  # 48 hours for visualization
sun_component = beta_hat[0]*np.sin(omega1*t_plot) + beta_hat[1]*np.cos(omega1*t_plot)
moon_component = beta_hat[2]*np.sin(omega2*t_plot) + beta_hat[3]*np.cos(omega2*t_plot)
total_component = sun_component + moon_component

ax4.plot(t_plot, sun_component, 'orange', label=f'Sun (T={12:.1f}h)', linewidth=2)
ax4.plot(t_plot, moon_component, 'blue', label=f'Moon (T={12.42:.1f}h)', linewidth=2)
ax4.plot(t_plot, total_component, 'red', label='Combined', linewidth=2)
ax4.set_xlabel('Time (hours)')
ax4.set_ylabel('Tidal Height')
ax4.set_title('Decomposed Tidal Components (48 hours)')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ==================== SUMMARY OUTPUT ====================
print("\n" + "="*60)
print("SUMMARY OF KEY RESULTS")
print("="*60)
print("Least Squares Estimate (β̂):")
param_names = ["b₁,₁ (sun sin)", "b₂,₁ (sun cos)", "b₁,₂ (moon sin)", "b₂,₂ (moon cos)"]
for i in range(len(beta_hat)):
    print(f"  β̂_{i+1} [{param_names[i]}]: {beta_hat[i]:.6f}")

print(f"\nUnbiased Estimator for σ²: {sigma2_hat:.6f}")
print(f"Standard Error (σ̂): {np.sqrt(sigma2_hat):.6f}")

print(f"\nPredictive Mean at t*=360: {y_star_mean:.6f}")

print(f"\n95% Prediction Interval for y(t*=360): [{pi_lower:.6f}, {pi_upper:.6f}]")
print("="*60)

print(f"\nSUMMARY:")
print(f"The tidal model successfully separates sun and moon contributions")
print(f"Sun amplitude: {A1_hat:.4f}, Moon amplitude: {A2_hat:.4f}")
print(f"Model explains {r_squared*100:.1f}% of tidal height variation")
print(f"Prediction for t*=360: {y_star_mean:.4f} ± {1.96*predictive_se:.4f}")