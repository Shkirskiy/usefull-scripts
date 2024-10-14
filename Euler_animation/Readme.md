# Rotating Vector Animation

This code generates an animation using **Matplotlib** that illustrates a rotating vector (phasor) alongside its corresponding sinusoidal waveform in the time domain. The animation demonstrates the relationship between the rotating vector in the complex plane and the real-time sinusoidal signal. You can adjust the frequency and save the animation as a **GIF** or **MP4**.

## Usage

1. Run the script to generate the animation.
2. Modify the save options to output either a GIF or MP4 file.

```python
# Save as GIF
ani.save('rotating_vector_animation.gif', writer='imagemagick')

# Save as MP4
ani.save('rotating_vector_animation.mp4', writer='ffmpeg')
```
