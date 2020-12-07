# Python Note Generator


I scraped the notes and their frequencies from the web.
Used **Selenium** for this process in the `init.py`

You can find the frequencies and wave lengths of all the notes on
https://pages.mtu.edu/~suits/notefreqs.html
<br>
## Requirements

If you **only** want to generate notes, you don't have to set anything up.
`winsound` package is **already in** Python.

**However**, if you want to see how the program scrapes the data, you will need to install this packages:

```
pip install pandas
pip install selenium
```
Then, you must install the driver for your browser from [**here**](https://selenium-python.readthedocs.io/installation.html#drivers).

Finally, make sure that the driver you've downloaded is in your [**PATH**](https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7). If you don't want to add the path of the driver to the **PATH** variable it would be enough that the driver is in the same directory with `init.py`

<br>

## Notes
- The program starts generating from `37Hz` due to the `Beep` function of `winsound`. <br> The notes that has lower frequency than `37Hz` are **not supported**.
  <br>
- Normally, the frequencies of notes were decimal numbers. However, the `Beep` function again does **not supports** float numbers. That's why I set the frequencies as integers. Don't worry though, you will not hear the difference.

<br>

## TODOs

  **The features are not ordered by priority. One may be removed or one may be added.**
- [x] Scrape the data from web with `Selenium`
- [x] Generate the notes with `winsound`
- [ ] Add time values of notes and a metronome
- [ ] Get input from user
- [ ] Make a loop system
- [ ] Visualize it! - Graphical User Interface with `PyQt5` or `Tkinter`
- [ ] Add Major and Minor scales for each note
