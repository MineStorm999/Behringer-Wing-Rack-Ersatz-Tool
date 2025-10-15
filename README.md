# Behringer Wing Sessions Replacement

## Usage
- Like the Official Live Sessions Programm converts .wavs to usable multi channel .wavs for the XLive slot from the Wing Series. (X32 not tested)
- Workflow
    - First Time only:
        - Windows:
            - RunFirstTime.bat
        - MacOS:
            - RunFirstTime.command
            - IF you get an error, because mac does not trust the file:
                - go to System Settings > Privacy & Security > click open anyway
        - Linux:
            - make shure that python and tkinter are installed
    - Create ONE MultiChannel .wav with up to 32 channels, and in 32bit PCM format (use e.g. Audacity).
    - Start converter:
        - Windows:
            - RunFirstTime.bat
        - MacOS:
            - RunFirstTime.command
            - IF you get an error, because mac does not trust the file:
                - go to System Settings > Privacy & Security > click open anyway
        - Linux:
            - run RunProgramm.sh
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

## Usage Terms
Consider sending me an email or just Star the Repo, if you are actually using it. Otherwise it's MIT License so do what you want with it. Also I do not take any responsibility