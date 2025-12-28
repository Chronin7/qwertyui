## Install Prerequisite (MacOS)

### Install XCode Libraries

Use the following code to install the `xcode` dependencies needed for install `pygame`.

```zsh
xcode-select --install
```

### Install needed packages

If you don't have homebrew installed, install it. Instructions can be found [here](https://docs.brew.sh/Installation).
Use the following command to install `pygame` dependencies

```zsh
brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf pkg-config
```

### Setup Python Environment

This should only need to be done once unless you delete the `.venv/` directory. From the command line run:

```zsh
python3 -m venv .venv
```

### Load Python Environment

From the terminal run:

```zsh
source .venv/bin/activate
```

### Install Python Dependencies

From the terminal run:

```zsh
pip install -r requirements.txt
```
