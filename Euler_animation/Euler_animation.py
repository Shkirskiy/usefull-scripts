import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.gridspec import GridSpec

# For Jupyter Lab animation display
from IPython.display import HTML
from matplotlib import rc
rc('animation', html='jshtml')

# Parameters
f = 0.2  # Frequency in Hz
omega = 2 * np.pi * f  # Angular frequency
T = 10               # Total time (2 seconds)
dt = 0.01           # Time step
t = np.arange(0, T, dt)  # Time vector

# Set up the figure and axes
fig = plt.figure(figsize=(10, 5))
fig.suptitle(f'Animation of a Rotating Vector at {f} Hz', fontsize=16)
gs = GridSpec(1, 2)

# Phasor plot (left side)
ax_phasor = fig.add_subplot(gs[0, 0])
ax_phasor.set_aspect('equal')
ax_phasor.set_xlim(-1.5, 1.5)
ax_phasor.set_ylim(-1.5, 1.5)
ax_phasor.set_xlabel('Real')
ax_phasor.set_ylabel('Imaginary')
ax_phasor.set_title('Rotating Vector (Phasor)')
ax_phasor.grid()

# Add thick black x and y axes
ax_phasor.axhline(0, color='black', linewidth=2)
ax_phasor.axvline(0, color='black', linewidth=2)

# Add a circle to represent the path
circle = plt.Circle((0, 0), 1, color='blue', fill=False)
ax_phasor.add_artist(circle)

# Time domain plot (right side)
ax_time = fig.add_subplot(gs[0, 1])
sinusoid = np.sin(omega * t)
ax_time.plot(t, sinusoid)
ax_time.set_xlim(0, T)
ax_time.set_ylim(-1.5, 1.5)
ax_time.set_xlabel('Time (s)')
ax_time.set_ylabel('Amplitude')
ax_time.set_title('Time Domain Signal')

# Add thick black x and y axes to time-domain plot
ax_time.axhline(0, color='black', linewidth=2)
ax_time.axvline(0, color='black', linewidth=2)

# Initialize the lines and points for animation
line_phasor, = ax_phasor.plot([], [], 'r-', linewidth=2)
point_phasor, = ax_phasor.plot([], [], 'ro')
line_time_point, = ax_time.plot([], [], 'ro')

# Add projection lines for both x and y axes in both plots
projection_phasor_x, = ax_phasor.plot([], [], 'r--', linewidth=1)  # Projection on x-axis
projection_phasor_y, = ax_phasor.plot([], [], 'r--', linewidth=1)  # Projection on y-axis
projection_time_x, = ax_time.plot([], [], 'r--', linewidth=1)  # Projection on x-axis (time-domain)
projection_time_y, = ax_time.plot([], [], 'r--', linewidth=1)  # Projection on y-axis (time-domain)

def init():
    """Initialize the animation."""
    line_phasor.set_data([], [])
    point_phasor.set_data([], [])
    line_time_point.set_data([], [])
    projection_phasor_x.set_data([], [])
    projection_phasor_y.set_data([], [])
    projection_time_x.set_data([], [])
    projection_time_y.set_data([], [])
    return (line_phasor, point_phasor, line_time_point, 
            projection_phasor_x, projection_phasor_y, 
            projection_time_x, projection_time_y)

def animate(i):
    """Update the animation at each frame."""
    current_time = i * dt
    if current_time >= T:
        current_time %= T  # Loop back to start

    # Update the phasor (rotating vector)
    angle = omega * current_time
    x_phasor = [0, np.cos(angle)]
    y_phasor = [0, np.sin(angle)]
    line_phasor.set_data(x_phasor, y_phasor)
    point_phasor.set_data([x_phasor[1]], [y_phasor[1]])  # x and y need to be sequences

    # Update the projections in the phasor plot
    projection_phasor_x.set_data([x_phasor[1], x_phasor[1]], [0, y_phasor[1]])  # Vertical projection on x-axis
    projection_phasor_y.set_data([0, x_phasor[1]], [y_phasor[1], y_phasor[1]])  # Horizontal projection on y-axis

    # Update the point on the time domain plot
    x_time = current_time
    y_time = np.sin(omega * current_time)
    line_time_point.set_data([x_time], [y_time])  # x and y need to be sequences

    # Update the projections in the time domain plot
    projection_time_x.set_data([x_time, x_time], [0, y_time])  # Vertical projection on y-axis (time domain)
    projection_time_y.set_data([0, x_time], [y_time, y_time])  # Horizontal projection on x-axis (time domain)

    return (line_phasor, point_phasor, line_time_point, 
            projection_phasor_x, projection_phasor_y, 
            projection_time_x, projection_time_y)

# Create the animation
ani = animation.FuncAnimation(
    fig,
    animate,
    frames=int(T / dt),
    init_func=init,
    interval=dt * 1000,
    blit=True
)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to accommodate suptitle

# Display the animation in Jupyter Lab
ani

# Save the animation as an MP4 file
ani.save('rotating_vector_animation_with_full_projections.mp4', writer='ffmpeg', fps=30)
