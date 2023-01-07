# Conconi test audio file creation
This repo provides the utilities to create audio files (.wav) for performing the Conconi Test [[1]](#1).

The initial speed and end speed can be specified (in km/h).
There will be a beep every 25th meter, and every 200m the speed is increased by 0.5km/h, which coincides with a higher toned beep.

For more info:
```
python -m create_audio_file -h
```

## Example
```
python -m create_audio_file --start_speed 12 --end_speed 22
```

## Available audio files
[Conconi 10km/h](conconi_10kph.wav)<br>
[Conconi 12km/h](conconi_12kph.wav)<br>
[Conconi 14km/h](conconi_14kph.wav)

## References
<a id="1">[1]</a>
Conconi F, Ferrari M, Ziglio PG, Droghetti P, Codeca L.
Determination of the anaerobic threshold by a noninvasive field test in runners.
J Appl Physiol Respir Environ Exerc Physiol. 1982 Apr;52(4):869-73. doi: 10.1152/jappl.1982.52.4.869. PMID: 7085420.
