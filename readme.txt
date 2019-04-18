Get Topic
Terri Morgan 
@Wudang96 
4/16/2019

Searches the content of a message for a set of keywords (metadata), finds the most common match (by count), then uses that match to get the related paired topic from a paired-topic list. 

The content of a message needs to be read into a variable. It doesn't need to be a separate text file. 


The keywords/metadata file is a list of words that are expected to be found in the text. The more refined the matching, the better the results.
	For the prototype, I created a simple, dummy list that I knew would/would not match.
	Some analysis of which words in which variations with which matching strings is needed. (e.g., Medical will not count Medicine but Medic* will) 

It is possible to create a list from the content (strip stop words) and to increment that list dynamically. There are issues with that, not the least of which is in being able to generate comparisons. At some point, a layer of metadata will have to be added. I'm just doing that first. The benefit is that for statistics on "health care" -- tagged as meta "medic*" the numbers for medical care, medicine, medicare, prescription drugs, and health care could all be grouped. This is one area where word-usage analysis is needed. Most charts should only have 5-9 items at the top level. 

It is also possible to do something with the additional meta (the code already retreieves all keyword matches and counts, I'm only using the top count). That could be used to generate sub-categories (e.g., health care / medical costs v. health care / access). 


For the prototype, I created a Pairs file. It creates a map between the keywords and the topics. After the code has extracted the top keyword match, it checks an array (dict) created from this file to match the keyword to the topic.  
	What has to happen is the pairing (e.g., medical : Healthcare or medical : Healthcare and Medical Costs) 
	Where it comes from is an open question. 

It could be a better way is to add a meta value to the topic lists on the forms. I'd have to work on extracting the values, but it's possible. Might be better to try to extract the topic lists from the forms and create a master 'matching pairs' file.   

However, it could be that once there is something close enough to the topic (like medic* for medicine), the code could use some pattern matching to pick (Healthcare = Health*). This is another area where some word analsis will be needed. Need to look at what the topic variations are and better understand how the forms work. 


If this were a database.... :0

The keywords would be a simple table. The topics could be a separate table, tied to both the pol and the keywords tables.


