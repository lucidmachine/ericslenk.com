Title: Personal Goals Review - 2019-02-23
Date: 2019-02-23
Category: 
Tags: 2019, goals, review
Summary: Review of progress toward my personal goals for 2019-02-08 to 2019-02-23.
Status: published 


# Goals
* **Relationships:** I made it out to a few social events, which were great. A party here, a date there, [DemoCamp Lansing](http://www.democamplansing.com/) over yonder. That said, I'd like to spend more quality time with people next fortnight. 
* **Career:** Not a whole lot of wins to speak of on the career front. I'm continuing to learn more about Angular as I migrate AngularJS code, but frankly we're catching up to the rest of the world in this respect. I experienced a few setbacks in personal projects, too. I somehow uninstalled the entire networking stack on my gaming rig. Taking the time to fix the dang thing derailed development and writing I had planned.
* **Health and Longevity:** My shoulder feels better this fortnight, but I have no idea why. Still haven't seen a medical professional. And I don't think I rode my bike at all aside from commutes.
* **Financial Independence:** I am, for the first time in my adult life, **WORTH A POSITIVE AMOUNT OF DOLLARS!** I'm still figuring out what my role is in the management of my family's finances at this point. We've curbed a bit of impulse spending, but I think I need to get back into habitually actively managing our accounts and I really didn't prioritize this or attempt to establish any habits about it.

# Habits
## Leave Work on Time
This has gone poorly for a few reasons. First, my team at work has been pair/trio/mob programming on all of the feature development we've done over the past fortnight. Mob programming has plenty of advantages, but when you're all collectively working on a problem it can be unpalatable to say "hey, it's 4pm and I think we should just drop it." Plus, the odds are that I'll be looking at somebody *else's* screen when the reminders go off on *my* computer. I've set a corresponding series of reminders on my phone to sort of work around the problem of not looking at my computer while the reminders go off. As for getting the team to stop, I'll just have to get used to it and trust that they want to go home as much as I do.

Second, I took it upon myself to make wide-ranging updates to our team's frontend code alone. Since I elected to do so alone I've been doing this work at times the team isn't mob programming - in the late afternoon. This effort is nearly complete, so the issue will sort of resolve itself in short order. But I will do the remaining work in the early morning, before our team begins programming. If I don't get to work on time to do migration work, so be it. At least I'll have my sanity.

Finally, I've just realized that my computer didn't automatically log me out at 5pm yesterday like it's supposed to... I'll look into that.

### Updated Habit
* **Trigger(s):** **Computer and phone** reminders at 3:30pm, **computer and phone reminders** at 4:00pm, **computer and phone reminders and auto-close computer** communication apps at 4:30pm, auto-logout at 5:00pm.
* Action(s): Stop current task. Close email and chat applications. Fill out work log. GTFO.

## Personal Goals Reviews
This post is a day late for a couple reasons. For one, I didn't have the right tools at the right times to write the post. I remembered that I had to write this post early yesterday morning at work - well before the post was due, but well after I had the opportunity to pack my personal laptop and bring it to work. This has been a problem before, but I managed to work around it the past few times. I think the requirement that I write these posts on my personal laptop is a real hindrance here, so I'm going to start a project, Easier Blog Publication, to work around that. I always have access to my personal phone and keyboard in the office, so I'm going to see if I can retool my blogging setup to allow for writing and publication from my phone.

The second reason was that my work day was especially mentally exhausting and especially long, so by the time I left the office I was a wreck. I got home late and passed out on the couch and by the time I felt remotely okay it was like 8pm. I pushed this post off until today to just take care of myself for the rest of the night. I've increased the priority of Leave Work on Time to address this, as it's really a problem of violating that boundary.

## Bedtime Routine
At least *this* habit's still on track! I've been digging mint tea and re-reading William Gibson's Bridge trilogy. I finished the first book in the trilogy, [Virtual Light](https://amzn.to/2MXEv0I), and am well into the second, [Idoru](https://amzn.to/2Xk7NLV).

## Financial Reviews
Our family's finances have slipped, and I've been asked to take back some of the active management responsibilities. To get started I'll take a couple hours every other week to just categorize some transactions and get a high-level overview of our finances. I'm going to let the trigger be a calendar reminder and see if involving my wife adds enough social pressure to make it effective.

### New Habit
* **Trigger(s): Calendar Reminder.**
* **Action(s): Update transaction log in Mint. Obtain high-level overview.**


# Projects
## Converting to TypeScript
I published [an article on declaring interfaces in TypeScript]({filename}/blog/converting-to-typescript-declaring-interfaces.md) in [the Converting to TypeScript mini-series]({tag}typescript). This is still going pretty well, and I'm still learning a bunch.

## Emulation Box
I'm writing a couple tutorials based on the setup of my emulation box soon, so keep an eye out for those. I sort of accidentally borked my Steam Machine a little while back, so I took a weekend and change to rebuild it. It's now based on [Xubuntu 18.04](https://xubuntu.org/) and [RetroPie](https://retropie.org.uk/), and I wrote some scripts and some config files so that it can detect and launch all of my Steam games from [EmulationStation](https://emulationstation.org/) along side my ROM collection. I'm just *so* pleased with how it turned out. While I'm at it I might take the opportunity to write a bit more about video game emulation, who knows?

## Easier Blog Publication
Presently my blogging setup looks like:

* Writing: Markdown and IntelliJ IDEA - I don't need a full IDE for this, but it meets many of my other needs as well.
* Building: Pelican, several Pelican packages, Python 3, Make
* Preview: Pelican, several Pelican packages, Python 3, Make - This is the same as building, as the process is literally building the site and running it on a local development server.
* Version Control: Git and Github
* Publication: Pelican, Python 3, Make, rsync, and one big-ass password (no crypto keys, too lazy I guess?)
* Publication Scheduling: Me, a human, who does not always like or remember to publish content early in the morning before work

This has served me pretty well until now, but I would love to be able to draft posts on my phone, on a different computer, etc. to give myself more flexibility. Requiring that the local device build, preview, and publish the site's content has proven to be a real impediment to this. I'm also going to try to figure out how to push content ahead of time and have it publish at a given future date. I think I could do this right now with Pelican if I had an automated daily process which rebuilt and re-published the site from my Github repo, but I don't, so I can't. I'll re-evaluate my writing and site development needs and work toward meeting those expanding needs.

