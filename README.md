# compatibility-app
#### A light-hearted Flask app that tells you how compatible your crush is!!

DISCLAIMER - This app is by no means an indicator of real compatibility and is purely for entertainment purposes ONLY.

I've been dabbling around with HTML and Flask to create interactive apps and part of that process has led me to create a simple way to assess one's compatibility with another individual in different ways,
- Numerology
- Moon Phases

#### How does it work?

The Numerology route takes you and your crush's names and finds the index of each letter in your names. Your compatibility score is a percentage score of the difference in the sum of indexes of both names, over the total sum of indexes for both names. It's all in the math!!

The Moon Phase route analyzes the moon phase on each of your birthdays. I've done this by working with the <code>ephem</code> library in Python, which is a popular module used in many astrological analyses. It enumerates the moon phase on a given date, eg - New Moon = 0 and Full Moon = 1. Taking the phases on both birthdays, the compatibility score is calculated based on the sum of each phase and how close they are to 1.

