28/05/25
- Changelog created
- Setting up repository

29/05/25
- Template added
- Playing around with pygame systems
- Decided on window size for game (to keep scaling consistent across devices)
- Wrote empty functions for organization and planning purposes

02/06/25
- Introduction added, bug fixes required
- Assets being worked on
- Started writing into empty functions

03/06/25
- Menu was added with special font
- More bug fixes of introduction
- Added working 'QUIT' button

04/06/25
- Assets resized and edited (Thanks Max!) and uploaded to github
- Introduction fixed
- Fixed transistion from introduction to Menu
- Added menu image and music

05/06/25
- More assets for the game being prepared
- Coded some of the logic for switching between screens
- Switched to a dictionary for storing player states/actions, meaning that functions can now properly access and change the player's available actions based on where they are
- Added a parameter to the night() function in order to control AI levels, planned "animatronic" movement
- Working menu buttons (Thanks Logan!) implemented

06/06/25
- Refining of program
- Code now accesses assets folder properly
- Additional dictionary for enemy control and movement

10/06/25
- Added working door system
- Bug fixes of camera system
- Added actual drawing when switching between screens
- Added lore introduction and screen that displays what night you're on

11/06/25
- Added animatronic movement
- small bug fixes involving door closing
- Working on fixing animatronic mechanics for Logan and Noah
- Added phone call voicelines

12/06/25
- fixed animatronic movement
- more bug fixes for jumpscares
- todo: work on timing of winning the night and telling the player what the controls are

13/06/25
- I downloaded rainbow six siege because it was free access so I might as well try
- In terms of game changes, timing issues fixed for jumpscares and winning the night
- Fixed door issue where you could run to the door even though you're already at the door
- Reset Logan's progress to 0 at the end of each night
- Stopped ambience from playing over the alarm when you win
- Preventing more bugs