# Automated Book Publication Workflow  
**Your AI-Powered Book Buddy—Making Book Magic Happen!**  

Hey everyone! 👋 Check out my *Automated Book Publication Workflow*—a super cool project that grabs book content from the web, jazzes it up with AI, lets me tweak it, and keeps everything organized. It’s like having a creative sidekick for book lovers or anyone curious about AI. Stick around—I’ll break it down for you in a way that’s easy to follow and fun to read!  

---

## What’s This Project All About?  
Imagine you’ve got a book chapter online, and you want to remix it into something fresh and awesome. That’s where this project comes in! Here’s what it does:  
- **Grabs Stuff**: Pulls text and a screenshot from a webpage.  
- **Gets Creative**: Uses AI to rewrite and summarize it.  
- **Lets Me Edit**: I can jump in and add my own flair.  
- **Saves It**: Stores everything neatly so I can find it later.  

It’s a simple way to play with AI and books—perfect for anyone who loves a good story or tech tinkering!  

---

## How’s It Organized? (Folder Structure)  
I’ve kept things nice and tidy so you can find everything easily. Here’s the layout:  

```bash
book_publication_workflow/
├── data/                 # Where all the cool stuff ends up
│   ├── raw/              # The untouched text straight from the web
│   ├── processed/        # AI’s remixed and reviewed versions
│   └── screenshots/      # Pictures of the webpage
├── src/                  # The code that makes it all happen
│   ├── fetch_content.py  # Grabs the text and screenshot
│   ├── ai_process.py     # AI does its rewrite and review magic
│   ├── storage.py        # Saves everything in a database
│   └── search.py         # Finds stuff I saved earlier
├── requirements.txt      # List of tools the project needs
├── main.py               # The one file to rule them all
└── README.md             # Hey, that’s this file!
```

Each folder has a job, and together they make the project run smoothly!  

---

## What Goes In and Comes Out? (Inputs & Outputs)  
Let’s talk about what I feed into this project and what it spits out—it’s pretty straightforward!  

### Input  
- **Just a Web Link!**: I give it a URL to a book chapter. For example:  
  `https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1`  
  That’s it! One link, and the project takes it from there.  

### Outputs  
Here’s what you’ll find after the project does its thing:  
- **`data/raw/chapter_1.txt`**:  
  - **What It Is**: The exact text copied from the webpage, no changes.  
  - **Why It’s There**: It’s the starting point—like the raw dough before baking!  
- **`data/processed/spun_content.txt`**:  
  - **What It Is**: The AI’s fun rewrite of the text in its own words.  
  - **Why It’s There**: It’s like a fresh take on the story—new vibes, same heart!  
- **`data/processed/reviewed_content.txt`**:  
  - **What It Is**: A short summary or review of the rewritten text, also by AI.  
  - **Why It’s There**: Gives me a quick rundown of what’s new—super handy!  
- **`data/screenshots/chapter_1.png`**:  
  - **What It Is**: A picture of the webpage I started with.  
  - **Why It’s There**: A cool visual reminder of where it all began!  
- **Stored Stuff**:  
  - **What It Is**: The final version (after my edits) saved in a database called ChromaDB.  
  - **Why It’s There**: So I can search and pull it up anytime—like a digital bookshelf!  

---

## How to Set It Up and Run It  
Want to try it yourself? Here’s how to get going:  

1. **Make a Home for It**:  
   ```bash
   mkdir book_publication_workflow
   cd book_publication_workflow
   ```

2. **Set Up a Safe Space**:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows
   ```

3. **Grab the Tools**:  
   - Save the `requirements.txt` file, then run:  
     ```bash
     pip install -r requirements.txt
     playwright install
     ```

4. **Build the Folders**:  
   ```bash
   mkdir data data/raw data/processed data/screenshots src
   ```

5. **Add the Code**:  
   - Drop the script files into their spots (check the structure above).  

6. **Hit Play**:  
   - Run `python main.py`, and watch it work! It’ll:  
     - Grab the content.  
     - Let AI remix it tally.  
     - Ask if I want to edit (I can skip with Enter).  
     - Save it all for later.  

---

## Why This Rocks  
- **AI + You**: It’s a team-up between tech and your creativity!  
- **Super Simple**: One command, and boom—it’s done.  
- **Fun for All**: Whether you’re into books, AI, or both, it’s a blast to explore!  

Thanks for checking it out! I had so much fun making this, and I hope you enjoy it too. Let me know what you think—I’m all ears! 🎉