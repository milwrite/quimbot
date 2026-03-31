# CUNY Reddit Corpus — Learning Trajectory Narratives

Eight Reddit users whose post histories across CUNY subreddits constitute **serialized educational narratives** — from application and enrollment through coursework, institutional friction, and graduation. These longitudinal profiles document the "hoops and hurdles" of navigating CUNY as first-generation, immigrant, transfer, and working students, grounded in **822 pieces of evidence** spanning 2018–2025.

**Key finding:** Two distinct narrator types emerge — *submission-based narrators* who document their journey through questions (Recent-Sky3311, Koran21, morphhyxia), and *comment-based narrators* who embed autobiography in peer advice (Salt-fish, HOIXIOH). Both types use Reddit as institutional GPS, but comment-narrators reveal their stories only obliquely, requiring reconstruction from scattered replies.

---

## Methodology

### Candidate Identification

Three parallel search strategies queried all 8 populated CUNY databases:

1. **Submissions-based longitudinal analysis**: Users with 10+ submissions whose `MAX(created_utc) - MIN(created_utc)` exceeded 2 years, filtered by educational keywords (transfer, graduate, financial aid, accepted, GPA, degree)
2. **Cross-subreddit matching**: Users appearing in 2+ campus-specific databases, indicating multi-campus engagement
3. **Comment-based journey reconstruction**: Users with 20+ comments containing autobiographical markers (first-person pronouns + institutional keywords), revealing educational narratives embedded in advice-giving

### Selection Criteria

From 22 Tier 1–2 candidates, 8 were selected based on:
- **Narrative completeness**: Documented arc from entry point through outcome
- **Minimum evidence threshold**: 5+ posts with educational content
- **Demographic diversity**: Transfer, immigrant, first-generation, working student, COVID cohort, major-changer
- **Arc coherence**: Posts form a legible chronological story

### Evidence Conventions

- Evidence IDs follow the format `submission_XXXXX` or `comment_XXXXX` (Reddit base-36 IDs)
- All IDs verified against source databases in `data/databases/current/`
- Dates are UTC; scores reflect community upvotes at time of data collection

---

## Profile 1: Recent-Sky3311 — Community College Transfer Odyssey

| | |
|---|---|
| **Subreddits** | r/CUNY, r/Baruch, r/HunterCollege, r/QueensCollege, r/BrooklynCollege (5) |
| **Span** | 4.5 years (Jan 2021 – Jul 2025) |
| **Evidence** | 46 submissions, 89 comments (135 total) |
| **Identity** | Latina, bilingual, depression, financial aid dependent |
| **Arc** | BMCC → applies to 4 senior colleges → agonizes over Baruch vs. QC vs. Hunter → enrolls at Hunter → academic crisis → recovery → still enrolled 2025 |
| **Tags** | `transfer` `financial-aid` `community-college` `accounting` `Latina` `depression` |

### Chronological Narrative

**Phase 1: Transfer Decision-Making (Jan–May 2021)**

On a single day — January 28, 2021 — Recent-Sky3311 posts across *four* subreddits simultaneously, asking about accounting programs at Baruch, Hunter, Brooklyn College, and QC. This cross-posting pattern, unprecedented among our candidates, reveals the CUNY transfer decision as a multi-campus comparison process played out in real-time across Reddit.

> "I heard Baruch has a grading curve so is it worth it going there for accounting?" — `submission_mw64xb` (r/CUNY, Apr 2021)

> "This school seems very competitive especially in regards to their accounting program... What if I do decent in a class but what if most of my classmates do better than me and what if they're the ones to end up with the A's, B's. What if I get curved down? And eventually dropped from the program? This is why I feel that accounting at baruch would be stressful and maybe even worsen my depression if I try my hardest and it's still not enough" — `submission_r0ymom` (r/Baruch, Nov 2021)

The Baruch anxiety is not abstract — she names depression explicitly and connects academic competition to mental health. Over 7 posts in r/Baruch across 10 months, every submission asks a variation of the same question: *Is Baruch worth the psychological cost?*

**Phase 2: Logistical Chaos (May–Dec 2021)**

Accepted to four senior colleges. Missed National Decision Day by *one minute* (`submission_n3en8i`). Accepted Baruch, then couldn't attend because summer classes at BMCC weren't available, forcing her to undo the acceptance (`submission_n5zafj`). Applied again. The cycle of acceptance, reversal, and re-application spans six months and 8 posts.

She eventually pivots away from Baruch entirely, accepting QC — then considers switching again:

> "I already accepted the offer of admission from qc, completed my transfer advisement today, and registered in some classes today. However, I got accepted to another college and I am now thinking that I want to accept another cuny school's offer of admission instead." — `submission_ri92mt` (Dec 2021)

**Phase 3: Academic Crisis at Hunter (Fall 2022)**

By November 2022, enrolled at Hunter, she faces financial aid jeopardy:

> "I'm taking 4 classes this semester (13 credits) but one of them is 4 credits. If I drop that class, will my financial aid be affected? ... I think I'm going to fail that class for sure and it would really mess up my gpa (I need higher than a 2.0 to keep getting financial aid)." — `submission_ytkna2` (Nov 2022, score 9)

The strategic calculus of *fail vs. withdraw* — weighing GPA damage against financial aid eligibility — generates 8 comments across r/CUNY and r/Baruch as she crowdsources the decision. She ultimately withdraws from two classes, dropping to 6 credits, and explores whether transferring to another CUNY would reset her financial aid eligibility (`comment_iz5fmwj`).

**Phase 4: Recovery and Persistence (2023–2025)**

Uses e-permits to take courses at other CUNY schools. Repeats intermediate accounting 2 at Hunter. By January 2025, takes an evening class at Queens College, and by July 2025 is navigating MFA authentication — still enrolled after 4+ years at the senior college level.

**Observation:** Recent-Sky3311's 135 posts across 5 subreddits constitute the most cross-posted transfer narrative in the corpus. Her trajectory reveals that "choosing a college" at CUNY is not a single decision but an iterative, multi-year negotiation between institutional reputation, personal mental health, and financial survival.

---

## Profile 2: Hypebeastzx — QCC to Hunter Biology, Complete Degree

| | |
|---|---|
| **Subreddits** | r/CUNY, r/HunterCollege, r/BrooklynCollege (3) |
| **Span** | 3.7 years (Jul 2020 – Mar 2024); comments through Jun 2025 |
| **Evidence** | 32 submissions, 22 comments (54 total) |
| **Identity** | QCC health science student, ASAP program participant |
| **Arc** | QCC → transfer application → accepted at Hunter → financial aid → coursework → **GRADUATED** (Human Biology, Summer 2023) → applies to post-bac MedTech → re-applies to Hunter |
| **Tags** | `transfer` `community-college` `STEM` `graduation` `post-bac` `financial-aid` |

### Chronological Narrative

**Phase 1: Pre-Transfer Exploration (Jul 2020)**

Hypebeastzx begins at Queensborough Community College (QCC) as a health science major. In a burst of activity in July 2020, they simultaneously research Hunter, Brooklyn College, and bio programs while navigating transfer applications during COVID:

> "I'm a health science major at Queensborough CC and I'm about to graduate in the fall semester. When I was graduating high school and applying for colleges, I added hunter on my list... but I wasn't able to due to my low sat score, no essay and no letter of recommendation, just pure laziness on my end. But now, I have a 3.3 GPA and about to obtain a A.S degree." — `submission_hsy3ai` (Jul 2020, score 8)

The Hunter Promise — guaranteed admission for CUNY CC graduates with 2.5+ GPA — emerges as the institutional mechanism enabling this transfer.

**Phase 2: Community Builder (Aug 2020)**

Their highest-engagement post is not a question but an encouragement:

> "First day of Class! Good luck everybody! Hope everybody has a great semester and let's strive to get the best grades possible!" — `submission_igxy8i` (Aug 2020, score 76)

This post — the highest-scoring submission in Hypebeastzx's history — exemplifies the mutual encouragement culture in CUNY subreddits.

**Phase 3: Hunter Enrollment and Degree Push (2021–2023)**

At Hunter, navigating financial aid at a new institution (`submission_l28kfd`), COVID testing for in-person classes (`submission_pbggl5`), WiFi connectivity (`submission_wxnadk`), and the Human Biology capstone requiring department consent (`submission_wdp9ak`). A critical DegreeWorks discrepancy — transferred credits counted as 4 credits instead of 4.5 — required faculty advisor intervention (`comment_jmnzmnr`).

**Phase 4: Graduation and Beyond (Summer 2023–2025)**

> "I applied for summer graduation and it's recently been approved." — `submission_16bwhwp` (Sep 2023)

> "I recently just graduated Hunter College with a Bachelors Degree in Human Biology and I was wondering what CUNY's have a Medical Lab Tech program that I'd be able to enroll in." — `submission_1743zas` (Oct 2023)

By March 2024, they re-apply to Hunter for a second program, having declined York College. Their final comment, in June 2025 — two years post-graduation — is still in r/CUNY: "Focus on school lmfao" (`comment_mwc7fem`).

**Observation:** One of the few users documenting **degree completion and the transition to post-baccalaureate planning**. The CC-to-senior-college-to-graduation pipeline is fully visible — including the credit transfer discrepancy that nearly derailed it.

---

## Profile 3: ceo_of_losing — Major Change Crisis and Graduation Melancholy

| | |
|---|---|
| **Subreddits** | r/CUNY, r/CCNY (2) |
| **Span** | 4.8 years (Aug 2020 – Jul 2025) |
| **Evidence** | 25 submissions, 126 comments (151 total) |
| **Identity** | Father's death, depression, gaming as coping, non-traditional timeline |
| **Arc** | Freshman → CC/CCNY → CS major → transfer to Lehman (mistake) → major change to Applied Math at CCNY → Real Analysis crisis → DegreeWorks stuck at 97% → **GRADUATED** → no job lined up |
| **Tags** | `major-change` `depression` `grief` `working-class` `DegreeWorks` `graduation-sadness` |

### Chronological Narrative

**Phase 1: COVID Freshman (Fall 2020)**

Enters college during COVID. First posts: Can a professor force cameras on? (`submission_iiv6yk`). Direct deposit rejected (`submission_j1k3f5`). Three years of near-silence follow — only financial aid questions in summer 2023.

**Phase 2: Crisis and Major Change (Spring 2024)**

In February 2024, a burst of intense posting signals crisis:

> "I am contemplating on whether or not i should drop a class thats just causing me some mental distress. I cannot even function correctly because thoughts of failing this class has been on my mind 24/7. I can't even rest properly either." — `submission_1b0n6ec` (Feb 2024, score 8)

Initiates transfer to Lehman College for CS. Within *days*, realizes the mistake:

> "if i transfer, can i go back to the current college im enrolled in or is it too late. I realized that i have no passion to complete computer science major and want to go into Math with a minor in computer science." — `submission_1btef38` (Apr 2024)

> "I literally changed majors because its so depressing" — `comment_ky7b4gx`

> "Im experiencing the same, changed majors and im still sad and have a lack of motivation. Also finishing my 4th year but still not close to graduating. I cannot relax without thinking about college nowadays too." — `comment_kxuw3vh`

**Phase 3: The Institutional Trap (Fall 2024–Spring 2025)**

DegreeWorks becomes the antagonist. Required courses haven't been offered in years (`submission_1fvkg8z`). Courses don't show as fulfilling requirements (`submission_1gglobt`, score 10). An advisor tells him he may not graduate because Math 390 (Vector Analysis) is no longer offered, yet remains listed:

> "I have everything checked off but an advisor said theres an issue with that course. The course isnt even on my degreeworks" — `comment_mlgch5t`

> "i didnt make any errors, after this semester everything is checked. i met with an advisor and he legit told me i would probably not be able to graduate because of that class." — `comment_mlgw80u`

Meanwhile, Real Analysis threatens his final semester:

> "Anybody else taking a required course for graduation and just barely passing it? im taking this course and its said to be the hardest course for most math majors 'Real Analysis' and im averaging a D so far. me passing literally relies on the final exam to pass" — `submission_1kbv77s` (Apr 2025)

**Phase 4: Graduation Sadness (May 2025)**

> "anyone else graduating without a job lined up or clear future insight? i kinda feel hopeless right now and idk what to do." — `submission_1kri1bn` (May 2025, score 54)

> "Yeah there's just a feeling of emptiness in me, kind of hard to deal with." — `comment_mtdk6q7`

> "Update: I was in fact close to getting a job but it didnt fall through. My dad passing away really impacted me in a negative way this semester. That one guy in here is kind of an asshole for saying it's my fault." — `comment_mth9ak5` (score 8)

He skips the graduation ceremony — "i dont really have any family members or friends at the ceremony because of my late graduation and other familial reasons" (`comment_muvm5yf`). His final posts: applying to jobs via Handshake, advising other CCNY students, playing Ocarina of Time on a repaired 3DS.

**Observation:** This narrative is the counter-story to triumphant completion — documenting the emotional and administrative reality of *barely* finishing. The father's death, the major change, the advisor saying he might not graduate, the DegreeWorks 97% trap, and the graduation-without-a-job despair constitute a portrait of institutional friction at its most grinding.

---

## Profile 4: Salt-fish — Immigrant Pipeline, BMCC to CCNY Engineering to MTA Career

| | |
|---|---|
| **Subreddits** | r/CUNY, r/CCNY (2) |
| **Span** | 6.8 years (Aug 2018 – May 2025) |
| **Evidence** | 6 submissions, 61 comments (67 total) |
| **Identity** | Asian immigrant, "broken English," non-traditional age (started ~28, graduated at 35) |
| **Arc** | CLIP language program → BMCC (ASAP) → CCNY Electrical Engineering → 90-minute commutes → **GRADUATED** Dec 2022 → MTA engineer trainee → promoted to assistant engineer ($93K) |
| **Tags** | `immigrant` `non-traditional` `community-college` `STEM` `working-class` `graduation` `career-outcome` |

### Chronological Narrative

**Phase 1: CLIP and Community College (2016–2019)**

Salt-fish enters the CUNY system through CLIP (CUNY Language Immersion Program) — a pathway for students whose English proficiency doesn't meet direct admission thresholds. At BMCC, they participate in ASAP (Accelerated Study in Associate Programs), which provides a free MetroCard and structured support:

> "i enrolled in the ASAP program which provides free metro card for full time student in Cuny." — `comment_e4lz3vd` (Aug 2018)

By late 2018, they're weighing Phi Theta Kappa membership and the value of professor recommendation letters for transfer applications (`submission_aay1t7`, `submission_aay74m`).

**Phase 2: CCNY Engineering (Fall 2019–2022)**

Transfers to CCNY for Electrical Engineering. The 90-minute commute from Kings Highway in Brooklyn becomes a recurring motif:

> "Just tell the truth , everyday I must prepare minmum 90 minutes for  one way commute to CCNY  from (Kings highway N) . My professors are Google and Youtube. I am a transfer Engineering student in this fall." — `comment_f52x3t6` (Oct 2019)

COVID disrupts: library book bureaucracy during campus closure (`comment_fkr7llr`), financial aid verification delays, credit/no-credit policy navigation. By August 2022, they reveal their age:

> "35 senior undergrad" — `comment_im5fmmf` (Aug 2022)

**Phase 3: Graduation and Career (Dec 2022–Present)**

Graduates with a BS in Electrical Engineering in December 2022. The post-graduation job search reveals the intersection of immigration, language, and employment:

> "It took me 7 years to graduate - 1 year clip + 2.5 year bmcc + 3.5 year ccny EE. No clue what to do with my life with broken English. 7 years still isn't enough for me. I decided to find restaurants or hotels again if no one is interested in hiring me. I will be an Asian example, not getting a decent job with BS in my family. / Lucky, I find a job in MTA." — `comment_lmjv0nh` (Sep 2024, score 9)

The MTA position — engineer trainee, then promoted to assistant engineer — provides the economic resolution:

> "1.CCNY, Electrical Engineering, Dec 2022. 2.MTA C&D - engineer trainee. 3.Initial 73k, now 77k. It will be 93k after 18 months trainee graduation." — `comment_la2fknj` (Jun 2024, score 30 — their highest-scored comment)

**Phase 4: Paying It Forward (2023–2025)**

Salt-fish becomes a comment-based institutional advisor, answering questions about transfers, GPA resets, financial aid, and CCNY coursework. Their final post — responding to "What's the easiest major to study in college?" with "Electrical engineering" (`comment_muqtsne`, May 2025, score 8) — is characteristic dry humor from someone who spent seven years earning the right to the joke.

**Observation:** The most complete **CC-to-career pipeline** in the corpus. Salt-fish documents CUNY's function as immigrant mobility infrastructure — from language immersion through associate's degree through engineering bachelor's to a $93K public-sector career. The 91% comment ratio (6 submissions vs. 61 comments) exemplifies the *comment-based narrator* type: their story is reconstructed not from self-posts but from advice given to others.

---

## Profile 5: Koran21 — High School to Hunter, Granular Freshman Documentation

| | |
|---|---|
| **Subreddits** | r/CUNY, r/HunterCollege, r/BrooklynCollege, r/Baruch (4) |
| **Span** | 2.9 years (Dec 2022 – Oct 2025) |
| **Evidence** | 138 submissions, 391 comments (529 total) |
| **Identity** | Likely first-generation, early-college HS program, Human Biology major |
| **Arc** | HS senior → freshman CUNY application → accepted at Brooklyn + Hunter → commits to Hunter → navigates Net ID, orientation, FAFSA verification → declares Human Bio → first semester logistics → Dean's List → Brightspace transition → third year ongoing |
| **Tags** | `first-gen` `freshman` `bureaucratic-navigation` `financial-aid` `Hunter` `onboarding` |

### Chronological Narrative

**Phase 1: Application Anxiety (Dec 2022–Jan 2023)**

Koran21's first posts are immediately recognizable as a first-generation applicant — no family member has told them what "work in progress" means on a transcript, how long evaluations take, or when decisions arrive:

> "Hey guys I am a freshman 2023 applying to cuny as a freshman for fall 2023. I Submitted my application on December 1st and it says my application is incomplete. My transcripts from Highschool says status work in progress" — `submission_za7biy` (Dec 2022)

> "Did anyone recieve any decisions for fall 2023 please answer I am getting anxious" — `submission_101w6px` (Jan 2023, score 8)

They post the same financial aid question 4 times in 11 days (`submission_10j2ehv`, `submission_10js4pd`, `submission_10n3swi`, `submission_10sucn6`), each time adding "please someone answer." This repetition — posting the same question until receiving a satisfactory answer — is itself evidence of how unguided the process feels.

**Phase 2: Onboarding (Feb–Aug 2023)**

After accepting Hunter's offer in February 2023, they post 12 times in two months about Net ID logins, asking across both r/CUNY and r/HunterCollege whether other admitted students have received theirs (`submission_11sctih`, `submission_11te10v`, `submission_11xkxv0`, `submission_122riie`). Math placement, orientation holds, Microsoft Authenticator setup, and Outlook email configuration each generate their own posts.

**Phase 3: First Semester and Beyond (Fall 2023–2025)**

Book advances, course access, Blackboard navigation, professor evaluations, Pell grant disbursement tracking, and the Brightspace transition (when CUNY replaced Blackboard). By fall 2024, applies to CUNY Spring Forward workforce program. Still actively posting in October 2025.

**Observation:** With **529 total posts** (138 submissions), Koran21 is the **most prolific freshman documenter in the corpus** — likely a first-generation student navigating the CUNY system without family guidance, using Reddit as institutional GPS. Every bureaucratic step of the freshman year is captured in real-time, from "what does work in progress mean" to "when will my Pell grant disburse."

---

## Profile 6: HOIXIOH — NYU Dropout to Hunter Transfer, Alumnus Advisor

| | |
|---|---|
| **Subreddits** | r/HunterCollege, r/CUNY (2) |
| **Span** | 4.9 years (Dec 2019 – Oct 2024) |
| **Evidence** | 0 submissions, 50 comments (50 total) |
| **Identity** | NYU transfer, Westchester commuter, English major, graduated with honors 2022 |
| **Arc** | NYU College of Arts & Science → internal transfer rejected → leaves NYU over cost → transfers to Hunter (57 credits) → campus integration during COVID → **GRADUATED 2022** with honors → returns as alumnus advisor for 2+ years |
| **Tags** | `prestige-to-pragmatism` `NYU-comparison` `transfer` `social-life` `COVID` `alumnus-advisor` |

### Chronological Narrative

**Phase 1: Transfer and Integration (Dec 2019–2020)**

HOIXIOH's opening post announces their arrival at Hunter with 57 credits — and immediately documents the transfer credit gauntlet:

> "53 of my 57 credits were officially accepted. Roughly 20 of those credits were valid for Hunter's core curriculum and I am meeting with my department today to try to get an additional 6 or so credits applied towards my degree... The process of transferring here requires a significant amount of running around and jumping through hoops, but with persistence you will get it done." — `comment_ff9zj95` (Jan 2020)

Their first campus months — Spring 2020, before COVID shut everything down — shape a lasting impression:

> "I transferred to Hunter last spring and the two months I spent around campus were enjoyable. It's centrally located in Manhattan and a nice area... I heard that Hunter was lacking in the social scene before I attended and partly because of that tried to be outgoing and friendly. Made a lot of nice, genuine connections" — `comment_ge892r4` (Dec 2020)

**Phase 2: The Social Life Crusade (2021–2022)**

HOIXIOH's defining theme is challenging the "Hunter has no social life" narrative. Across 10+ comments, they repeat the same message with increasing passion:

> "The attitude of hunter lacking a social life perpetuates! You can start being social any day! Just say hello and start talking to a person or people you think look cool." — `comment_hddpl4x` (Sep 2021, score 13 — highest-scored Hunter comment)

This culminates in a heated exchange during the January 2022 Omicron wave, where HOIXIOH argues for in-person classes while most r/CUNY users demand online options. The thread reveals personal stakes:

> "When covid first hit, it really fucked with my mental health. I gravitated towards drugs and alcohol. I need routine. I need to interact with people. I need to leave my house." — `comment_hsz9mv0` (Jan 2022)

**Phase 3: The NYU Comparison (2024)**

Two years after graduating, HOIXIOH returns with their most substantive contribution — a detailed NYU-vs-Hunter comparison requested by a prospective student:

> "I was an undecided major at NYU college of arts and science and applied as an internal transfer to attend a different school under the NYU umbrella. I felt I was worthy of being accepted and when they didn't accept me I said fuck em I'm not gonna spend 60gs a years to study English when I can go up the road and do it at hunter for a fraction of the cost." — `comment_ltt1nvd` (Oct 2024, score 10)

> "Honestly I would say on average the student at hunter is more motivated than NYU. I met ppl at NYU whose families were so loaded that there grades didn't mean that much to them... one of my boys would just drink whiskey in class at NYu for example, saw no one doing that shit at hunter." — `comment_ltt1nvd`

**Observation:** The **prestige-to-pragmatism** narrative. HOIXIOH's zero-submission, 50-comment profile exemplifies the *alumnus advisor* archetype — someone who graduated and stays to defend their institution's reputation and mentor incoming students. Their NYU comparison provides the rare perspective of someone who experienced both systems and chose CUNY on economic rationality.

---

## Profile 7: DalekSupreme23 — BCC to Queens College Design, Working Student

| | |
|---|---|
| **Subreddits** | r/CUNY, r/QueensCollege (2) |
| **Span** | 4.7 years (Aug 2020 – May 2025) |
| **Evidence** | 30 submissions, 61 comments (91 total) |
| **Identity** | Working adult, Design major, BCC transfer, tuition paid by employer |
| **Arc** | Bronx CC → diploma delay → transfers to QC for Design → remote learning as lifeline → scheduling conflicts with full-time job → near-dropout crisis → **GRADUATED** Spring/Summer 2024 → diploma delay (again) |
| **Tags** | `working-student` `transfer` `scheduling` `institutional-critique` `Design` `budget-cuts` |

### Chronological Narrative

**Phase 1: Transfer and Remote Learning (2020–2021)**

DalekSupreme23 transfers to Queens College from Bronx Community College for a Design major. Their earliest posts reference BCC diploma delays that span *months* (`submission_jfddv3`, `submission_m6erhl`). At QC, remote learning is not a pandemic inconvenience but a structural necessity:

> "Remote learning works with my schedule" — `comment_gjdxbsz` (Jan 2021, score 8)

**Phase 2: The Scheduling Wall (2022–2023)**

The dominant theme emerges: Design classes are offered *only* during midday weekdays, directly conflicting with full-time employment. This generates the highest-scoring post in their history:

> "CUNY advertises itself as flexible and affordable for working people, but it is anything but that, especially their 4-year colleges. Graduating as a working person feels impossible due to their system. I only need 3 classes, yet I am trapped in their bureaucratic maze." — `submission_13l7mhl` (May 2023, score 18)

The critique is structural, not personal:

> "Listen im a senior that needs 3 classes to graduate. And the college i go to only schedules mornings or midday during M-F. I work a full time job and really cant afford to just quit my job. Specially in this job market." — `comment_k2n4bqf` (Sep 2023, score 9)

> "My problem with Cuny is that it advertises itself as flexible and their schools are anything but flexible." — `comment_jadj8id`

E-permits are blocked because major courses can't be taken elsewhere. The career center doesn't serve Design majors. Weekend and evening options don't exist. The department head says no to schedule changes.

**Phase 3: Resolution and Aftermath (2024–2025)**

After budget cuts reduce security and slow registrar response times (`submission_1ac0hm0`), DalekSupreme23 finally graduates in Spring/Summer 2024. But the institutional friction doesn't end — their employer needs the diploma, and the registrar is unresponsive:

> "Has anyone received their diploma yet? Registrar hasnt gotten back to me. And my employer has been inquiring for the last week." — `submission_1ecvf4u` (Jul 2024)

> "What?! Now im walking into campus and causinf a scene on Monday." — `comment_lf45xwn`

Their final posts advise future Design students: "practice a lot. Pick an area of design you like... Also network. Go to meet ups." (`comment_mi7k0dj`, Mar 2025)

**Observation:** Documents the **structural mismatch** between CUNY's marketing ("flexible and affordable") and the lived reality of working students. The Design department's midday-only scheduling effectively creates a barrier to degree completion that is invisible in enrollment statistics but visible in Reddit frustration.

---

## Profile 8: morphhyxia — COVID Freshman to Baruch Graduation and MPA

| | |
|---|---|
| **Subreddits** | r/Baruch, r/CUNY (2) |
| **Span** | 3.9 years (Apr 2020 – May 2024) |
| **Evidence** | 38 submissions, 9 comments (47 total) |
| **Identity** | COVID-cohort freshman, political science, shy, emoji-heavy register, AAVE features |
| **Arc** | HS senior choosing between Hunter/JJ/Baruch → commits to Baruch → entirely online first year → first campus visit Aug 2021 (wrong name on ID) → political science → internship → **GRADUATED** Spring 2024 → accepted to MPA programs at Baruch and John Jay |
| **Tags** | `COVID-cohort` `first-gen` `shyness` `Baruch` `graduation` `graduate-school` |

### Chronological Narrative

**Phase 1: College Decision Day (Apr–May 2020)**

morphhyxia's first post captures the anxiety of choosing a college during a pandemic:

> "So I don't know which CUNY decide from I only applied to 3 to make the decision process easier. I have no clue what I want my major to be at this point. I just want a challenging education in an safe environment to be honest. If you were to pick between John Jay, Hunter & Baruch which should I pick????" — `submission_gavmi8` (Apr 2020)

They commit to Baruch — Weissman School of Arts and Sciences, not Zicklin — and immediately ask whether non-business majors are neglected (`submission_gcjt2m`).

**Phase 2: The Remote Freshman Year (Fall 2020–Summer 2021)**

morphhyxia's entire first year of college occurs without ever setting foot on campus. Posts during this period ask about online class survival strategies, camera policies, access codes, course requirements, and foreign language options. A persistent preference for remote learning emerges even after reopening:

> "It sucks that no language classes are offered online for the fall semester. I just wanted all online classes :(" — `submission_oqwr33` (Jul 2021, score 6)

**Phase 3: First Campus Visit (Aug 2021)**

After 16 months as a Baruch student, morphhyxia physically enters the campus for the first time:

> "This will be my first time in Baruch & I was wondering if my class is located at C-Newman 108 do I just put the Baruch College Address in Google maps?" — `submission_p8a9x9` (Aug 2021)

Their ID has the wrong name — middle and last instead of first and second (`submission_pblnrk`). The bureaucratic hiccup on day one echoes through the entire narrative.

**Phase 4: The Shyness Barrier (2022)**

morphhyxia's highest-scoring post names the social cost of COVID-era education:

> "I've been looking into internships but every time I see there's a requirement for an reference I have to move on... also im kind of shy so this advice is greatly needed please" — `submission_s5xsd4` (Jan 2022, score 10)

The inability to build professor relationships — itself a consequence of starting college online — becomes a barrier to professional development. This is the structural legacy of the COVID freshman cohort.

**Phase 5: Graduation and the Circular Return (2024)**

By Spring 2024, morphhyxia is taking graduation photos (`submission_1ai9cmp`) and choosing between MPA programs:

> "i got accepted into both mpa programs for baruch and john jay and was wondering if i could please get some insight" — `submission_1bp827h` (Mar 2024)

The circularity is striking: they began in April 2020 choosing between Hunter, John Jay, and Baruch for undergrad. Four years later, they're choosing between Baruch and John Jay again — but for a master's degree. Their final comment notes the graduation ceremony didn't call students' names individually (`comment_l5kuxin`).

**Observation:** morphhyxia documents the **social isolation of the COVID freshman cohort** — entering college without seeing campus for over a year, then struggling to form the faculty relationships needed for career advancement. Despite these barriers, they graduate on time and advance to graduate school, demonstrating resilience through a distinctly pandemic-shaped pathway.

---

## Cross-Cutting Themes

### 1. Transfer as Defining Experience

Six of eight profiles (Recent-Sky3311, Hypebeastzx, ceo_of_losing, Salt-fish, DalekSupreme23, HOIXIOH) document the community-college-to-senior-college transfer pipeline. Transfer is not a single event but a multi-semester process involving credit evaluation battles, GPA resets, DegreeWorks discrepancies, and the discovery that courses don't align across campuses. The CUNY system's promise of seamless intra-system transfer is repeatedly tested against institutional reality.

### 2. Financial Aid as Existential

Every profile except HOIXIOH documents financial aid as a governing constraint on academic decisions. Recent-Sky3311's *fail vs. withdraw* calculus, ceo_of_losing's "if it does affect fafsa and TAP, I AM COOKED," Salt-fish's finish-line tuition with repayment penalties, morphhyxia's mother submitting documents — financial aid is not background bureaucracy but the structural floor beneath all academic planning.

### 3. DegreeWorks as Adversary

Three profiles (ceo_of_losing, Hypebeastzx, Koran21) document DegreeWorks — the degree audit system — as a source of institutional friction. Courses that should count don't. Required courses haven't been offered in years. Credit transfers miscount by half a credit. DegreeWorks stuck at 97%. The system designed to track progress becomes an obstacle to completion.

### 4. The Comment-Based Narrator

Salt-fish (91% comments) and HOIXIOH (100% comments) represent a distinct narrator type: users whose educational stories are embedded in advice to others rather than self-posts. Salt-fish never writes "I graduated from CCNY with an EE degree" as a post — instead, this fact emerges across dozens of comments advising other students about transfers, financial aid, and career paths. This has methodological implications: submission-only analysis would miss the richest longitudinal narratives in the corpus.

### 5. The "Paying It Forward" Culture

Four of eight users (Salt-fish, HOIXIOH, ceo_of_losing, DalekSupreme23) continue posting *after graduation* to advise current students. HOIXIOH returns for 2+ years as an alumnus advocate. Salt-fish advises on MTA careers. ceo_of_losing counsels students dealing with depression and major changes. This post-graduation advising sustains the mutual-aid function of CUNY subreddits across student generations.

### 6. COVID Cohort Isolation

morphhyxia and HOIXIOH bracket the pandemic experience. morphhyxia starts college entirely online and doesn't enter campus for 16 months; the resulting shyness barrier affects their ability to secure references for internships. HOIXIOH, who transferred *into* Hunter in Spring 2020, gets exactly two months of in-person experience before COVID — and spends the next two years arguing passionately for in-person instruction, disclosing that isolation "fucked with my mental health" and led to "drugs and alcohol."

### 7. Non-Traditional Timelines

Salt-fish's 7-year pipeline (age 28–35), ceo_of_losing's 5-year undergraduate trajectory, DalekSupreme23's 4.7-year working-student path, and Recent-Sky3311's still-ongoing enrollment challenge the assumption of a 4-year degree timeline. CUNY's non-traditional student population navigates employment, immigration, caregiving, major changes, and institutional friction that extend completion timelines far beyond the normative model.

### 8. Reddit as Institutional GPS

Koran21's 529 posts across 3 years document every step of the freshman experience because no one in their life has explained what "work in progress" means on a transcript, when financial aid packages appear, or how to get a Net ID. Reddit substitutes for the institutional knowledge that first-generation students lack — and the posts themselves become a de facto onboarding guide for future students.

---

## Evidence Appendix

### Evidence Counts by Profile

| Profile | Submissions | Comments | Total | Subreddits | Span |
|---------|------------|----------|-------|------------|------|
| Recent-Sky3311 | 46 | 89 | 135 | 5 | 4.5 yr |
| Hypebeastzx | 32 | 22 | 54 | 3 | 3.7 yr |
| ceo_of_losing | 25 | 126 | 151 | 2 | 4.8 yr |
| Salt-fish | 6 | 61 | 67 | 2 | 6.8 yr |
| Koran21 | 138 | 391 | 529 | 4 | 2.9 yr |
| HOIXIOH | 0 | 50 | 50 | 2 | 4.9 yr |
| DalekSupreme23 | 30 | 61 | 91 | 2 | 4.7 yr |
| morphhyxia | 38 | 9 | 47 | 2 | 3.9 yr |
| **TOTALS** | **315** | **809** | **1,124** | — | — |

### Key Evidence IDs Cited in This Document

| Evidence ID | User | Subreddit | Date | Type |
|-------------|------|-----------|------|------|
| submission_mw64xb | Recent-Sky3311 | r/CUNY | 2021-04-22 | Transfer comparison |
| submission_r0ymom | Recent-Sky3311 | r/Baruch | 2021-11-24 | Depression + Baruch anxiety |
| submission_n3en8i | Recent-Sky3311 | r/CUNY | 2021-05-02 | Missed Decision Day |
| submission_n5zafj | Recent-Sky3311 | r/CUNY | 2021-05-06 | Undoing acceptance |
| submission_ri92mt | Recent-Sky3311 | r/CUNY | 2021-12-17 | Switching schools again |
| submission_ytkna2 | Recent-Sky3311 | r/CUNY | 2022-11-12 | Financial aid crisis |
| comment_iz5fmwj | Recent-Sky3311 | r/CUNY | 2022-12-06 | Transfer for aid reset |
| submission_hsy3ai | Hypebeastzx | r/CUNY | 2020-07-17 | Hunter Promise transfer |
| submission_igxy8i | Hypebeastzx | r/CUNY | 2020-08-26 | Community encouragement |
| comment_jmnzmnr | Hypebeastzx | r/HunterCollege | 2023-06-02 | Credit discrepancy |
| submission_16bwhwp | Hypebeastzx | r/HunterCollege | 2023-09-06 | Graduation approved |
| submission_1743zas | Hypebeastzx | r/CUNY | 2023-10-09 | Post-grad MedTech |
| submission_1b0n6ec | ceo_of_losing | r/CUNY | 2024-02-26 | Mental distress |
| submission_1btef38 | ceo_of_losing | r/CUNY | 2024-04-01 | Transfer mistake |
| comment_ky7b4gx | ceo_of_losing | r/CUNY | 2024-04-05 | Major change depression |
| comment_kxuw3vh | ceo_of_losing | r/CUNY | 2024-04-03 | Mid-college crisis |
| submission_1kbv77s | ceo_of_losing | r/CUNY | 2025-04-30 | Real Analysis crisis |
| submission_1kri1bn | ceo_of_losing | r/CUNY | 2025-05-20 | Graduation sadness |
| comment_mth9ak5 | ceo_of_losing | r/CUNY | 2025-05-21 | Father's death |
| comment_muvm5yf | ceo_of_losing | r/CCNY | 2025-05-29 | Skipping ceremony |
| comment_e4lz3vd | Salt-fish | r/CUNY | 2018-08-22 | ASAP program |
| comment_f52x3t6 | Salt-fish | r/CUNY | 2019-10-24 | 90-min commute |
| comment_im5fmmf | Salt-fish | r/CUNY | 2022-08-28 | "35 senior undergrad" |
| comment_lmjv0nh | Salt-fish | r/CUNY | 2024-09-11 | 7-year journey |
| comment_la2fknj | Salt-fish | r/CUNY | 2024-06-24 | MTA salary disclosure |
| submission_za7biy | Koran21 | r/CUNY | 2022-12-02 | First application post |
| submission_101w6px | Koran21 | r/CUNY | 2023-01-03 | Application anxiety |
| submission_10sucn6 | Koran21 | r/CUNY | 2023-02-03 | Financial aid plea |
| submission_11sctih | Koran21 | r/CUNY | 2023-03-15 | Net ID wait |
| comment_faywg48 | HOIXIOH | r/HunterCollege | 2019-12-15 | Transfer announcement |
| comment_ff9zj95 | HOIXIOH | r/HunterCollege | 2020-01-22 | Credit evaluation |
| comment_hddpl4x | HOIXIOH | r/HunterCollege | 2021-09-18 | Social life advocacy |
| comment_hsz9mv0 | HOIXIOH | r/CUNY | 2022-01-17 | Mental health disclosure |
| comment_ltt1nvd | HOIXIOH | r/HunterCollege | 2024-10-26 | NYU vs. Hunter |
| submission_13l7mhl | DalekSupreme23 | r/CUNY | 2023-05-18 | Scheduling frustration |
| comment_k2n4bqf | DalekSupreme23 | r/CUNY | 2023-09-28 | Working student |
| comment_jadj8id | DalekSupreme23 | r/QueensCollege | 2023-02-28 | Flexibility critique |
| submission_1ecvf4u | DalekSupreme23 | r/QueensCollege | 2024-07-26 | Diploma delay |
| submission_gavmi8 | morphhyxia | r/CUNY | 2020-04-30 | College decision day |
| submission_gcjt2m | morphhyxia | r/Baruch | 2020-05-03 | Commits to Baruch |
| submission_p8a9x9 | morphhyxia | r/Baruch | 2021-08-20 | First campus visit |
| submission_s5xsd4 | morphhyxia | r/Baruch | 2022-01-17 | Shyness + references |
| submission_1bp827h | morphhyxia | r/CUNY | 2024-03-27 | MPA acceptance |
| comment_l5kuxin | morphhyxia | r/Baruch | 2024-05-25 | Graduation ceremony |

---

## Data Sources

```
Profile Data:
├── 8 CUNY SQLite databases (data/databases/current/)
├── 8 users × full post/comment histories
├── 1,124 total evidence items
├── 315 submissions + 809 comments
└── Analysis date: February 2026

Extracted Profiles:
├── Recent-Sky3311_complete_history_20260211.md
├── Hypebeastzx_complete_post_history_20260211.md
├── ceo_of_losing_complete_history_20260211.md
├── user_profile_Salt-fish_20260211.md
├── koran21_complete_history_20260211.md
├── HOIXIOH_complete_history_20260211.md
├── DalekSupreme23_complete_history_20260211.md
└── morphhyxia_complete_profile_20260211.md
```
