import wave
import struct
import math

# Set the parameters for the WAV file
nchannels = 1  # Number of channels
sampwidth = 2  # Sample width (in bytes)
framerate = 8000  # Frame rate
# Set the parameters for the beep
frequency = 3000  # Frequency of the beep (in Hz)
duration = 0.15  # Duration of the beep (in seconds)


def _get_beep_interval_time(speed: float) -> float:
    """Get the time (in seconds) needed to cover 25m at the given speed (in km/h)."""
    beep_distance = 0.025  # 25m, in km
    return (beep_distance / speed) * 3600


def _get_beep_samples(sound_frequency: int) -> list:
    samples = []
    for i in range(int(framerate * duration)):
        value = int(32767.0 * math.sin(sound_frequency *
                    math.pi * float(i) / float(framerate)))
        samples.append(value)
    return samples


def _get_speed_samples(speed: float) -> list:
    samples = []
    time_for_25m = _get_beep_interval_time(speed)
    silence_time = time_for_25m - duration
    for i in range(8):
        sound_frequency = frequency * 1.5 if i == 0 else frequency
        samples += _get_beep_samples(sound_frequency)
        samples += [0] * int(framerate * silence_time)
    return samples


def _get_samples(start_speed: float, end_speed: float) -> list:
    speed = start_speed
    samples = []
    while speed < end_speed:
        samples += _get_speed_samples(speed)
        speed += 0.5
    return samples


def _create_audio_file(file_name: str, samples: list):
    # Create a WAV file
    wavefile = wave.open(file_name, "w")
    wavefile.setparams((nchannels, sampwidth, framerate,
                        len(samples), "NONE", "not compressed"))

    # Write the samples to the WAV file
    wavefile.writeframesraw(struct.pack("h" * len(samples), *samples))

    # Close the WAV file
    wavefile.close()


def create_conconi_audio(file_name: str, start_speed: float = 10.0, end_speed: float = 23.0):
    samples = _get_samples(start_speed, end_speed)
    _create_audio_file(file_name, samples)
