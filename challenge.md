# Stellar Coding Challenge

## Summary
Write an API web server that accepts a snippet of text and makes that snippet
available at a URL. Each snippet should be available as text at a URL until it
expires. Snippets expiry should be extended when they are accessed.

The request to store the snippet should accept this information:
- name
- expires
- snippet

The request to store the snippet should be replied to with a response that
includes the URL where the snippet can be read.

Snippets can be stored in memory, and do not need to be editable after storing.
The solution needs only to be an API, not a graphical or website user
interface.

## Extension
Pick one feature to implement on top of the above. Pick only one.
1. Store snippets on disk in files.
2. Allow editing snippets using a password set at the time they are stored.
3. Add a "like" API endpoint that increases a counter for a snippet.

## Instructions
Aim to spend about 2-hours on an implementation.

The code should be comparable to code you’d put in front of others for code
review and put in production. It should address production concerns, but the
number of concerns it addresses may be limited given the time constraint.
Include what you can. If you’re short on time, aim to make something unpolished
that works rather than something polished but incomplete.  Feel free to access
online resources, but you must complete the challenge without help from anyone
else.

Include a README that explains how to use your API, assumptions, design
decisions, production concerns addressed, why you've chosen the technologies,
data formats, and message formats used in the solution, and any other
discussion about the solution to demonstrate your experience building
production systems.

Use the repl.it online IDE to code your solution. Go to [repl.it/languages] to
start. Once your application exposes a port (e.g. 3000, 4567, 8080) your
application will automatically be given a URL where you can access your API.
You may also code your solution offline on your own computer, but please upload
your solution to repl.it and ensure it runs successfully before sending in the
solution.

Use the language you are most proficient with to complete the solution, but if
you are proficient in Go we’d love to see what your solution looks like in it
as we use Go heavily.

[repl.it/languages]: https://repl.it/languages
