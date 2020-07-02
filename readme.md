# Synth AI

## Plan
### Stage 1: Basics
- Generate background pads, play melody over it
- Create graph of chord sequence biases
- Generate melodies, control cutoffs, etc
- Use this to build song structure: intro, verse, chorus, etc
- Create cli to use interactivley
- DL extract top notes and bass notes from piano track, send to 2 modular LFOs

### Stage 2: Intermediate
- Choose between different melody types and sounds
- Various midrange instrument types
- High instrument additions
- Variations on background pad
- Add cutoff interpolations

### Stage 3: Advanced
- Use true AI techniques
 - Use ML to choose melody/chord note list that match emotional coloring on 2d plane
 - Use z3 to pick chord patterns
 - Add additional melody contraints based on genre
 - Use z3 to pick melody note combinations
 - Use z3 to pick melody patterns
 - Use z3 to alter melodies to fit chords
 - Use z3 to relate note speed and release time
 - ML could generate several note sequences, z3 modulates them to be as similar as possible, still with chord
 - Use fluid simulators to give melodies/transitions more "flow"
 - Use google interpolate for transitions
 - z3 solve which instruments to use based on placement in sonic space

### Stage 4: Visuals
- Transfer to dedicated computer (dell laptop)
- Add [spectrum visualizer](https://www.amazon.com/Nobsound-1424-Analizador-espectro-fidelidad/dp/B014KLRU9I/ref=sr_1_8?dchild=1&keywords=spectrum+visualizer&qid=1593227841&sr=8-8) or [DIY one](https://create.arduino.cc/projecthub/shajeeb/32-band-audio-spectrum-visualizer-analyzer-902f51)
- Add colored background lighting, set with ableton
- New camera with bokeh
- Blue front lighting, red back lighting

### Stage 5: Upload
- Automatically record video, sync with audio and upload to YouTube
- Add log output to youtube comment, video, or description
- Generate and upload sheet music
- Upload midi files
- Generate patch list and description

---

## General
- Generate youtube videos each day/week, automatically upload them to youtube and website
- Have an intensity value over time that everything adjusts to.
- Pull synth presets from git repository folders
- Use https://github.com/ideoforms/pylive
- Leave running overnight Friday, will record videos for entire week, upload to youtube, then shut down
- Layer output log semi-transparent over video
- Generate sheet music/midi files for upload
- Script audacity with python, generate paulstretched pads
- Feed song through iZotope to isolate drums, melodies, vocals, etc. Generate synth patch based on this information, automatically cover that song.
- AI/mathy module generates arps based on input pitches for key and chord

## Lead line
- Use 1 moog mother 32's for main melody
- Send MIDI to moog, start with random notes, eventually learn melodies based on melody banks or from playing
- Add actuators to moog so Ableton can change filter parameters
- Vibrato option
## Countermelody
- Randomly choose one of the omnisphere hardware options
- Could be like blade runner synth
- Could be more stabbing, plucking repetitive sound
## Background pad
- First generate background pad, run through paulstretch. Choose pad sound from one of several patches
## Bass
- Choose one from several bass patches. Choose whether or not to include based on intensity
- Could have glide or not
- Could be be an arp or not
## Middle arp
- 25% chance to be in song
- Could always fade in and out
- One of several patches
- Like the classic omnisphere arp patch
- Choose from several patches
- Choose whether single not or switch back and forth
- May or may not follow chords
## High arps
- 25% chance to be in song
## FX
- Add sweeps and hits
- Add light kick parts
## Other
- Random tempo each time

pydoc live
# Synth AI

## Plan
### Stage 1: Basics
- Generate background pads, play melody over it
- Create graph of chord sequence biases
- Generate melodies, control cutoffs, etc
- Use this to build song structure: intro, verse, chorus, etc

### Stage 2: Intermediate
- Choose between different melody types and sounds
- Various midrange instrument types
- High instrument additions
- Variations on background pad
- Add cutoff interpolations

### Stage 3: Advanced
- Use true AI techniques
 - Use ML to choose melody/chord note list that match emotional coloring on 2d plane
 - Use z3 to pick chord patterns
 - Add additional melody contraints based on genre
 - Use z3 to pick melody note combinations
 - Use z3 to pick melody patterns
 - Use z3 to alter melodies to fit chords
 - Use z3 to relate note speed and release time
 - ML could generate several note sequences, z3 modulates them to be as similar as possible, still with chord
 - Use fluid simulators to give melodies/transitions more "flow"
 - Use google interpolate for transitions
 - z3 solve which instruments to use based on placement in sonic space
 - Make z3 maximize various symmetry classifications for melodies

### Stage 4: Visuals
- Transfer to dedicated computer (dell laptop)
- Add [spectrum visualizer](https://www.amazon.com/Nobsound-1424-Analizador-espectro-fidelidad/dp/B014KLRU9I/ref=sr_1_8?dchild=1&keywords=spectrum+visualizer&qid=1593227841&sr=8-8) or [DIY one](https://create.arduino.cc/projecthub/shajeeb/32-band-audio-spectrum-visualizer-analyzer-902f51)
- Add colored background lighting, set with ableton
- New camera with bokeh

### Stage 5: Upload
- Automatically record video, sync with audio and upload to YouTube
- Add log output to youtube comment, video, or description
- Generate and upload sheet music
- Upload midi files
- Generate patch list and description

---

## General
- Generate youtube videos each day/week, automatically upload them to youtube and website
- Have an intensity value over time that everything adjusts to.
- Pull synth presets from git repository folders
- Use https://github.com/ideoforms/pylive
- Leave running overnight Friday, will record videos for entire week, upload to youtube, then shut down
- Layer output log semi-transparent over video
- Generate sheet music/midi files for upload
- Script audacity with python, generate paulstretched pads
- Use machine learning insturment isolation, and midi generation, to feed data to ai auto-cover
- Use ML transcription to build dataset of ambient piano pieces, use this to train ambient piano model

## Lead line
- Use 1 moog mother 32's for main melody
- Send MIDI to moog, start with random notes, eventually learn melodies based on melody banks or from playing
- Add actuators to moog so Ableton can change filter parameters
- Vibrato option
## Countermelody
- Randomly choose one of the omnisphere hardware options
- Could be like blade runner synth
- Could be more stabbing, plucking repetitive sound
## Background pad
- First generate background pad, run through paulstretch. Choose pad sound from one of several patches
## Bass
- Choose one from several bass patches. Choose whether or not to include based on intensity
- Could have glide or not
- Could be be an arp or not
## Middle arp
- 25% chance to be in song
- Could always fade in and out
- One of several patches
- Like the classic omnisphere arp patch
- Choose from several patches
- Choose whether single not or switch back and forth
- May or may not follow chords
## High arps
- 25% chance to be in song
## FX
- Add sweeps and hits
- Add light kick parts
## Other
- Random tempo each time

pydoc live

