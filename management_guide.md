# Guide to Managing NIAC Events
## Introduction
This document aims provide some guidance to new executive officers of the NIAC. 
Anything discussed here is merely a suggestion and the only rules to be followed are written in the [constitution](https://www.nexusformat.org/NIAC.html).

## Teleconference
1. Choose a date
   * Hopefully had some agreement on a general timeframe (e.g. start, middle or end of next month) at the end of the previous meeting.
   * Make an online poll (using e.g. [Strawpoll](https://strawpoll.com/)) so that people can vote on their preferred dates.
   * Send an email to the nexus-committee and nexus-tech lists advertising the poll and give a deadline for voting.
   * Add a link to the poll in the minutes of the previous meeting.
   * After the deadline, select a specific date. This must be emailed to the nexus-committee and nexus-tech lists and it is good to include a link to the agenda page (see below) and attach a calendar item (see below). It is good to occasionally remind everyone that they can add items to the meeting agenda.
2. Create Zoom Meeting
   * Log in to your Zoom account
   * Create a new meeting:
      * Be very careful about the time zone - use UTC! Also take care during the times when daylight savings are beginning and ending.
      * Make the security settings very low, we haven't yet had any problem with unwanted people crashing the meeting, but you should try to make it possible for the meeting to still happen if you don't show up to host it.
         * (yes) Passcode
         * (no) Waiting room
         * (no) Require authentication to join
         * (yes) Allow participants to join anytime (this is hidden under "options")
      * Just "Computer audio" is enough, no need to include telephone audio.
      * Adding an "alternative host" can be good, though it might be limited to only people within the same organisation, which is notvery useful in our case.
   * Double check the details of Zoom invitation (because mistakes are embarrasing!) and keep the page open so that you can copy the details into the wiki page (next step)
   * Save the calendar file (`.ics`) to be attached to an announcement email.
4. Add agenda page to the wiki
<BR>The web site is constructed from files in the [`wiki` repository](https://github.com/nexusformat/wiki/tree/master/content). The list of teleconferences (and links to each agenda page) is kept in [`Teleconferences.md`](https://github.com/nexusformat/wiki/blob/master/content/Teleconferences.md) while the individual meeting agenda pages have file names of the form `Telco_YYYMMDD.md`.
   * Create a new `Telco_YYYMMDD.md` file substituting the correct date.
   * Copy the contents of the agenda page for the previous meeting (use the "raw" view in the web interface), paste into the new file and adjust as appropriate.
   * Add the details of the Zoom meeting.
   * Save/commit the new file and its contents.
   * Edit the `Teleconferences.md` page to include a link to the new meeting agenda page.
   * Wait a few minutes and then check that the [served Teleconferences page](https://www.nexusformat.org/Teleconferences.html), the added link and the new meeting agenda page are all working correctly. 
5. Send announement email to the nexus-committee and nexus-tech lists, including:
   * Date and time of the meeting.
   * link to the meeting agenda page.
   * Attach the calendar `.ics` file.
   * If special guests have been invited to join the meeting, then make sure they also receive the email.
6. At the meeting you should have one person running the meeting (i.e. leading the discussions) and another person taking minutes.
7. After the meeting, post the minutes on the agenda page you created earlier (i.e. `Telco_YYYMMDD.md`). Then, go back to step #1 to start setting up the next meeting.
## Membership Vote
Membership on the NIAC expires after [a term of 3 years](https://www.nexusformat.org/Membership_Dates.html). New (or renewing) members require a nomination letter from their facility/organisation.
1. Send an email to the nexus-committee list asking everyone to to vote to accept the new member on the NIAC. (Remember to give a deadline.)
2. Once the deadline has passed, check that the majority has voted to accept the new member.
3. Send another email to the nexus-committee list giving the result.
4. If the member is accepted:
  * update the [NIAC membership list](https://github.com/nexusformat/wiki/blob/master/content/NIAC.md)
  * update the [expiration dates list](https://github.com/nexusformat/wiki/blob/master/content/Membership_Dates.md)
  
