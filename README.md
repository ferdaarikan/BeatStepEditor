# BeatStepEditor

This is not official software, just a small script that maybe useful to others. Use at your own risk. You need to be comfortable with reading and writing device memory using the official software otherwise this script won't be useful.

This script allows easy editing of Arturia Beatstep midi mappings. Arturia Beatstep supports selection of scales in ```SEQ``` mode. 
**Midi Control Center** allows entering any notes for pads for ```CNTRL``` mode however user interface is not ideal for editing, especially for multiple programs 1-16.

I didn't add editing the notes in ```SEQ``` mode as it is already relatively easy using the official software.

**Warning** Midi Control Center does not like manual editing of .beatstep files due to the way they handle the file format. There is a high chance that you can break it, though this does not pose any risk to hardware. This script generates outputs that are compatible with the software.

## BeatStep Pad Layout

![image](https://github.com/ferdaarikan/beatstep-remote/assets/13984102/58e9b1eb-f866-40b6-94eb-67609df67b41)

<sub>image credit: [MusicMatter](https://www.musicmatter.co.uk)</sub>

||||||||| 
|-----|-----|-----|-----|-----|-----|-----|-----|
|Pad 1|Pad 2|Pad 3|Pad 4|Pad 5|Pad 6|Pad 7|Pad 8|
|Pad 9|Pad 10|Pad 11|Pad 12|Pad 13|Pad 14|Pad 15|Pad 16|


## Usage

You need to export your current settings as .beatstep file using ***Midi Control Center***. You can use the ```before.beatstep``` file in the repository to test the script. 

```map_pads.py --config after.beatstep --map dorian4.json --out dorian4.beatstep```

```--config``` parameter is the starting configuration. Obtain this file by exporting a memory bank using ***Midi Control Center***

```-map``` parameter specifies the scale definition. A scale is represented in json format where keys are pad numbers and values are the notes
including octave information such as ```C1``` or ```C#2``` and so on. Both ```#``` and ```b``` are supported in notes and they just modify whatever the note is. 
So even ```B#3``` is a valid entry.

```--out``` specifies the name of the output file after pad mappings are applied.

Once you run the script you can import the generated .beatstep file into ***Midi Control Center*** and write to a memory bank using ```Store To``` button.

### Exporting Current Settings
Connect to your hardware using ***Midi Control Center***. Select a device memory and click ```Recall From```. This will read the memory from hardware once completed you can click ```File > Export ``` to obtain the .beatstep file.


## Scale Definitions
Here scale is any combination of 16 notes in any octave that will be mapped to Arturia BeatStep pads to use in CNTRL mode. You can find some scale files in the repository. If you need the same scale in different octaves since octave 
information is fixed in the scale definitions you need to create multiple maps.
