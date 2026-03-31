## Dissertation Advisement: Progress Reports (2024-26)

### **2026: Progress Report**

March 16

While busy as hell lately, and perhaps more than i would like to admit within a dissertation progress report, I have been plugging away at the introductory chapter as well as reading and writing more broadly on content meant to be integrated in other sections of the project. The other day i wrote a reflection, for instance, on the lineage of literacy crisis discourse and its bearing on where, how, and when students read and write during this very strange and uncanny era of higher education in which we seem to be situated. That reflection was inspired in part by the Visible Pedagogy piece that i’m writing in parallel, [linked here](https://docs.google.com/document/d/1wpRUbhXRjHSGdRA64MOcDc5DIyfOUfAC/edit) though still in progress, which i can see having a place in the dissertation given how many students post their grievances about AI detection on Reddit. 

More specifically, i am interested in beginning the dissertation with a focus on the rise of literacy crisis discourse and the way in which it takes the form of strategic discourse on the part of the university to address larger and more diffuse austerity conditions within public higher education. I want to debunk the deficit model of literacy learning associated with such moral panic, begin to demythologize the fact that students today are not reading and writing, and plant a flag in the idea that societal and institutional pressures are to blame, and that students have responded by taking matters into their own hands by reading and writing not always for coursework or grades but rather as a means by which to survive their time at CUNY. 

From this point, I hope to segue to the conventional opener used in my prospectus and dissertation fellowship proposal, which frames the massive increase in student activity on Reddit over the past five years. At the same time, I aim to emphasize the point that students using Reddit to get by within higher education is nothing new, and that the problems posed and addressed in those spaces represent downstream effects of long-term state disinvestment in public higher ed, leaving students to their own devices and blaming the broader literacy crisis on them as responsible indiviudals in the process. 

At any rate, I am also writign a methodological addendum on my use of agentic coding tools for data collection, preprocessing, and analysis. Here is what I have so far:

*Throughout this dissertation, I employed large language models (LLMs) like Claude as coding scaffolds to support computational methods use for data collection, preparation, and analysis. I want to be precise about what this means and, more importantly, what it does not mean. At no point did an LLM process, read, or have access to the student data collected from Reddit; the language model never saw a single post, comment, username, or any fragment of the 273,702 records housed in my local databases. Its role was strictly limited to generating Python scripts and shell commands that I then reviewed, tested, and* 

*There is a distinction to be made here between the AI tool that generates workable code and the development environment where I run scripts for research. When, for instance, I needed a script to query all comments from r/Baruch containing references to financial aid between March and June 2020, I would describe the task to the LLM in natural language and tie it to the specific database schema, table structure, or SQL filtering logic fit for the task at hand. The LLM would subsequently generate and return a Python script, which I would read, test, and modify before running it myself from command line. In so many words, the agentic coding scaffold would generate the Python script from a description of the task, save it to my machine, and then allow me to run it locally in a separate and secure environment where accumulated findings live as SQLite datasets.*

*For a more specific example, I would often describe a computational task—like “write a Python script that reconstructs discussion networks from a SQLite database of Reddit submissions and comments, linking commenters to original posters through parent ID relationships”—and the LLM would produce a working draft. Sometimes the draft needed significant revision; sometimes it was close to what I needed. In either case, I was the one who executed it, examined the output, and decided what to do next.*

*Consider how this played out with the network reconstruction work I did to fill in gaps left by the discovery logic of my main Reddit scraper, where I built interaction networks across eight CUNY subreddit databases containing submissions and comments with fields like author, parent\_id, created\_utc, and score. The resulting script had to be able to parse Reddit’s t3\_ prefix convention to link comments back to their parent submissions, filter out deleted accounts and bot activity, and output edge lists suitable for network analysis via NetworkX. When I outlined these requirements and submitted them to Claude Code, the LLM produced a script that saved to scripts/analysis/network/, which I would then run against each database independently. The script processed approximately 153,000 edges across the CUNY network, and the model that helped write it never encountered a single one of those edges or the usernames and post content that generated them.*

*Shell scripts made this workflow even more modular: when recurring operations like running the same analysis across all ten databases, for instance, I had the LLM draft shell wrappers that looped through database files and called the Python scripts sequentially. Scripts in bin/ like run\_all\_cuny\_scrapers.sh and query-overview follow this pattern and were driven by scripting methods such as the use of for-loops, path variables, a call to sqlite3 or python3, and so on. In the process, the workflow creates multiple layers of separation between the tool and the data, and I want to walk through these concretely because I think concerns around AI and research ethics often assume a monolithic process where everything flows through a single system, and that is most certainly not how this process unfolded in my case.*

*Because AI-generated code can contain errors, I treated every script the model produced as a draft requiring validation. I ran scripts on small subsets of data first, spot-checked outputs against manual SQL queries, and compared results across multiple analytical approaches to confirm consistency. When a network reconstruction script produced edge counts, I verified those counts against direct database queries, or when another script reported activity spikes across a given period of time, I cross-referenced the dates against known events—the March 2020 pandemic onset, Hurricane Sandy in 2012, CUNY budget crises in 2016—to confirm the patterns were real rather than artifacts of code errors or confabulations courtesy of the coding agent.*

*Any computational research pipeline requires validation regardless of how the code was written. The difference here is one of utility, transparency, and replicability. In disclosing my use of AI as a coding scaffold for Python scripting and data collection and analysis, I hope readers will see those methods as a chance to critique the technology at the same time that they benefit from it, allowing them to evaluate AI’s role in methodology beyond the confines of any one dissertation project. In this case, however, the interpretive claims and broad sweep of this project remains my own, accountable only to me, to my ethos as a researcher, and my dual identity as a teacher and a learner within the CUNY system.* 

### **2026: Progress Report**

Feburary 9

In January, I wrote and submitted my dissertation fellowship proposal, which is [linked here](https://docs.google.com/document/d/1L7qja2LfXLo9ZdP7oSybqe5_U0GhLLJ2rS2k2G8PgMs/edit?tab=t.0#heading=h.aoyqfveycl1) as a Google document. Doing so offered an constructive opportunity to rewrite my prospectus from a few years ago, and allowed me the chance to articulate my current stance on the project, sharpen the focus around Reddit (instead of discord, too), and unpack the broader chronological sweep of the study from 2011-2025, broken into three parts: 2011-2019, 2020-2025, and present day. I’ve also been auditing each of my subreddit datasets for integrity and completeness, and filling in gaps wherever I can find them. Many of these gaps result from the programmatic way in which I collected the data, namely, through user-centric identifiers with cycles of comment recovery.

I’ve also been doing an environmental scan of “bridge users” on Reddit to help fill out the research that will comprise the third chapter. For the purposes of my study, I define a bridge user as someone who contributes to three or more subreddits within the CUNY subreddit ecosystem. Here, I look at those with high levels of clustering and edgewise data that demonstrate pockets of activity across subreddits, examining how these bridge users quilt together these alternative public spheres through conversation around policy, transfer mechanics, comparative institutional knowledge, crisis resources, critiques of the university, and rapid-response peer mentoring practices. From this, I can see students developing a distributed advisory system that augments and at times replaces official university functions, where students name systemic problems, help with CUNYFirst and DegreeWorks, recommend specific schools in the system, explain transfer policies, and express deep knowledge of the quirks of CUNY as an institutional apparatus. 

For more, see the following document I’ve been working on: **[CUNY Reddit Baselines and Participation.docx](https://docs.google.com/document/d/1QgieYQex4aDwRDpXMp7HF_Sw_LSG6XdK/edit?usp=drive_web&ouid=106119372102135658746&rtpof=true)**

**Next step**s: 

- [ ] email committee for methods chat  
- [ ] continuing interview procedures and reaching out to bridge users  
- [ ] finish drafting literature review sections for second and third chapters  
- [ ] email Matt about whether there’s anything he needs to do in terms of IRB protocol    
      * CITI certification renewal?

### **December 2025: Progress Report**

December 8

This past month was a whirlwind. I published an issue of the Journal of Basic Writing and am preparing to publishing an issue of JITP on top of that, along with a workshop and conference presentation on AI-related matters. So I haven’t been able to make time to dissertation writing to the extent that I would have liked. That said, I moved most of my prospectus materials and additional source-integrated material to a Scrivener project for future writing practices. Out of the first chapter, I have written around 5,500 words including but not limited to: an expanded introduction and institutional context, developed material to contextualize Reddit, and revised chapter outlines. I am going to continue drafting this material and aim to send a rough draft to you, Matt, as well as the rest of the committee by the end of the year, so that when we meet as a committee we can discuss that work in addition to the role of generative AI in my research workflow. 

On the subject of interviews, I’m looking into talking with a graduate student who serves as a moderator for multiple subreddits, recommended by a fellow TLC fellow, and who might be able to provide a strong judgement on the moderation and governance principles of CUNY Reddit ecosystem. I’ve also been drafting messages I can send to CUNY redditors en masse. More on that soon. 

Chapter Outline

Chapter 2 examines how students built and sustained peer infrastructures of knowledge and care on Reddit before, during, and after the March 2020 crisis. Computational analysis identifies recurring patterns of material precarity, institutional frustration, and horizontal knowledge sharing that predate the pandemic and persist long after it. CUNY-affiliated subreddits function as local publics (Long 2008), where students carved out discursive spaces distinct from official university communication to address unmet needs. Through danah boyd’s framework of networked publics (2011), I interpret how Reddit’s affordances of searchability, psuedanonymity, and persistence enabled students to build usable archives of vernacular institutional knowledge. Warner’s theory of publics and counterpublics (2002) helps clarify how these networks form not through institutional mandate but through the reflexive circulation of discourse itself, where “stranger sociability” produces recognition, belonging, and collective identity grounded in a shared and often unspoken code of conduct. Drawing on Elliot T. Panek’s framing of Reddit as a city, I then characterize CUNY’s subreddit ecosystem as an urban formation that is at once dense, polycentric, and unevenly resourced, with its neighborhoods linked by overlapping flows of information and care. Panek notes that “subreddits possess small cores and large peripheries,” a pattern that mirrors the circulatory dynamics of the CUNY network, where a relatively small set of steady contributors anchors an ever-changing population of newcomers seeking help.

Chapter 3 turns to the structure and resilience of CUNY’s distributed eight-subreddit network. The network includes r/CUNY, r/Baruch, r/HunterCollege, r/QueensCollege, r/JohnJayCollege, r/CityCollege, r/Brooklyn\_College, and r/NYCCC. I contrast CUNY’s federated arrangement with the single-subreddit systems used by NYU and Columbia to show how campus-specific forums cultivate local expertise while sustaining circulation across institutional boundaries. The distributed model supports both autonomy and interconnection, and enables information and mutual aid to move laterally through the system rather than vertically through official channels. The chapter presents case studies in collective problem-solving that make such resilience visible—from improvised registration workarounds and ad-hoc advising guides, to posts about late trains, broken elevators, and rodent infestations that render everyday study itself a logistical challenge. When CUNY campuses blocked access to social platforms on campus Wi-Fi, for instance, CUNY Reddit threads circulated VPN instructions and alternate client recommendations within hours, showing how students deploy technical literacy to counter institutional restriction and sustain connectivity. Drawing on semi-structured interviews, this chapter foregrounds stories from students who turned to subreddit communities for academic, personal, and social survival, and accounts for how students “go public as ordinary people” (Long 2008\) while navigating complex bureaucracies and asserting agency within what Brim (2020) calls CUNY’s “underclass institutional identity.”

### 

### **November 2025: Progress Report**

November 10

I conducted another interview this past month with a past student but have not yet taken the plunge into interview super users and moderators. The interview I did run was constructive, with the student highlighting the oft-unspoken understanding that students on Reddit often share when contributing to CUNY subreddits. That understanding is based on an “unspoken… connection or bond” as well as an “emotional, profound gut feeling” ([transcript](https://drive.google.com/drive/folders/11WDBqtC2qHC3XSXceKGhETEUJuZ59MsA)), and driven by a desire to “know what’s going on” among other things. Perhaps the most interesting takeaway from this interview was the student’s description of gaining access to a book in the library through a recommendation on Discord from another student who “instantaneously wanted to help me with no regard for getting anything in return.” The student later discussed paying it forward by playing the role of the recommender, the advocate, for another student in the same position as him. Overall, it was a very successful interview\!

More broadly, I’ve been writing mostly in markdown files and organizing them on a Jekyll site with lots of relevant resources, writing guide material, analytical reports, and the like. The prose is not up to snuff, but the broader arc of how I’m approaching the dissertation structure and the paragraph units are well on display on this site, which I’ve linked below. Part of why I’ve elected to do this in Jekyll is because I plan to migrate some of these resources to Manifold, but more broadly I’ve like the process of writing in a text editor and later reading and reviewing the results using public Hypothesis annotations. It makes for a nice separation of writing and editing practices and enables me to read for broader argumentative and organizational concerns without getting caught up on the sentence-level, where I tend to lose the forest for the trees. \`

The site is broken into three parts: chapter writing drafts, resources like evidence IDs and analysis reports, and a series of blog posts that track the broader process. A disclaimer that some of the analysis reports and blog posts have been written with the help of Claude to pin down methods and insights before I forget what I was doing, so most of the site is not necessarily usable in the dissertation directly so much as guided documentation and process logs for my reference. That said, the first chapter outline could use review for broader organizational concerns, such as whether the progression makes sense, what to keep and what to cut, as well as broader argumentative moves and claims. 

One final note about Discord being banned on campuses such as Baruch. Where can I find official reports on this news? Seth Graves mentioned it to meIs Reddit next?

* Interview number 4: [https://drive.google.com/drive/folders/11WDBqtC2qHC3XSXceKGhETEUJuZ59MsA](https://drive.google.com/drive/folders/11WDBqtC2qHC3XSXceKGhETEUJuZ59MsA)   
* ~~Dissertation drafting website: [https://zmuhls.github.io/dissertation/](https://zmuhls.github.io/dissertation/)~~ 

Minutes

- Reach out to Seth to see what documentation around Discord wifi  
- College is attempting to control student discourse; failing to understand how students use it? or are they well-aware and attempting to consolidate channels of communication around Teams?  
- [https://www.wired.com/story/nepal-discord-gen-z-protests-vote-prime-minister-election/](https://www.wired.com/story/nepal-discord-gen-z-protests-vote-prime-minister-election/) 

### **October 2025: Progress Report**

October 8

Lately, i’ve been working on developing an outline of my three chapters with evidence IDs and source material to help build out the substance and structure of a writing guide. In the process, I’ve been wondering about the organizing principles of my chapters, and how much to include the first chapter without making it redundant or overwrought with details. To be brief about it, I’m focusing on establishing a pre-pandemic baseline in the first chapter to help draw out the infrastructural cracks that were amplified (rather than created) by the COVID-19 pandemic, with attention to crisis-related discourse and student survival strategies. By investigating the difference between intensification of existing problems, I’m interested in how student already built parallel educational infrastructure before the pandemic that was then intensified and rendered as a kind of publicly visible discourse during and after COVID-19 hit the NYC area. The first chapter seems like an ideal place to establish this baseline and to preview 

Part of this analysis involves a computational treatment of comments and posts that demonstrate compound crisis discussions, which, according to my calculations, increased by 679% since the pandemic. For instance, some students discuss emergency aid requests in connection with eviction threats, or they discuss CUNYfirst registration holds blocking both financial aid access and house assistance. There are TONS of examples of cascading vulnerabilities: student dorm closures during the pandemic causing house instability and mental health crises, difficulty accessing financial aid portals due to lack of technology, evicted students sleeping in their car unable to concentrate on classes. In addition to these analyses of crisis discourse among students, I’m also looking at what de Certeau calls “clever utilization” of imposed power structures, such as how students hack systems-level infrastructure to work in their favor, including registering timing strategies, inter-campus ePermit navigation, credit threshold management, grade recovery tactics, and administrative language translation.

Here is an overstuffed but substantive outline of the first chapter, such as it stands: [Introduction, Context, and Literature Review.pdf](https://drive.google.com/file/d/16dzY0l4gN8HLHFbmySqLeM_mzGpT0J_Z/view?usp=sharing) 

Minutes:

- Consider reducing the amount of percentages; move these to the second review  
- What am I trying to get people to understand in the first chapter?   
- What is it about reddit theoretically and in terms of the literature that i need to   
- Differentiate between the computational findings and the theoretical basis of the argument   
- Argumentatively, what does the first chapter need to do to bring readers on board?

Next Steps: 

* Reach out to super users and moderators  
* Contact students identified as at-risk based on their posting patterns  
* Destatisfy the first chapter to make a clearer separation of findings and theoretical grounding 

### **September 2025: Progress Report** September 8th

[CUNY Reddit Statistical Overview](https://docs.google.com/document/d/17QUaB_qdcLuJuO6uwHUoLV98tLFg3d11Lddj7P-RvCQ/edit?tab=t.0)

Review of work done:

* Scraped 8 CUNY-affiliated subreddits  
* Conducted distant reading analysis in terms of temporal, network, and text data  
* Scraped r/NYU, r/Columbia, r/Fordam, and others for comparative analysis

Next Step: 

* Reach out to edge cases surfaced by the statistical report  
* Put together reading material for Matt to review  
* Transform research\_process\_log.md into academic paragraphs

Minutes

* How can I make policy recommendations that engages the super users? What can I pull from their contributions in terms of policy for the university? What knowledge do they carry and distribute, and why do they do it? 

### **May 2025: Progress Report**

Monday, May 12th

Done with interview \#2\! The second interviewee appeared to be a less active user of CUNY Reddit and Discord. They did, however, emphasize the importance of the physical commons, of spending time in CCNY common areas with friends, and of the material stability that comes with commoning with peers on campus. Many of their experiences veered in and out of digital spaces: they joined a LGBTQ CUNY Discord server but felt awkward with its silences and lack of critical mass, and so left. This reminded me of the CUNY spaces which exist, but which are not made public or available to broader CUNY stakeholders. They also described Reddit more broadly, and CUNY Reddit more specifically, as a 24/7 hour deli, which I thought was an apt description. One major takeaway from this interview involved their commentary on “Blackspace” (lol) and the general fear that comes with learning and writing in ways associated with your formal name; that is, the student suggested that the LMS make room for student usernames to leverage the pedagogical affordances of writing and learning with a moniker, which students of their generation have grown increasingly used to, and which gives them space to step outside of their comfort zone, to push the limits of their learning, without fear that their name will always be attached to the learning they do. I thought this was a profound point, and I hope to keep that attention to pseudo-anonymity and monikers at the forefront of interviews going forward. 

1. **Transcript \#2**: [02\_full\_transcript.txt](https://drive.google.com/file/d/1d2c4EHsVeHEgp1OnsgtmiuxBsKhV-GBS/view?usp=sharing)   
2. **Next step**: complete 7-10 interviews and draft Chapter 1 by the end of summer  
3. **Smaller next step**: interview two undergraduate students (Timmy and Simmy) I met at the TLC/FI showcase who are both smart and engaging and interested in the project. 

### **April 2025: Progress Report**

**Monday, April 21**

Recently finished my first interview with NP about Reddit and Discord, which exceeded expectations and gave me some really grounded, interesting insights into how differently these platforms function NP helped me see that Discord is more about community-building with flexible privacy options allowing users to make spaces either public or private depending on what you're going for. Reddit, on the other hand, is public from day one, which encourages students to look there for “honest” information, rather than to build relationships. I'm eager to see if these patterns, especially this dichotomy between information-seeking and community-seeking purposes, holds up in future interviews, or if they're just NP's personal experience. Next interview is tomorrow, so more to come… 

1. First interview complete: [01-NP-Interview-Transcript.pdf](https://drive.google.com/file/d/11JrijeA7A-DQluH-qGY5TfSJ2IyVy-hB/view?usp=sharing)  
2. Second interview tomorrow, April 22, at 4pm  
3. U/I for Reddit scraping: TBD

### **March 2025: Progress Report**

**Monday, March 24**

***Meeting Notes:*** 

*What is the disbursement mechanism of the DSRG grant? This will influence how funds are tracked from disbursement to compensation to receipt. Here, I have roughly two options. One is to cover the gift cards and cover the payment later on; another is to delay payment to students, then pay them once the grant monies become available via ACH.*

*Remember to take advantage of the interviews I can do, recognizing the limits of having only $500 to spend, specifically in terms of phases and batches. Move slowly and start with the first batch of four—two students, then two more—advance to the next batch of four with key moderators and top commenters, who will bear the greatest fruit, prioritizing the interviews that most centrally aligned with the goals of the project, reserving the last batch of 4-8 interviews to fill gaps and address lingering issues or concerns from the first two batches of interviews.*

**March Update: Part 2 (3/23)**

1. **Awarded DSRG funds ($500)—I am officially IRB exempt and funded\!**  
2. **Need to wait until early June 2025 before I can start using these funds**  
   * Do I really need to wait until June 2025 before conducting any interview?  
   * Hypothetically, could I cover $35 worth of Visa gift card credits then repay the deficit with the dsrg money once available in June?   
2. **Planning a interview recruitment strategy in the near-future**  
   * Reach out to a handful of major moderators and top commenters   
   * Reach out to past students of mine from both Baruch and CCNY  
   * Thinking about entry points and types of Reddit content to guide the search:  
     * Communities:  r/CUNY, r/Baruch, r/CCNY, r/HunterCollege, r/QueensCollege, r/BMCC, r/CUNYuncensored, r/NYC  
     * Subjects: Top Posters and Commenters, Recreational Posters and Commenters, (Ex-)Moderators, Subscribers, and Lurkers (i.e. the silent majority)  
     * Features: Comments/Threaded Comments, Posts, Flair, Rules, Wiki, Subreddit Info and Images, Pinned Messages, Automations  
3. **Potential fieldwork at the college campuses:** Following Pigg (2022), I’d visit campuses to observe and take field-notes, and interview students about their thoughts on that college’s subreddit and CUNY Reddit more broadly. Informed by field-notes and participant observation, I could leverage “think-aloud protocol” (LaFrance 2023\) to facilitate ad hoc, semi-structured interviews in quick non-commital, serendipitous ways, tapping this semi-random, self-selected pool of potential participants as a countermeasure against overfitting the data to the research project.   
4. **Need to complete this form:**   
   [https://docs.google.com/forms/d/e/1FAIpQLSdZEYcv-vWOFu0775Sb7r27LXnIG2VwYSJ4GGzSN-AYvSCrDg/viewform](https://docs.google.com/forms/d/e/1FAIpQLSdZEYcv-vWOFu0775Sb7r27LXnIG2VwYSJ4GGzSN-AYvSCrDg/viewform)   
   * Reach out to department to see if there are still funds available from this initiative

**Reflection (March 3/10)**  
Lately, I presented my work on Reddit to Rhet-Comp people in Milaukee and have been writing freely to build out framing materials for the first chapter or two. I also delivered an elevator pitch to the TLC on the project, and have since been reflecting on whether to center my analysis on Reddit or incorporate Discord as an extension of student engagement from subreddits. Must it be both platforms or only one? Could I justify a chapter dedicated to discourse analysis of student posts and comments within CUNY subreddits, alongside a separate ethnographic chapter on Reddit that acknowledges significant subreddit connections to Discord? Framing it this way allows me to narrow the project’s scope clearly and propose Discord as an area for future research—something I can revisit and develop more thoroughly in a subsequent book project.

*March 10, 2025*

1. **Update (3/10): the project is officially exempt with IRB approval**  
   1. Previously I resubmitted IRB Protocol with the templated consent form, updated other info, and had been going back and forth with Rebecca to finish things off  
   2. Now I’m waiting on DSRG funding to begin reaching out to interview candidates

   **Pursue funding opportunity** within the department: [https://docs.google.com/forms/d/e/1FAIpQLSdZEYcv-vWOFu0775Sb7r27LXnIG2VwYSJ4GGzSN-AYvSCrDg/viewform](https://docs.google.com/forms/d/e/1FAIpQLSdZEYcv-vWOFu0775Sb7r27LXnIG2VwYSJ4GGzSN-AYvSCrDg/viewform) 

   **Drafting framing materials** grounded in scholarly sources to guide the broader project's conceptual direction, particularly the discourse analysis (e.g., digital orality, local literacies, commoning, problem-posing postures, "keeping the conversation going")

   3. [INTRO: Framing Paragraphs on Reddit and Discord](https://docs.google.com/document/d/1ESutw1noVyTmMJlFduG8GzJJnzNcTW-70g5PZ952sYU/edit?tab=t.0) 

   **Interview candidates**: 

| First Round of Interviews | Subreddit/Discord |
| :---- | :---- |
| futuretechftw2 | r/CCNY |
| stopsakura10 | r/HunterCollege |
| ehebsvebsbsbbdbdbdb | r/HunterCollege |
| flashcapulet | r/CUNY |
| Brilliant\_Claim1329 | r/HunterCollege |
| Ramen\_thekeami | r/CCNY |
| dumbgumb | r/Baruch |
| andrea\_dee\_ | r/CUNY |
| Salty\_Bag1852 | r/QueensCollege |
| Nintendo\_Pro\_03 | r/CUNY |
| Correct\_Mountain2886 | r/QueensCollege |
| Interesting-Ship7161 | r/CUNY |
| coruscree | CUNY Hunter College |
| skyronthekid | CUNY Hunter College |
| rexythedragon | CUNY Hunter College |
| aharongrama | CUNY |
| zeallll | CUNY |
| jakedenko | Baruch College |
| happy\_abe | Baruch College |
| aharongrama | Brooklyn College |
| mobina1359 | Brooklyn College |
| plebble\_ | Brooklyn College |
| egrodo | Baruch College |
| yonniman | Baruch College |

### 

### 

### 

### 

**Dissertation Resources**

* Prospectus: [ZM-Prospectus.pdf](https://drive.google.com/file/d/19onFRmzx0yXzGOhOmUb-VlqC9cmwaVAK/view?usp=drivesdk)  
* Assorted Resources:[2023-2024 Dissertation Resources.docx](https://docs.google.com/file/d/1CIrZZlgFsDgpYD0rYK00xJPOvyyE3XBj/edit?usp=docslist_api&filetype=msword)  
* Interviewee Recruitment: [interview\_candidates\_reddit-discord](https://docs.google.com/spreadsheets/d/1t2Olwqp8mODOicxJl8bdi4IJSN1AN86g52e8hRZRUzM/edit?usp=drive_link)  
* Interview Guide: [IRB Interview Guide](https://docs.google.com/document/d/10hstoYRBGa1bAjWeLEaQlUkIwr7hTEFvvrQ3wTOFoCg/edit?tab=t.0#heading=h.e0s2x3fmb6jp)  
* DSRG Grant:[Grant Proposal\_Voices from the Digital Town Square.docx](https://docs.google.com/document/d/1sNOtvWihO892-Q4MFYvaIk_1p5go0XoY/edit?usp=drive_link&ouid=106119372102135658746&rtpof=true&sd=true)

**Meeting Notes**

* Reddit as primary and Discord as secondary? Batman and Robin, or?   
  * Lead with interests: Reddit  
* Other funding opportunities I should have on my radar?   
  * Internal departmental funding  
* Best way to get feedback on early drafting efforts during our next meeting?   
  * Send local word document to Matt with some targeted sections for feedback on sections that would benefit from further development

### 

### **January 2025: Progress Report**

**Reflection**  
I submitted the dissertation fellowship proposal and am revising the protocol form based on feedback and suggestions. My goal is to resubmit and secure IRB approval by early to mid-February. Once approved, I’ll begin reaching out to potential study participants to schedule semi-structured interviews. I’ve already added the requisite forms to the IRB protocol, ensured consistency across sections, and completed the draft for the dissertation fellowship grant.

**Grant Proposal(s)**  
Dissertation Grant**:**[Grant Proposal\_Voices from the Digital Town Square.docx](https://docs.google.com/document/d/1sNOtvWihO892-Q4MFYvaIk_1p5go0XoY/edit?usp=drive_link&ouid=106119372102135658746&rtpof=true&sd=true)

**Next steps:**

* Submit application for DSRG  
  * Matt: “Your mentor needs to confirm this in a simple way when you apply — and be available for guidance.” (Email here: [dsrg@gc.cuny.edu](mailto:dsrg@gc.cuny.edu))   
* Resubmit IRB Protocol Form and address these concerns:  
  * Zach: Make compensation consistent throughout form  
  * Zach: Add final interview recruitment document (re: internet based consent form)  
  * Zach: Revise recruitment materials  
  * Zach: Add email script  
  * Zach: Add oral or internet based consent/information document  
  * Zach: Address minor notes and suggestions (re: Consent, Procedure & Risk)  
  * Matt: CITI HSR Training \- Expired 03/17/2024  
* Present in Milwuakee as part of the WIC Cookbook conference (this Friday)  
* Draft excerpts of Ch. 1 to get writing about Reddit, Discord, and so on

**Dissertation Resources**:  
Still awaiting departmental feedback: [ZM-Prospectus.pdf](https://drive.google.com/file/d/19onFRmzx0yXzGOhOmUb-VlqC9cmwaVAK/view?usp=drivesdk)  
Assorted resources and notes:[2023-2024 Dissertation Resources.docx](https://docs.google.com/file/d/1CIrZZlgFsDgpYD0rYK00xJPOvyyE3XBj/edit?usp=docslist_api&filetype=msword)  
Recruitment data: [interview\_candidates\_reddit-discord](https://docs.google.com/spreadsheets/d/1t2Olwqp8mODOicxJl8bdi4IJSN1AN86g52e8hRZRUzM/edit?usp=drive_link)

**IRB Documents:**  
[IRB Interview Guide](https://docs.google.com/document/d/10hstoYRBGa1bAjWeLEaQlUkIwr7hTEFvvrQ3wTOFoCg/edit?tab=t.0#heading=h.e0s2x3fmb6jp)

**Meeting Notes**  
*Reddit Answers*  
How does the community affordances of CUNY reddit get flattened ? How does this resemble dana boyd’s notion of “context collapse” in social media research? Has/will the number of subscriber, posts, and comments slow down following the beta release of Reddit Answers? What are the implications of writing on Reddit for community audiences compare to posing questions through LLM-powered tools like Reddit Answers? The results link back to the community, but what is lost for student contributors in the process? How does the student-run public sphere get collapsed into bullet points and hygenic tidbits? These lines of inquiry might be worthwhile to integrate this work as part of an epilogue. Future directions and invitations for further research. 

### 

### **December 2024: Progress Report**

**Reflection**  
I didn’t receive funding via the PS2 Adjunct Incubator grant and can’t proceed with the protocol form until I have a pending grant, so I repurposed the prospectus to serve as a doctoral student research grant application, and I’s beginning to finalize IRB documents (see below), such as the interview guide, consent form, and recruitment materials. After I send in the grant application, I’ll be free to submit my IRB protocol form. Between now and then, I’ll take time to review literature on Reddit and Discord in an effort to start drafting framing materials that can go in the first chapter. I’ll also present work closely related to the dissertation in Milwaukee, which will provide some grounded insight into how comp-rhet scholars perceive this research, offering a chance to refine my approach based on their feedback.

**Grant Proposal(s)**  
[Grant Proposal\_Voices from the Digital Town Square.docx](https://docs.google.com/document/d/1sNOtvWihO892-Q4MFYvaIk_1p5go0XoY/edit?usp=drive_link&ouid=106119372102135658746&rtpof=true&sd=true)

**Dissertation Resources**:  
Still awaiting departmental feedback: [ZM-Prospectus.pdf](https://drive.google.com/file/d/19onFRmzx0yXzGOhOmUb-VlqC9cmwaVAK/view?usp=drivesdk)  
Assorted resources and notes:[2023-2024 Dissertation Resources.docx](https://docs.google.com/file/d/1CIrZZlgFsDgpYD0rYK00xJPOvyyE3XBj/edit?usp=docslist_api&filetype=msword)  
Recruitment data: [interview\_candidates\_reddit-discord](https://docs.google.com/spreadsheets/d/1t2Olwqp8mODOicxJl8bdi4IJSN1AN86g52e8hRZRUzM/edit?usp=drive_link)

**IRB Documents:**  
[IRB Interview Guide](https://docs.google.com/document/d/10hstoYRBGa1bAjWeLEaQlUkIwr7hTEFvvrQ3wTOFoCg/edit?tab=t.0#heading=h.e0s2x3fmb6jp)  
[IRB Informed Consent Form.docx](https://docs.google.com/document/d/1UZ2cvxcUnP3exF_Xi9BjXjtjGYEkTsti/edit?usp=drive_link&ouid=106119372102135658746&rtpof=true&sd=true)  
[IRB Recruitment Document](https://docs.google.com/document/d/1Z8qqk5VOWEghykFO2nNYXvshNlJ0IWyR/edit?usp=drive_link&ouid=106119372102135658746&rtpof=true&sd=true)

**Next steps:**

* Submit application for Dissertation Fellowship Grant  
* Submit IRB Protocol Form after submitting new grant application  
* Present in Milwuakee as part of the WIC Cookbook conference  
* Draft excerpts of Ch. 1 that frames the study within the historical contexts of Reddit/Discord 

**Meeting Notes**: 

* Regarding the interview guide  
  * Plain language, tailor to CUNY students’ vocabulary and language  
  * Do i want to ask them about how they are accessing these spaces? Are they do it through email on their computer, or are they accessing it as apps on their phones?   
  * To what extent is anonymity important on Reddit and Discord?   
  * What kinds of responses have you gotten from CUNY officials?

  * ### Be more direct: What are your experiences as a CUNY student, especially concerning the support you receive or do not receive from the university?

* What are my central hypotheses and how can I ask them directly to elicit answers from students more directly?


### 

### **November 2024: Dissertation Progress Report**

**Reflection**  
Applied to the adjunct incubator grant to fund interviews with moderators and active participants in these communities; proposed $4,000 budget allocates funds for participant compensation, transcription services, support for student communities, and associated travel and research expenses. Completed first draft of the informed consent form that I will eventually distribute to participants before conducting semi-structured interviews over CUNY Zoom. Based on this [IRB template](https://researchservices.cornell.edu/sites/default/files/2019-05/IRB%20consent%20template%20-%20social-behavioral.doc). 

**Documents**

* **Adjunct Incubator Application**:[Muhlbauer\_Zachary\_CAI2025.pdf](https://drive.google.com/file/d/12c4f5njB2kmTXc4ouR365gOY0iJQ455i/view?usp=sharing)  
* **Informed Consent Form**: [Draft\_Informed\_Consent\_Form.docx](https://docs.google.com/document/d/1UZ2cvxcUnP3exF_Xi9BjXjtjGYEkTsti/edit?usp=drive_link&ouid=106119372102135658746&rtpof=true&sd=true)

**Next steps**

* Finish IRB protocol forms  
  * Bug in the form? Need to email IRB again.   
* Finish second draft of informed consent form   
* Draft interview questions (identify \~30 participants to contact)  
* Draft excerpts of Chapter 1 and Chapter 2  
* Apply for [internal funding sources](https://www.gc.cuny.edu/fellowships-and-financial-aid/doctoral-student-funding/early-research-initiative/internal-funding-sources)  
* Present in Milwuakee; submit to WIC Cookbook

**Dissertation Resources**:

* Still awaiting departmental feedback: [ZM-Prospectus.pdf](https://drive.google.com/file/d/19onFRmzx0yXzGOhOmUb-VlqC9cmwaVAK/view?usp=drivesdk)  
* Assorted resources and notes:[2023-2024 Dissertation Resources.docx](https://docs.google.com/file/d/1CIrZZlgFsDgpYD0rYK00xJPOvyyE3XBj/edit?usp=docslist_api&filetype=msword)

**Reddit Data** (e.g. r/CUNY, r/Baruch)

* First web scraping attempt on Reddit:[0624\_reddit\_dataTable\_early\_run.xlsx](https://docs.google.com/spreadsheets/d/1mPfJz0dj2uPt1QSFyW6mAWFuzg1QmEOT/edit?usp=sharing&ouid=106119372102135658746&rtpof=true&sd=true)   
* Updated version of the first web scraping attempt above: [0924\_cunytest\_v2\_results.xlsx](https://docs.google.com/spreadsheets/d/1XCLrYTe2k3iAdX3__330_72bYgtt3Cib/edit?usp=drive_link&ouid=106119372102135658746&rtpof=true&sd=true)  
* Too big to open on Google Drive but a good view of user activity: [user\_activity\_output.xlsx](https://docs.google.com/spreadsheets/d/1-4Qk79BaiTK_rV8uq8v7XhDVHDJ2Nwdm/edit?usp=sharing&ouid=106119372102135658746&rtpof=true&sd=true)  
* In progress, need to port over Reddit prospects:[Reddit/Discord Interview Participants](https://docs.google.com/spreadsheets/d/1t2Olwqp8mODOicxJl8bdi4IJSN1AN86g52e8hRZRUzM/edit?usp=sharing)

**Google Drive Folder**: [Dissertation\_ZM](https://drive.google.com/drive/folders/1HE6f3jnQFUHf63IvdaKdZxWOb0Np9mjr?usp=drive_link)

**Tue Nov 12 Notes**:

- Getting students opinions on why they communicate in these spaces as opposed to institutional channels. Get sense of their relationship to university services compared to social media services:  
  - How many are aware of the problems that drive why they engage these spaces?  
  - What’s important about these spaces? Why does it make it you feel more or less comfortable to engage your fellow students for support in this forums?   
  - How many advising sessions have you gone to? What did your advisor recommend if you did? How did this not meet your needs such that you needed more support from peers?   
  - Did you contact the registrar? What did they say? How did you feel your meets were or were not met as part of more traditional communications with university officials?   
  - How does the anonymity of communicating in Reddit and Discord influence your relationship to these spaces compared to official channels of university communication? 

- Different categories of interview subjects:  
  - Primary: Student-users in search of answers, sociality, support, and community  
  - Primary: Student-users acting as moderators who design and maintain these spaces to support their peers and college community, even after they graduate and become alumni   
  - Secondary: College faculty and staff (e.g. Lehman)   
  - Secondary: Prospective students / potential applicants  
  - Tertiary: University administrators, faculty, and staff unaware of these spaces

- 

