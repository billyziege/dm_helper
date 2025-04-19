# Table of Contents
1. [What is this?](#dm-helper)
1. [Why is this here?](#purposes-of-repo)
1. [How does it work?](#what-dm-helper-is-designed-to-do)
1. [Can I use this?](#notes-about-copyright)
1. [How can I set it up?](#running-the-app)

# DM Helper
DM stands for Dungeon Master, a role played by someone playing Dungeons and Dragons (D\&D).
The DM essentially narrates most of the story, called a campaign or one-off, that everyone
else participates in.  There are many modern variants of D\&D and similar games, but
many of these games have a similar focus on dice rolls and statistics. 

The problem is that a good DM needs to
prepare lots of material before telling the story, and then they need to access this information during the
game.  Many people do this using binders.  Many people are very good at retrieving and
understanding large quantities of written notes from bindings.  I am not
one of those people.  I need a helper that can deliver to me the information I prepared 
when I need it.

This is what the app DM helper is meant to do.

Before you get excited, this project is very large and is in its infancy.
I'll update this, though, as I get the project working.

# Purposes of Repo
There are two purposes for this repo: (1) practical and (2) professional.

## Practical Purpose
I have kids.  My kids like D\&D.  They want me to run campaigns.  I have no idea what I am doing.

I have books.  Lots of books.  I know how to read, but it takes me time to flip through
books and read my notes.  It's a disorganized mess, and when my kids do something spontaneous, I
spend so much time trying to figure out what comes next that the story suffers.

I am also a scientist who has been programming for more than 15 years.  I've been using Python
for much of this time, and I have a vague idea about how websites are made (I am not a web-designer,
just a Python enthusiast).  I understand that my disorganization could be solved with a
decent browser app that accesses relational databases on the "back-end".  I am familiar with the Python
modules Flask and SQLAlchemy.  So building an app with these tools is what I am setting out to do.

I am not talking about publishing databases; see my [notes on copyright](notes-about-copywrite)
as to why.  There will be what is known as database schemas (how the databases are organized) in
this repo, but no content.  A content creator (usually just the DM) will provide the content.  The
DM Helper is just a facade that will provide easy access and [persistent] storage for this content.

## Professional Purpose
As I mentioned before, I am a scientist who programs.  I program a lot.  The programming I do
is owned by others.  I cannot publish it, so no one sees my work.

When I am on the job market, how will people know I can work with Python?  This is the other
reason I am willing to see this project through.

# What DM Helper is Designed to do

My current Design follows:

There will be a 4 roles: admin, content creator, dm, and player. Users can have one, all,
or some combination of roles although they can only have one active role.  The use of the
app will dependend on the role.

The admin role will have access to creating users, managing roles, and managing access.  This
will be done by going to the appropriate "webpage" in the browser (via the on-site menus) and
then doing the specified action.

The content creator role will have access to all D\&D related database "tables".
Tables store the information that we want to recall -- like the stat blocks for some character or a monster.
This role will have access to web-pages that allow them to populate these tables.  
For me, this means taking what I read in books and putting it into the web-forms on the web-pages
I plan to create; anyone else using this app will have to do the same.

The dm role will have access to high level tables that allow them to access
all of the information they need for the campaign.  Again, this will be done in the browser.

The player role will have access to character webpages.  This web page will have similar information
to what people call the character sheet.

If you can figure out how to host the app, the DM will be able to access their information while the 
characters access their information simultaneoously from a different device.  At the end of the session, 
any changes to the character can be saved and stored for the next session.

# Notes about copyright

Hasbro owns D\&D.  I do not want to anger a company like Hasbro, and I also want
to protect their Intellectual Property (IP) so that they can continue to make content.
For these reasons, there will be no databases provided here.  The user
has to create the databases themselves, and DM Helper will provide the tools to do that
through the content creator role.

I imagine the content will either be home-brew or
taken from books.  I purchased my books already, and I will be using this content to populate
my tables for my personal use.  I am not interested in sharing this content as
I see that if I were to do so that I could be violating IP law.
If anyone want to share their databases, I recommend you talk
to people about IP before you do.  

This being said, the interface I am creating is made with opensource tools.
The information about the schema is my understanding of how D\&D works from
what can be found online and talking with others.  The tools, the web-pages that interface with the databases,
are my work and make up the majority of this project.  These are under the Creative Commons license.
Feel free to use the tools, modify them, etc. I don't really care about attribution.

If you want to contribute, feel free to contact me via github or email. 
Any code that will be within this repository, though, is going to be under the Creative Commons license, so 
make sure you are okay with that.  I personally think that providing a tool to make
some people be the best DM they can be is a goal unto itself.

# Running the App

The app isn't finished yet.  There is no running it.  When there is, I will update this section.  I also
intend to make a user-document explaining what can be done in each role.
