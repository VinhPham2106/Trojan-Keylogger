<div align="center">
<h1>Trojan-Keylogger</h1>
<img src="https://nordvpn.com/wp-content/uploads/blog-featured-keylogger-945x496-1.svg" width="300">
  
Image's source: https://nordvpn.com/blog/keylogger-protection/
</div>

## Disclaimer!
The author assumes no reponsibility for any illegal actions performed using code from this project. This project is purely for educational purpose.

## Overview
The hypothetical scenario is that the victim uses this app for trojan purpose, like chatbot, play music, etc... The keylogger program runs on the background, recording keys typed and send the list of keys to the attacker's server using HTTP. The attacker would analyze the received data in hopes of getting passwords or spying on the victim. Again, this project is purely for educational purpose.

## Components
- **Main**: The plaintext python program that pretends to do something while silently does keylogging using the 'keyboard' module. All interaction of the 'os' module is silenced, and the logged result is sent to the attacker.
- **Obfuscated_main**: Same with the main, except malicious codes are obsfucated to cover the real intention (hopefully).
- **Server**: simple http.server implementation that grabs the data sent from the victim machines. When all is done, it writes everything to an output file. It does use functions from the analytics files to handle special keys like 'ENTER', 'BACKSPACE', 'SPACE', copy paste sequence.
- **Analytics**: Provide functions that analyze the list of keys and make it easier to infer what the victim was doing.
- **Keylogging_Scanner**: Test if a software-based keylogger is currently running, essentially a counter-measure. Under development.

## Attacker's mindset and explanation of choices
I've seen many keylogger implementations send the data through SMTP, Google Drive API, ... However, I wanted to make the process *simple*, *lightweight* while remaining *stealthy*. So I came up with this idea of using simple HTTP requests. 

You probably wonder how does the networking part work outside the localhost context. My approach is to use the *cloudflared tunnel*, which makes your server accessible most of the time. There's probably alternatives for cloudflared tunnel of HTTP is our flavor, I'm very open to suggestion.

*Can someone on the victim side attack the attacker's server?* I think they can. I'll try to look into the victim side and try to secure the attacker's server. Sound so wrong huh?

## Testing
So far this works on Windows 11 and Kali Linux. Bitdefender doesn't pick this up. I'll try to test this on Mac and different Linux distro. Let me know if this does not work on your end, we'll try to see what happen. 

## Further development
Any feedback on how to mature this project is welcomed. Again, this is for educational purpose only. I'm trying to figure out how to take this keylogger to a stealthier, lower level like C or hardware. 

## About the author
I'm a cybersecurity enthusiast trying to work on fun, explorative projects in my freetime, trying to get into a hacker's mindset.
