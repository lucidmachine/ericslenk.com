{:title "Personal Goals Review - 2019-06-20", :date "2019-06-20", :tags ["2019" "goals" "review"], :description "Review of progress toward my personal goals from 2019-06-02 to 2019-06-20."}


# Goals
* **Relationships:** I've had a lot of opportunities for growth this past month. I've learned some humbling things about myself and have some personal and emotional skills to develop. On the upside I've been in touch with my family and a handful of friends.
* **Career:** I'm back to learning Clojure with [Clojure for the Brave and True](https://www.braveclojure.com/clojure-for-the-brave-and-true/). And I have some schemes about a project for which Clojure might be a good fit. Or a terrible fit! Time will tell.
* **Health and Longevity:** I'm finally seeking proactive healthcare. I also started running again, which was exhausting but good. And I got to squeeze in a couple bike rides with friends! *AND* I finally finished assembling one of my ergonomic keyboards! 
* **Financial Independence:** Looks like we've been spending an inordinate amount this month. Oof.

# Habits
## Leave Work on Time
I left my log at the office. -_-  But experientially, this has been going okay. The auto-logout successfully caused me to call it quits, and I've largely been home before 6pm for the past 2 weeks. I think more than anything this is because my workload has finally let up, as the project we've been grinding at for the entire 2nd quarter is pretty much done. I'm happy to report that we haven't - as far as I can tell so far - overcommitted ourselves this coming quarter.

### Habit
* Trigger(s): Computer and phone reminders at 4:00pm, computer and phone reminders and auto-close computer communication apps at 4:30pm, auto-logout at 5:00pm. Record leave time and the reason I left when I did.
* Action(s): Stop current task. Close email and chat applications. Work on an easy task.

## Bedtime Routine
I've gone to bed mostly at reasonable hours, but the rest of the ritial's been... spotty. No packing clothes, no tea, no reading, no logging bed times. I think over time the practice has transformed a bit. I still reliably grab a beverage of some type on my way to bed, which is good. I pack for the day ahead... most of the time? Part of my challenge here is that I've fallen off of reading things. I haven't had the books I'm working through in the right places at the right time, and when my wife comes to bed with me she often asks me to turn out the light before I've even started. Maybe a bedside lamp's in order.

### Habit
* Trigger(s): Dinner.
* Action(s): Stop what I'm doing. Pack for the next day. Brush my teeth. Grab a tasty beverage. Log my bedtime. Read in bed. Go to sleep.

## Financial Reviews
I actually remembered to do this! I think that means incorporating financial review into my personal review was a good trigger. Plus, I have better insight when writing about my Financial Independence goal.

* Trigger(s): Personal Goals Review.
* Action(s): Update transaction log in Mint. Obtain high-level overview.

# Projects
## Hardware BitClock
There have been some setbacks in this project since I last wrote. For starters, there were a couple shorts in the display circuit, which took me several hours to find and fix.

Then there's the software. At first I wrote some driver software in TypeScript with Johnny Five. It was a blast. But when I finally got it up and running I was dismayed to find that it just wasn't looping through the LED matrix fast enough to achieve the persistence of vision of effect necessary. Instead it had this incessant flicker which literally hurt to look at. I was afraid if a person with photo sensitive epilepsy had looked at it they'd be at risk. So now I've rewritten the whole thing in C. And it displays arbitrary BitTimes/ matrices just fine - no flicker!

But then there's the matter of timekeeping. I finally installed a [DS3231 real time clock (RTC) module](https://learn.adafruit.com/adafruit-ds3231-precision-rtc-breakout/overview) in the circuit. But it doesn't seem to be working off board power? And I didn't have any batteries on hand, and it turns out that nobody in my city actually *sells* the particular type required for the RTC module I bought. So the whole project came to another screeching halt while I waited for the [CR1220](https://www.adafruit.com/product/380) batteries to ship.

## Iris Mechanical Keyboard(s)
Once the bikes I needed finished were finished and the hardware BitClock ground to a halt I dusted off my old mechanical keyboard project. Back in November or December I started assembling some [Keebio Iris](https://keeb.io/products/iris-keyboard-split-ergonomic-keyboard?variant=7431310573598) split mechanical keyboards, partially for fun, partially because I think I'm developing repetitive stress injuries in my right hand. I ordered and received some keycaps and a couple other odds and ends and finally finished assembling a complete set! This took a lot of time and hard lessons, but I'm so proud and pleased with the results that I'll give this project a full write-up soon. After using it for a week at work I'm happy to report that it's quite comfortable, and my hand seems less tense and painful!

## Update Primary Care Physician
Speaking of repetitive stress injuries, I'm finally getting off my ass about seeing a doctor. I'm old enough that it's frankly embarassing, but I haven't made a proactive appointment for myself... ever. So I spent a couple days getting the right papers and accounts in order and sought a new primary care physician. Unfortunately I didn't even get to searching with my health insurer for a physician until Friday afternoon, and it turns out that every candidate physician on my list has short hours on Fridays. Better luck Monday, I guess.