[[COMP23412]]

[[user interface design]] covered the different techniques available and why a user interface design can be useful - this part aims to cover guidelines for actually creating your own user interface designs

there are many guideline sets for creating user interface designs

## Ben Shneiderman's 8 Golden Rules

1. ==Strive for consistency - using the same fonts, colour pallets==

sites like amazon use consistency to trick users - it becomes difficult to notice that to avoid trying prime for free you actually just need to click the 'Continue' button rather than the big Try Prime FREE button which sticks out to you

2. ==Seek universal usability==
The following things should be taken into account when designing the user interface:
==Users==:
- Abilities
- Age
- Skills
==Devices==:
- Technology being used
- Wearable > Mobile > Desktop > Large display
==Situations==:
- Bad connection
- On the move
- Weather
- Stress / emotional condition  - minimal things like how much text being displayed on the screen

3. Offer informative feedback
When notifying the user about certain things in your app, you should say ==why== this thing happened, and any possible next steps. This should all be done with the ==right tone==. These notifications should aim to not just explain things to developers, but to regular users as well

4. Design dialogues that bring closure
Whenever a certain task is completed (i.e. order been made), be sure to ==affirm== this to the user in a way which cannot be misinterpreted

5. Prevent errors
Simple examples include not allowing a user to select a date range which goes back in time, DOBs from the future. Ideally, these should not just return an error, but ==not be selectable by the user in the first place==

6. Permit easy reversal of actions (==universal undo==)
Certain websites like amazon actually prevent this, and this is an example of [[dark patterns]] - it isn't straightforward to remove something from your cart if you're about to pay for it, in the hope that you just order it anyways

7. Keep users in control
Information shown to users should be what they requested - no more, no less

8. Reduce short-term memory load
This can be things like decluttering user interfaces, not displaying huge amounts of information to the user when they perform some action, removing certain fields which might not be compulsory