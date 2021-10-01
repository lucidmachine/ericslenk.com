{:title "Personal Goals Review - 2019-07-22", :date "2019-07-22", :tags ["2019" "goals" "review"], :description "Review of progress toward my personal goals from 2019-06-20 to 2019-07-22."}


# Goals
* **Relationships:** I got to catch up with a lot of people at Blissfest, but otherwise have not been very sociable.
* **Career:** I worked through another chapter of [Clojure for the Brave and True](https://www.braveclojure.com/clojure-for-the-brave-and-true/).
* **Health and Longevity:** I've run into some obstacles selecting a primary care physician. Turns out there is a lot of paperwork I don't want to do, and also once I file all that stuff I'll probably be on a waiting list for 6 weeks. I began reading [Back Care Basics by Mary Pullig Schatz](https://www.penguinrandomhouse.com/books/551660/back-care-basics-by-mary-pullig-schatz-foreword-by-william-connor-preface-by-b-k-s-iyengar/9780962713828/) to work on my weak back and see if that helps with the discomfort in my shoulder, but progress has been slow. I also finished my second split ergonomic mechanical keyboard - just after accidentally ripping the microUSB port off one of the first keyboard's microcontrollers!
* **Financial Independence:** Well Astral and I got approved for a car loan with fairly generous terms but I've no idea where the extra money for a car payment and mandatory full-coverage auto insurance is supposed to come from so I'm kind of freaking out a bit and also fuck cars I don't even want a car? We want to buy a house soon, too, but I *super* don't want to take on two loans at once.


# Habits
I've been reading through [Atomic Habits by James Clear](https://jamesclear.com/atomic-habits) and I've redone the structure of these habits to align with Clear's cue, craving, response, reward pattern.

## Leave Work on Time
I've decided to stop tracking my leave times as it's annoying and doesn't really provide much value. I'm also going to try cutting back to just 1 cue here - the rest are unnecessary complications.

I think my fundamental problem here is that I have this implicit belief that working a bit late to get Important Things done is a noble sacrifice that an effective person makes. I understand logically that this is a) wrong and b) fucked up, but I need to figure out how to *feel* otherwise. I'm trying to construct a mental model of the sort of person who I can admire that also leaves work on time and then use that as a role model instead. I'll check back in on this next time. Also I think I'm gonna try some classical training sort of reward for when I leave the office before 5:00pm.

### Habit
* Cue: Computer and phone reminders and auto-close computer communication apps at 4:30pm, auto-logout at 5:00pm.
* Response: Stop current task. Log work for the day and set tomorrow's agenda. Pack up and walk out that damn door.
* Reward: If I've left on time, grab a snack from the snack bar on my way out. Bask in all that free time I've clawed back to enjoy life.

## Bedtime Routine
This has gone much better save for reading in bed. I think I just need to elect another light reading book - all of my current books are technical or self-help. Also, I'm not gonna log this time anymore either, time tracking your actual life sucks.

### Habit
* Cue: Dinner's finished.
* Response: Pack for the next day. Brush my teeth. Grab a tasty beverage. Read in bed. Go to sleep.
* Reward: Read a fun book and drink a tasty beverage.

## Financial Reviews
Stacking this habit with the personal review habit continues to be a hit. Looking at this habit through the Atomic Habits lens, though, I realize that my short-term "reward" for this habit is just sort of... anxiety? And when I review with Astral she often panics. Also, working through our entire transaction log before getting an overview of our financial standing doesn't exactly "make it easy." It might be better to spin transaction fixing into a separate habit. And maybe this could be made more rewarding if we could measure positive impact of our active finance management? I'm going to punt on these for now since I haven't the time or energy, but those changes are probably necessary at some point.

* Cue: Personal Goals Review.
* Response: Update transaction log in Mint. Review budgets.
* Reward: Anxiety, panic.

# Projects
## Hardware BitClock
The batteries I was waiting on shipped, I finished my software rewrite, and the whole thing is *working*! However, I hate the physical layout. It's an Arduino Uno, the LED matrix board, a breadboard, and the RTC module, all just sort of... near each other? Connected by jumper wires. And I am struggling to figure out how to compact the design, or even how to care enough about this project to do so. I think a second revision with a different board layout and a smaller microcontroller is in order, honestly. I'm considering learning to design PCBs and ordering a small batch, but that sounds like a lot of effort for a project that's become a slog.

## Iris Mechanical Keyboards
I've been using my first keyboard at work for a couple weeks now and I really enjoy it. I'm up to speed with most of my keystrokes at this point, and I've really come to appreciate its reprogrammability and flexibility. I'm also fixing some bad typing habits I didn't realize I had. I'm well pleased that retraining myself has gone so smoothly.

And I built my second keyboard! I added sockets for the microcontroller headers on this one to make microcontroller service and replacement loads easier. The second build went very smoothly

But also, I broke my first keyboard. That was a major bummer. I accidentally ripped the microUSB port off of one of the microcontrollers. And I really dread the work to fix it. The last time I had to replace that keyboard's microcontrollers I had to clip the headers of each microcontroller and then desolder all of the keys before desoldering each individual header pin remnant, dropping in new microcontrollers, and re-soldering all of the keys and headers. That's redoing 152 solder joints, folks. It was a *huge* pain in the ass. This time I'm going to try to learn to desolder all of the headers at once with a heat gun to avoid messing with the 112 key joints. And once I get that microcontroller out I am *definitely* retrofitting this board with microcontroller sockets.

## Update Primary Care Physician
Well I found a physician and went to their office but I was given a huge packet of forms to fill out and told that once I filed that packet they'd probably call me back in 6 weeks so... Not great. I'm nearly done with the paperwork but having this drag out into a multi-week project has been demoralizing. I just want a routine checkup and a consultation about my sore shoulder.