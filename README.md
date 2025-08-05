# Behringer Wing Sessions Replacement

## Usage
- Like the Official Live Sessions Programm converts .wavs to usable multi channel .wavs for the XLive slot from the Wing Series. (X32 not tested)
- Workflow
    - First Time only: Run: RunFirstTime. (bat(win) / command(mac os))
    - Create ONE MultiChannel .wav with up to 32 channels, and in 32bit PCM format (use e.g. Audacity).
    - Run RunProgramm. (bat(win) / command(macos))
    - Select Your Multi Channel .wav
    - Select Your Output Folder 
    - Write a Name
    - Convert
    - Wait until completion

## Reasons
The official Wing Live Sessions Software didn't work every time, thus not usable for stage performances.

## Bugs
- In MacOS the used tkinter UI doesn't work properly:
    - Design insn't used at all
    - You cant see Lables and Text inputs(but you can use them)