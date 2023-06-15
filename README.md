## **CLEARANCE**
***
#### _Planet Earth's Best Verified Database of Documented UAP/UFO Encounters_

![Image](https://static01.nyt.com/images/2017/12/19/autossell/STILL2/STILL2-articleLarge-v2.gif?quality=75&auto=webp&disable=upscale)

#### Written by Brian Cherchiglia, Nicholas Emmons & Platin Syla
#### Published by  **[~~CLASSIFIED~~]** 
#### Created on June 15, 2023
***
***

#### [**GitHub**](https://github.com/cherch173/clearance)

#### [**Trello Board**]()
***
***
### _**Description**_
Years ago, we would have scoffed at the idea too. 

However...in light of current events, validated, vetted testimonials and declassified government cables & documents _and_ confirmed UAP Footage captured by high-ranking military officials (well-regarded by many as the most trusted observers in the world) it's become clear that in this era of true UFO/UAP/NHI Disclosure: we need a refined, **organized**, database of all proven UAP Encounters across the globe.

**CLEARANCE** is that service.

Split into individual CASES -- we at _Clearance_ have devised a simple, accesible, user-friendly web based application to handle the maelstrom of information that's come our way since Leslie Kean & Ralph Blumenthal first published their article in the _New York Times_ in 2017 confirming the existence of AATIP (the _Advanced Aerospace Threat Identification Program_) within the United States' Department of Defense within the Pentagon.

Turns out the truth _is_ out there and well, it'd sure be a lot easier to access if it was a bit more user-friendly...
***
![Image](https://media-cldnry.s-nbcnews.com/image/upload/t_nbcnews-fp-1024-512,f_auto,q_auto:best/newscms/2021_20/3475469/210517-ufo-corbell-2x1-mn-1540.gif)

### _**Concept**_
Using **Django** as our framework and **Python** as our language -- we can structure our application to just a few Data MODELS.

We'll also be utilizing the built-in styling of **Materialize** to implement **CLASS BASED VIEWS** -- extending our BASE TEMPLATE throughout our application creating a comfortable, easily transferable design.

The **database** will be stored and accessed using **PostgreSQL**.

For **Images**, we'll store them using an S3 Bucket in AWS (Amazon Web Services), which we'll also utilize for our **User Authentication**.

***
***
### _**Technologies**_
- Python
- PostgreSQL
- Django
- S3 + AWS
***
***
![Image](https://pbs.twimg.com/media/FnOMaGTaMAY3I7K?format=jpg&name=4096x4096)
## _**Getting Started**_
To talk about (and witness) difficult things, simplicity and accessibility is crucial.

The design element has to provide a sense of comfort, and will largely be homogenous thanks to **Materialize**.

We'll stick to _Business Logic_ and keep our MODELS fairly light.

Each Model will have the following criteria:

**CASES**
- name = charField()
- location = charField()
- date = dateField()
- description = textField()
- declassified = booleanField()
- foia_link = charField()

**NEWS** (One to Many)
- I = Internet Only
- N = Newspaper
- P = Press Conference
- T = Television

**TESTIMONIALS (Witnesses)** (Many to Many)
- date = dateField()
- name = charField()
- location = charField()
- comment = textField()

Each MODEL will have CRUD capabilities.

We'll also utililiza SHOW Functionality to bring an INDEX & DETAILS view for each CASE.

**Images, Authentication & Authorization** will 




### _**Credits**_
#### **IMAGES USED**
##### USS Nimitz Tic Tac UAP Gif -- [New York Times](https://static01.nyt.com/images/2017/12/19/autossell/STILL2/STILL2-articleLarge-v2.gif?quality=75&auto=webp&disable=upscale)
##### USS Omaha UAP Gif -- [NBC News](https://static01.nyt.com/images/2017/12/19/autossell/STILL2/STILL2-articleLarge-v2.gif?quality=75&auto=webp&disable=upscale)