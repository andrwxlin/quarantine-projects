# coronavirus-projects
During the COVID-19 pandemic, I got bored and decided to do some coding :)

## About the projects

/python
- `discordRPC-beta.py` Basically just my sandbox for Discord Rich Presence applications
- `login.py` A simple little login script using a username and password provided by `credentials.json`
- `pomodoro.py` A script that acts as a timer for the [Pomodoro Technique](https://wikipedia.org/wiki/Pomodoro_Technique). Uses the [`pypresence`](https://github.com/qwertyquerty/pypresence) script to display the timer information as a Rich Presence on your Discord profile
- `sudokuSolver.py` A sudoku board solver using a backtracking algorithm to solve a sudoku board. Followed [this guide](https://www.youtube.com/playlist?list=PLzMcBGfZo4-kE3aF6Y0wNBNih7hWRAU2o) by Youtube channel [Tech With Tim](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg)
- `version-finder.py` A script that finds all songs in a Spotify playlist (Uses [`spotipy`](https://github.com/plamere/spotipy) to connect to Spotify API) that has the string "` ver`" in its title. Exports all those song titles + artists to a .csv file (Uses [`pandas`](https://pandas.pydata.org/)) with the desired path+name.
- `zoom.py` A script that prompts the user for the meeting topic, then displays that as a Discord Rich Presence.