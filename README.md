# Parser_for_angel.co
Task
The customer wants to get a parser function in Python that would accept a link to a person's page on the angel.co site. 
The outcome has to return a link to their Linkedin, or None if the specific person does not have a Linkedin link on the page.
The function should work when you transfer at least 100 links to it within an hour.

Outcome
The script works with the angel.co website only and has dual functionality:
1) entering a separate link to a specific user on the site.
At the output, you have a username in the console and a link to the Linkedin profile, 
if any, otherwise None + a bonus .txt file is created in the directory with the script.
2) specifying a file with a list of links (the file must be .txt and the links must be line by line). 
At the output, we have everyone in the console + result.txt.
