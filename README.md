# Python Note Generator

<hr>

I scraped the notes and their frequencies from the web.
Used **Selenium** for this process in the `init.py`

You can find the frequencies and wave lengths of all the notes on
https://pages.mtu.edu/~suits/notefreqs.html

## Note

- The program starts generating from `37Hz` due to the `Beep` function of `winsound`. <br> The notes that has lower frequency than `37Hz` are **not supported**.
  <br>
- Normally, the frequencies of notes were decimal numbers. However, the `Beep` function again does not supports float numbers. That's why I set the frequencies as integers. Don't worry though, you will not hear the difference.
