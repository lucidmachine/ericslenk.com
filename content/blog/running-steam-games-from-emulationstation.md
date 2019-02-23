Title: Running Steam Games from EmulationStation
Date: 2019-02-25
Category: 
Tags: emulationstation, steam, emulation, frontend, linux, roms
Summary: Configure EmulationStation to browse your Steam collection alongside your very legally emulated console classics.
Status: draft


[EmulationStation](https://emulationstation.org/) is a controller-friendly, graphical, themeable, flexible, open-source application for browsing and launching your games. If you want one unified place to look through your game library and figure out what the heck to play this evening, then this is your app! Its bread and butter is launching ROMs on emulators, but with a bit of configuration it will handle your Steam collection alongside your very legally emulated console classics. This walkthrough will get your Steam games into your EmulationStation collection. It's written to use Linux scripts and commands, but should translate to macOS or even Windows with a bit of careful thought.

# 0. Get EmulationStation
If you don't have EmulationStation yet I highly recommend using the [RetroPie](https://retropie.org.uk/) fork of EmulationStation and the whole RetroPie ecosystem. It's a wonderful project. Get started with the [RetroPie setup tool](https://github.com/RetroPie/RetroPie-Setup).

# 1. Install Steam Games
Step number one is to grab some games to surface. Go [download the Steam client](https://store.steampowered.com/about/) if you don't already have it. Then use Steam to install a game or two. Launch one of those games to make sure everything's working fine before you move on.

# 2. Create Game Shortcuts
Now we need to make something that EmulationStation can open for us. We'll be building desktop shortcut files - specifically [XDG Desktop Entries](https://standards.freedesktop.org/desktop-entry-spec/latest/). Now, you can ask the Steam client to build these for you, but that method has a couple down sides. For starters, you must ask this per game at install time. Second, it will only place them on your user's desktop, and if you have a habit of collecting hundreds more games than you could ever possibly play this can wreak havoc on your otherwise pristine desktop. Instead, we're going to do things the hard way and build them all at once with a shell script!

```bash
```

[] TODO: explain the script.

Now go ahead and run that bad boy.

```bash
> ./bin/scrape_steam_games.sh
> cd ~/RetroPie/roms/steam && ls
Anodyne.desktop
Bastion.desktop
...
VVVVVV.desktop
XCom: Enemy Unknown.desktop
```

Nice.

# 3. Add Steam to EmulationStation
Generating all those .desktop files is only half the battle. Now we need to tell EmulationStation how to use those suckers. We'll need to open the configuration file `es_systems.cfg` to add a new system for our Steam games. It might live at [] or at []. Once you've got it open, add this stanza to the file.

```xml
```

[] TODO: explain the stanza

Now you should be able to launch your Steam games from EmulationStation! But we're not quite done yet.

# 4. Install an EmulationStation Theme with Steam Support
After going through all that trouble to build your Steam collection in EmulationStation you're gonna want a theme that supports it! There are plenty of themes which have special icons and assets just for Steam, so go get you one. My personal favorite is [Pixel by Rookervik](https://github.com/RetroPie/es-theme-pixel). If you're running RetroPie you can run the setup script and find it in the theme library.

# 5. Scrape Game Metadata
The last piece of the puzzle here is to go and grab metadata for your Steam games. Just run your EmulationStation scraper of choice here, same as for the rest of your systems. Now you can happily scroll through all of your games in one place!

**DONE.**
