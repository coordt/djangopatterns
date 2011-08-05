=========================================
My Development Assumptions and Principles
=========================================

by Corey Oordt

Since I started developing in Django in 2006, I've been lucky enough to meet and work with many talented people with a variety of experiences. Gradually, typically through failure or dire need, we developed a methodology and approach to development of projects.

The approach was internalized; each of us *knew* how it worked so it was never directly expressed. With a recent move to a new job, I was struck by the differences and needed to express the ideas in terms of **assumptions** and **principles**. 

*Assumptions* are the preconceptions you and your team hold when approaching a project. These assumptions aren't necessarily bad. As long as you are aware of them, and regularly check to make sure they are valid, they will be helpful. 

*Principles* are the guides to behavior. They are not hard and fast rules that you must never break, merely guides to success that should be understood and deviated from with full knowledge of why it makes sense in the situation.

Key Design Assumptions
======================

No two projects are alike.
**************************

Each project will share some things with others, but not all projects will share the same things, or in the same way. You will need to listen to the needs of the end users and the people running the project.

Most projects will fail
***********************

It should fail quickly, with as little effort as possible to determine its imminent doom. This is not a pessimism, but innovation. The easier it is to try something to see if it works, the more you will try and the more that will work.

People have their own way of doing things.
******************************************

I'm an opinionated bastard. As an opinionated bastard, it really torques me when others make me do things in ways I disagree with. When there are several ways to get the same result, let others get there by any of those means.

Another way to look at this is to manage *outcomes,* not practices or methods.

Two or more project's requirements may conflict.
************************************************

The conflicts only matter if the projects must share something or are co-dependent.


Things change.
**************

Life moves very fast on the internet. Projects must adapt quickly or fail miserably.


Key Design Principles
=====================

Design the user's experience first
**********************************

Many developers create solutions that are functional, but not usable. When you start with the user's experience, you at least get more usable solutions, if not better ones.

Break down the tools to their simplest bits.
********************************************

It is easier to find new uses for simple tools than complex tools. I am constantly surprised how people have found new ways to use code that was meant for something else.

Similar ideas are:

* Separate functionality whenever possible.

* Be flexible in implementation.

* Couple loosely.

Code is like a making a baby: only do it if you are willing to support it for the rest of your life.
****************************************************************************************************

I've learned the hard way that code you wrote years ago can come back to haunt you. I've received calls from people I wrote code for years before asking for help due to an unforeseen bug. (To me the unforeseen bug was that they were still using the software.) Unless you are willing to be a jerk, you got to give them a hand.

This leads to two practices: use external code libraries whenever possible to reduce the amount of code for which you are directly responsible, and write your code in a way that you won't be too horrified to see it in three years.

A similar practice is when making a utility to enhance functionality, don't assume that the implementer will "own the code".

External dependencies should be declared and few
************************************************

I see dependencies like farts on an elevator: the fewer the better (and please confess).

If you want people to do something, make it incredibly easy to do.
******************************************************************

And don't forget its sibling: *If you want people to do something a specific way, make it easier to do it that way than any other.*

Even small barriers will limit how often "best practices" are followed. People put off things if:

* They have to do prep work to accomplish the task

* They aren't sure how to accomplish the task

* They don't understand why the task is important


