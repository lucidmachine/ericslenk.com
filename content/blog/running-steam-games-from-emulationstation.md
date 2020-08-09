Title: Running Steam Games from EmulationStation
Date: 2019-03-04
Category: 
Tags: emulationstation, steam, emulation, frontend, linux, bash, roms
Summary: Configure EmulationStation to browse your Steam collection alongside your very legally emulated console classics.
Status: published


[EmulationStation](https://emulationstation.org/) is a controller-friendly, graphical, themeable, flexible, open-source application for browsing and launching your games. If you want one unified place to look through your game library and figure out what the heck to play this evening, then this is your app! Its bread and butter is launching ROMs on emulators, but with a bit of configuration it will handle your Steam collection alongside your very legally emulated console classics. This walkthrough will get your Steam games into your EmulationStation collection. It's written to use Linux scripts and commands, but should translate to macOS or even Windows with a bit of careful thought.

# 0. Get EmulationStation
If you don't have EmulationStation yet I highly recommend using the [RetroPie](https://retropie.org.uk/) fork of EmulationStation and the whole RetroPie ecosystem. It's a wonderful project. Get started with the [RetroPie setup tool](https://github.com/RetroPie/RetroPie-Setup).

# 1. Install Steam Games
Step number one is to grab some games to surface. Go [download the Steam client](https://store.steampowered.com/about/) if you don't already have it. Then use Steam to install a game or two. Launch one of those games to make sure everything's working fine before you move on.

# 2. Create Game Shortcuts
Now we need to make something that EmulationStation can open for us. We'll be building desktop shortcut files - specifically [XDG Desktop Entries](https://standards.freedesktop.org/desktop-entry-spec/latest/). Now, you can ask the Steam client to build these for you, but that method has a couple down sides. For starters, you must ask this per game at install time. Second, it will only place them on your user's desktop, and if you have a habit of collecting hundreds more games than you could ever possibly play this can wreak havoc on your otherwise pristine desktop.

Instead, we're going to do things the hard way and build them all at once with a shell script! You can [download the whole Steam games import script from my Github repo](https://raw.githubusercontent.com/lucidmachine/bin/master/import-steam-games.sh). If you want to learn how this script works, read the next section. If you don't, skip ahead to [the usage section](#usage).
can [download the whole Steam games import script from my Github
repo](https://raw.githubusercontent.com/lucidmachine/bin/master/import-steam-games.sh). If you want
to learn how this script works, read the next section. If you don't, skip ahead to [the usage
section](#usage).

## 2.a importsteamgames.sh - The Long Way
To begin, we point the script to a few important directories.

```bash
readonly ROMS_DIR="${HOME}/RetroPie/roms"
readonly OUTPUT_DIR="${ROMS_DIR}/steam"
readonly STEAM_APPS_DIR="${HOME}/.steam/steam/steamapps"
```

`ROMS_DIR` is the directory where your ROM subdirectories live. RetroPie assumes this is `${HOME}/RetroPie/roms`, so I've used that by default. Change it if you want your Steam shortcuts directory built elsewhere. `OUTPUT_DIR` defines the directory which the script will build and fill with .desktop files, by default the `steam` subdirectory of the `ROMS_DIR` directory. `STEAM_APPS_DIR` is the directory where your Steam apps live. Steam defines this as `"${HOME}/.steam/steam/steamapps"` by default, so it's probably still there.

Now to get into the meat of it. 

```bash
if [[ -d "${OUTPUT_DIR}" ]]; then
    rm -r "${OUTPUT_DIR}"
fi
mkdir -p "${OUTPUT_DIR}"
```

If the target output directory currently exists we're going to nuke it and recreate it to start from scratch every time.

```bash
app_manifest_names=$(ls "${STEAM_APPS_DIR}" | grep "${STEAM_MANIFEST_EXT}")
```

Then we search your Steam apps directory for app manifest files, which are files whose name ends in '.acf'.

```bash
for app_manifest_name in ${app_manifest_names}; do
    app_manifest_path="${STEAM_APPS_DIR}/${app_manifest_name}"
    app_id=$(getManifestProperty "${app_manifest_path}" '"appid"')
    app_name=$(getManifestProperty "${app_manifest_path}" '"name"')
    xdg_desktop_file_path="${OUTPUT_DIR}/${app_name}.desktop"
    xdg_desktop_file_contents=$(xdgDesktopTemplate "${app_id}" "${app_name}")

    echo "${xdg_desktop_file_contents}" > "${xdg_desktop_file_path}"
    chmod 755 "${xdg_desktop_file_path}"
done
```

For each and every manifest we found we're going to read the "appid" and "name" properties out of the file, use the ID and name to generate the contents of a XDG .desktop file, then write those contents to a file for this specific app in the target output directory. Phew!

You might note that a couple non-trivial operations were glossed over there. Those have been extracted into separate functions, which we'll cover now.

```bash
function getManifestProperty() {
    local app_manifest_path="$1"
    local property_name="$2"

    echo $(
        grep "${property_name}" "${app_manifest_path}" \
        | rev \
        | cut -f 1 \
        | rev \
        | sed -e 's/"//g'
    )
}
```

In order to get a property from a manifest we use `grep` to search for the property name in the manifest file. Then we do some post-processing, because `grep` outputs an entire line which looks like this:

```bash
> grep "name" appmanifest_105600.acf 
	"name"		"Terraria"
```

We use `rev | cut -f 1 | rev` to get the last string on the line, `"Terraria"`. This works by reversing the whole thing with `rev`, using `cut -f 1` to get the *first* string on the line, `"airarreT"`, and reversing it with `rev` one more time. The very last bit, `sed -e 's/"//g'`, removes all `"` characters, turning `"Terraria"` into `Terraria`. Now THAT we can use.

The final piece of the puzzle is using our parsed out properties to build .desktop file contents.

```bash
function xdgDesktopTemplate() {
    local app_id="$1"
    local app_name="$2"

    cat <<EOF
[Desktop Entry]
Name=${app_name}
Comment=Play this game on Steam
Exec=steam steam://rungameid/${app_id}
Icon=steam_icon_${app_id}
Terminal=false
Type=Application
Categories=Game;
EOF
}
```

This is just one big [HEREDOC](http://tldp.org/LDP/abs/html/here-docs.html) with our app ID and name passed in and injected in the appropriate places. Everything between `<<EOF` and `EOF` is the template. The template itself is copied from one of those Desktop files Steam will create for you if you ask it nicely.

<h2 id="usage">2.b importsteamgames.sh - Usage</h2>
Now that you've downloaded my Steam games import script to `~/bin/importsteamgames.sh` go ahead and run that bad boy.

```bash
> ~/bin/importsteamgames.sh
> ls ~/RetroPie/roms/steam
Anodyne.desktop
Bastion.desktop
...
Undertale.desktop
XCom: Enemy Unknown.desktop
```

Nice.

# 3. Add Steam to EmulationStation
Generating all those .desktop files is only half the battle. Now we need to tell EmulationStation how to use those suckers. We'll need to open the configuration file `es_systems.cfg` to add a new system for our Steam games. It might live at `/etc/emulationstation/es_systems.cfg` or at `/opt/retropie/configs/all/emulationstation/es_systems.cfg`. Once you've got it open, add this stanza to the file.

```xml
<system>
    <name>steam</name>
    <fullname>Steam</fullname>
    <path>/home/yourusername/RetroPie/roms/steam</path>
    <extension>.desktop</extension>
    <command>xdg-open %ROM%</command>
    <platform>pc</platform>
    <theme>steam</theme>
</system>
```

This tells emulationstation that there's a new system called `steam` which it should present to humans as `Steam` whose games live in `/home/yourusername/RetroPie/roms/steam`. Be sure to change that to whatever directory you put your .desktop files in earlier. Those game files will have names that end in `.desktop`, and when EmulationStation wants to run one it will run `xdg-open` on the selected game file. `xdg-open` will in turn open up that .desktop file, read the line `Exec=steam steam://rungameid/${app_id}`, and ask steam to run the game with the target app ID. EmulationStation -> XDG -> Steam. The platform line tells any metadata scrapers that when they search for a game in this folder they should search for PC games. The theme line tells EmulationStation that if a theme supports Steam it should use that part of the theme for this system's collection.

Now you should be able to launch your Steam games from EmulationStation! But we're not quite done yet.

# 4. Install an EmulationStation Theme with Steam Support
After going through all that trouble to build your Steam collection in EmulationStation you're gonna want a theme that supports it! There are plenty of themes which have special icons and assets just for Steam, so go get you one. My personal favorite is [pixel-metadata](https://github.com/ehettervik/es-theme-pixel-metadata). If you're running RetroPie you can run the setup script and find it in the theme library.

![pixel-metadata gamelist screen](https://raw.githubusercontent.com/wetriner/es-theme-gallery/master/pixel-metadata-gamelist.png)

# 5. Scrape Game Metadata
The last piece of the puzzle here is to go and grab metadata for your Steam games. Just run your EmulationStation scraper of choice here, same as for the rest of your systems. Now you can happily scroll through all of your games in one place!

**DONE.**
