# a culture of writers

collectively, quansight has a lot to say, but we remain relatively quiet. this document outlines process for creating and funneling content through the quansight team and brand.

the gaant below illustrates a timeline for newcomer to content delivering novel content within 2-3 weeks. with experience different parts of the process will be reduced. with a goal efficiency of 1 week for review; a success like this is predicated on experience in turning research into narrative which comes with experience in the practice of writing.

```mermaid
gantt
    title writerly experience

    section writer
    research :research 0d, 4d
    draft :draft , 3d, 5d
    pull request   :pr, after draft , 11d
    post mortem :posts, after publish, 3d
    
    section editor
    assign editor   :assign, after draft , 2d
    first reviewer     :first_review, after assign, 1d
    assign audience     :audience, after first_review, 0d
    mediator     :mediate, after first_review, 5d
    publish     :publish, after reviews, 3d
    post mortem :posts, after publish, 3d
    section audience
    review  :reviews, after first_review, 5d
```

a challenge in curated content is finding the appropriate author and editors for a specific piece. a common hinderance, and unknown unknown, is how practiced the writer is. if our writers are practicing only on curated content then they lack opportunities for improvement through practice. a necessary feature of this culture are enrichment opportunities to improve writing and communicating open source.

a culture focused on writing and sharing will have more practice communicating with others. through practice, the cumulative effort will improve our communications with clients, funders, and management.

## expectations

in content work, there are two different expectations that need to be understood:

1. the writing experience for the author(s)
2. the readerly experience of our managers and audiences

### inward, writerly expectations

the writer should be focused on writing something they are proud of. they should be sheilded from external marketing and branding considerations; their editor manages this. the writer's focus needs to be narrowed and encouraged through their struggle of turning nothing into something.

### outward, content expectations

marketing and branding are outward considerations. they are dependent on the content and climate of the audience. these considerations are independent and confusing to the inward writely perspective.

## writer experience

the writer needs a time~~dead~~line, a date for success, not a date for succeed or fail.

1. time and space to research and draft a work
2. fork the content repo
3. sync their content from hackmd to their fork
4. create a pull request to the content repository
5. fill out the pull request template
6. assign an editor
7. begin the revision



### getting started

the writer needs support in getting started, for some going from nothing to something is difficult, for others ~~@tonyfast~~ completing something is difficult.

#### a week of preparation

the first week an author is assigned to content they spend their effort researching and documenting their findings. the outcome is rough draft of the key pieces of information and content.

##### prompts

to help the authors start, we will curate a list of prompts and priorities for folks to write about.

###### sample prompts

action: add yours

* a day with xxx project
* a review of xxx
* a visualization of some data
* how to xxx
* xxx vs yyy
* redo old with new knowledge
* share your configuration settings
* diagram and describe a complex workflow
* yyyyy is cool
* a playlist for xxxxx
* your personal journeys

##### audience

in the past, content has been written for an ideal audience that is fairly distant from our developer's positions. our audience is the quansight organization, not consulting or labs, but all of quansight. authors are encouraged to write for themselves and members of our organization as their primary audiences.

with quansight as the audience we (content creators) will define where to share our work, and with whom.

#### submitting the pr

we encourage writers to draft their work in hackmd, and to explore all the syntaxes they support. once a draft is ready for feedback.

before the end of the first week, the author makes a pull request to a content repository. it is submitted through their fork of content repository. they transfer their hackmd document to their fork by [syncing the content to the repository](https://hackmd.io/c/tutorials/%2Fs%2Flink-with-github). then they submit their contribution as a pull request.

interactive, binder/qhub will be more challenging and saved for later.

#### assigning the editor

an editor is assigned as the primary reviewer to the pull request that will guide the author through the publishing process and manage the feedback.

#### initial feedback

the editor provides initial feedback and guidance for the writer. they review the form, flow, and intent of the document. 

#### getting feedback

the writer and editor iterate until it is ready to share with a sample audience.

the editor facilitates the engagement between the sample audience and the author providing project management through the editting process. the editor and audience focus on the content of the work independent of its marketing intent. they focus on the narrative, syntax, and grammar.

#### finalizing and publishing the work

a final effort blesses the work for publishing and begins to include external features like marketing and branding.

## editor experience

the editor is the crucial interface between the writer and the audience. they diffuse the blows from the critics.

editors should not be involved when there is no content, editors begin their engagement when a pull request is made for consideration.  At that time, the author is assigned an editor.


1. the editors recieve notification of new literature and chooses if they can facilitate publishing that work with that author
2. they assign themselves as a reviewer, or someone assigns them
3. they need to write the first response to the pull request with thanks and set expectations for their first review (an hour, a day). 
4. they send a second response with initial feedback on the form and content on the media.
5. the author and editor iterate until the work ready for a sample audience.
6. the editor engages a sample audience and they have a xx days to review the work
7. after sufficient review from a sufficient audience the final steps to publishing are completed.
8. the pr is closed
9. the editor advocates for this work and stays aware of relevent uses for it in consulting and labs.

### editor assignment

within (24/48) business hours, editors use the pull request to either volunteer or are assigned by a project manager to facilitate the publishing of an author's work.

#### first interaction

the editor shows thanks and appreciation for the writer's toil. the editor provides initial feedback on form, flow, and intent. 

#### writer's first edit

the writer uses the editor's critique to make a first edits.

#### engaging a sample audience

after the first tweaks, the editor engages a sample audience to provide feedback on form and syntax/grammar. they guide writers through multiple reviews during the review window. they remain available to the author for feedback and advice.

#### publishing

following a sample audience, the writer and editor do the work needed to publish and polish to post.

#### post-publishing

the editor interacts with consulting and labs to translate and groom the narrative into content for targetted audiences outside of our developer fandom.

as a post mortem, a form is filled out by the writer and editor on their experiences through the process, or 15five?? (practice writing on 15five too, can we have it all?)

### writerly process conclusion

above we discussed the process and responsibilities for the key actors: an author and an editor. all times are subjective, and can be modified to suite an author or editor's needs.

with practice and experience we can expect throughput to increase.

## culture and media

through our organization's growth we have learned to define the extent of quansight, quansight consulting and quansight labs. still the broad identity of quansight, the responsible part that balances open source and consulting, isn't apparent or easy to present.

if growth continues, and we don't define what quansight is, we may cause irrepairable damage to our culture by continuing to define differences. between quansight's consulting door and the labs door there is endless quality talent. which door to enter at quansight isn't always clear. (eg where is the combined consulting/labs blog?) 

this section proposes an intermediate place - quansight.github.io - to highlight the talent and open source lifestyles that makes us - Quansight - successful.

### quansight factory floor

quansight.github.io is proposed to be a projection of quansight through our team members and the contributions they make to open source. the consulting and labs pages represent some of the organization. the open source quansight homepage is a data driven page with our team mates open source personas and data available. 

#### the perfect is the enemy of the good

quansight.github.io demonstrates our organizations practice and processes, the things we consider to provide quality open source support.

quansight.github.io is designed to be a place for quansight culture to practice what it is and wants to be. the media portion of this page is designed to follow the submission process outlined above. members across the quansight community are welcomed to contribute writings to this media stream to share their research, art, design, community work, and management. 

the quansight community is very strong at self regulation when processes are open source and transparent; the labs blog is exemplary. quansight.github.io will be designed to be open source AF, with positive new comer experiences and community oriented meetings.

#### price of entry

writing content for quansight is about practice that creates quality literature or code. the only thing we ask for our authors is that they have a readme profile on github.

##### github readme

it is important that the writers feel good about themselves. when folks submit media to quansight.github.io we ask them to create their github readme profile, and we provide support in editting it. we'll generate better quality media if we can help folks see their own value.

these readme's will be critical for populating the team page. as a result, clients will have measurable understanding about the people they are working with.

### maturing content

the finishing touches can cost a lot of time, and in some open source time is too critical to bring out the microscope to qualify. quansight.github.io is design as a sink for fast content that can be matured to formal consulting or labs content.

the editors are interfaces between leadership that are aware of work in the pipeline. they help shepard quansight.github.io to more formal audiences.

the writer workflow can be applied to labs or consulting, the timeline will be modified. ideally, these iterations require less research and review with experienced authors are engaged, they should take less time.

## media conclusion

quansight.github.io could be a cultural beacon for quansight. it will be safe place to practice sharing and growing ideas. over time and with practice we'll all, working together, become better communicators.(and learn what commas are for)

## the work ugh

practice is important for professionals and quansight.github.io. 

### steps to agreement

1. use nikola to build `quansight.github.io`
2. pull request template setting expectations
3. accept content through pull requests on `quansight.github.io` through notebooks, markdown, and rst
4. publish content through `quansight.github.io`
5. add support for interactive content with binder

    * jupyterlite would work for a lot of things
    
5. build out other aspects of the `quansight.github.io` identity besides just the blog. add member information.
5. add sphinx (for pdf) and mkdocs (for completeness) options
7. have members of quansight create their own sites from the `quansight` unified documentation cli

    truly a culture of writing
    
6. `quansight read @Quansight @Quansight-Labs` will share all the cool stuff we've written.
7. have labs use the `quansight` documentation api
8. client projects use the `quansight` documentation api

the software serves as another substrate to practice writing documentation, issues, pull requests, and code. this software will the ease of building documentation, and fill some of the repetitive costs we sink into docs.

### measuring progress

#### consistency

quansight is consistently good, and quansight.github.io imbues that. we'll target labs' consistency of 2 posts/month, and hope for 4 posts/month early next year.

#### look good / feel good

the more people with readmes that are happy with them the better we'll feel. having personal blogs is another positive.

#### churn

churn is bad, if our process is positive and encouraging we should have repeat authors. maybe 2(?) post/year is good. we don't have a good kpi, but we want return writers. we want them to want to want to write for us.

#### mature

quansight.github.io content is referenced in, and thereby inspires, formal content for consulting and labs.

#### multi-lingual

a feature of quansight is our global and cultural reach. it would be a wonderful nice to have for there to be content in french, portguese, spanish, etc. eventually...

### unified documentation api

    quansight config
    quansight build
    quansight watch
    
alongside the efforts to improve our writerly talents we will also build software that unifies the process of building documentation and blogs. all open source projects eventually need documentation. we'll build unified documentation tools that provide suggested configurations for the best readerly and writerly experiences.

through these steps quansight.github.io, quansight members, and labs will have the same publishing systems. 

## (exercise): what are some reasons someone wouldn't share their interests?

* they don't think they have an audience for their special interests
* they don't know what to write about
* they lack confidence in their english writing
* They become (legitimately) busy on client projects
* They are between projects but that just means they have time to catch up on all of the other tasks they were asked to do in the last two months (writing is added to the bottom of the queue)


## Implementation Meeting Notes (2021-08-27)

```mermaid
gantt
    title writerly experience

    section writer
    research :research 0d, 4d
    draft :draft , 3d, 5d
    pull request   :pr, after draft , 11d
    post mortem :posts, after publish, 3d
    
    section editor
    assign editor   :assign, after draft , 2d
    first reviewer     :first_review, after assign, 1d
    assign audience     :audience, after first_review, 0d
    mediator     :mediate, after first_review, 5d
    publish     :publish, after reviews, 3d
    post mortem :posts, after publish, 3d
    section audience
    review  :reviews, after first_review, 5d
```

## writer experience

the writer needs a time~~dead~~line, a date for success, not a date for succeed or fail.

1. time and space to research and draft a work
  - Time to work (see gantt). More structure to aim for.
2. fork the content repo (provides isolation for the writer)
3. sync their content from hackmd to their fork
  - Easy for anyone to do - no action needed for us
5. create a pull request to the content repository
6. fill out the pull request template
  - Make PR template @kcpevey
8. assign an editor
  - Literally assign reviewer in the PR
10. begin the revision


## editor experience

the editor is the crucial interface between the writer and the audience. they diffuse the blows from the critics.

editors should not be involved when there is no content, editors begin their engagement when a pull request is made for consideration.  At that time, the author is assigned an editor.


1. the editors recieve notification of new literature and chooses if they can facilitate publishing that work with that author
  - Editor/reviewer will get github notification
  - Manager should also get a notification
2. they assign themselves as a reviewer, or someone assigns them
3. they need to write the first response to the pull request with thanks and set expectations for their first review (an hour, a day). 
4. they send a second response with initial feedback on the form and content on the media.
5. the author and editor iterate until the work ready for a sample audience.
6. the editor engages a sample audience and they have a xx days to review the work
7. after sufficient review from a sufficient audience the final steps to publishing are completed.
8. the pr is closed
9. the editor advocates for this work and stays aware of relevent uses for it in consulting and labs.


## What we really need
- a repo to hold stuff https://github.com/Quansight/media
- Markdown docs for contributing (requirements)
- Prompts for writing
- Meeting for writers and editors (office hours, not stand up). Tony always there. Eric always there.
- Submission process/PR template
- gh actions for publishing (nikola -> quansight.github.io)
- make meeting to continue this planning

Next steps
- test module/CLI


###### sample prompts

action: add yours

* a day with xxx project
* a review of xxx
* a visualization of some data
* how to xxx
* xxx vs yyy
* redo old with new knowledge
* share your configuration settings
* diagram and describe a complex workflow