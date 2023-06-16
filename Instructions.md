# 📚 **Library Data Analysis & Visualization Project for Small Teams** 📚

In this project, your team of 2-3 people will build upon your previous Library Management System by integrating it with a PostgreSQL database and adding data analysis and visualization capabilities. Using Python, SQL, and Matplotlib, you'll extract meaningful insights about member habits and book popularity.

**🎯 Objectives 🎯**

- Apply your knowledge of Python, SQL, and data visualization.
- Build upon your previous project to enhance your understanding of Object-Oriented Programming.
- Create a data-driven model of a Library Management System.
- Interpret data to draw meaningful insights.
- Learn how to utilize Github and Github Desktop for collaboration.
- Learn how to effectively document a project.

🧑‍🚀 Roles 👨‍🚒
You should assign these roles prior to starting. Each role has a survival guide in the survival-guides folder.

If you're in a team of three, everyone should take on one of these roles.
- **Project Leader:** This individual takes a supervisory role, coordinating all tasks and ensuring that every team member is on the right track. They handle scheduling, keep an eye on the project’s progress, and make sure the work is divided equally.
    
- **Documentation Specialist:** This role involves keeping the project well-documented. This person would take charge of writing, editing, and updating project documentation such as README files, in-code comments, and external project descriptions.
    
- **Code Quality/Git Czar:** This person is responsible for maintaining the quality of the code and managing the git repository. They review code changes, ensure adherence to coding standards and conventions, and manage branches, pull requests, and merges on the repository.

In a team of two, these roles can be adjusted so that each member takes on multiple responsibilities.

- **Project Leader/Git Czar:** This individual takes a supervisory role, coordinating all tasks and ensuring that every team member is on the right track. They handle scheduling, keep an eye on the project’s progress, and make sure the work is divided equally. In a two-member team, the Project Leader also takes on the responsibilities of the Git Czar. This role involves maintaining the quality of the code and managing the git repository. They review code changes, ensure adherence to coding standards and conventions, and manage branches, pull requests, and merges on the repository.
    
- **Documentation Specialist:** This role involves keeping the project well-documented. This person would take charge of writing, editing, and updating project documentation such as README files, in-code comments, and external project descriptions. They should also assist with code review and offer feedback on pull requests to spread the workload and keep the project moving forward efficiently.

🙌  **`git` and Github Desktop**  🙌

As this is a collaborative project, you'll be using `git` and GitHub Desktop to manage your code and work together. This section will cover the basics of how to use these tools, from setting up a repository to making changes, opening pull requests, and syncing those changes across your team.

**GitHub Desktop Installation**

1. **Download GitHub Desktop:** Go to the [GitHub Desktop download page](https://desktop.github.com/) and download the installer for your operating system.
    
2. **Install GitHub Desktop:** Run the installer and follow the prompts to install GitHub Desktop. The exact steps will depend on your operating system.
    
3. **Sign in to GitHub Desktop:** Open GitHub Desktop, click the "File" menu, and select "Options" (on Windows) or "Preferences" (on macOS). Then go to the "Accounts" tab and sign in to your GitHub account.
    
4. **Configure GitHub Desktop:** While still in the "Options" or "Preferences" window, go to the "Git" tab. Enter your name and email - these will be attached to your commits. Click "Save" when done.

**Repository Setup**

The first thing you'll need to do is set up a shared repository where your team can store and manage your project's code. One team member should create a new repository on GitHub, and then each other team member should clone that repository to their local machine using GitHub Desktop.

**The role of the Git Czar:** The Git Czar will create the initial repository and add all the team members as collaborators. 

- *Creating a Repository*: To create a new repository, go to [GitHub](https://github.com/) and click the "+" icon in the upper right corner, then select "New repository". Give your repository a name, and make sure to initialize it with a README file. You can leave the rest of the settings at their defaults, and then click "Create repository".

- *Cloning a Repository*: To clone the repository, open GitHub Desktop and go to "File > Clone repository". Select the repository you just created, choose where you want to save it on your local machine, and then click "Clone".

**Branching**

In a collaborative project, it's essential to work on separate branches for different tasks. This way, you can avoid conflicts and keep your code organized.

**Everyone's Responsibility:** All team members are responsible for creating and managing their own branches. 

- *Creating a Branch*: To create a branch, click on the "Current branch" tab in GitHub Desktop and then click the "New" button. Give your branch a descriptive name related to the task you're working on, and then click "Create Branch".

- *Switching Between Branches*: To switch between branches, simply click on the "Current branch" tab and then select the branch you want to switch to.

**Making Changes and Committing**

Whenever you make changes to your code, you should commit those changes to your branch. This records a snapshot of your code at that point in time, which you can refer back to or revert to if necessary.

**Everyone's Responsibility:** All team members are responsible for making changes to their code and committing those changes.

- *Staging Changes*: To stage changes, go to the "Changes" tab in GitHub Desktop. You'll see a list of files that have been changed, added, or deleted. Check the box next to each file you want to stage for commit.

- *Committing Changes*: Once you've staged your changes, write a descriptive commit message in the box at the bottom of the GitHub Desktop window. Then click the "Commit to [branch]" button to commit your changes.

**Pull Requests**

Instead of immediately merging branches, you should use pull requests. This gives your team the chance to review changes before they're integrated into the main codebase.

**Everyone's Responsibility:** All team members are responsible for opening pull requests for their own branches.

- *Opening a Pull Request*: To open a pull request, first push your branch to GitHub. Then, go to your repository on GitHub, select your branch, and click the "Pull request" button. Give your pull request a title and description, then click "Create pull request".

**The role of the Git Czar:** The Git Czar is responsible for reviewing and merging pull requests. They should look over the changes, ensure they align with the project's requirements and code standards, and handle any merge conflicts.

- *Reviewing and Merging a Pull Request*: To review a pull request, go to the "Pull requests" tab in your repository on GitHub. Select the pull request you want to review, and you'll see the changes that have been proposed. If everything looks good, click the "Merge pull request" button to integrate the changes into your main branch.

This is the basic workflow you'll be using with `git` and GitHub Desktop to collaborate on your project. Remember, communication is key - make sure to discuss with your team who's working on what, when to merge branches, and any other important decisions related to your code. Happy coding! 🚀👨‍💻👩‍💻

**👨‍💻 Pair Programming 👩‍💻**

Pair programming is a method where two developers work together on one computer. In this project, we'll use pair programming for some tasks. 

You'll be doing one of two jobs: the 'driver' or the 'navigator'. 

The 'driver' is the person who types out the code. Think of them as the person actually steering the car, pressing the gas pedal, and operating the brakes. They handle the hands-on part of coding.

The 'navigator', on the other hand, watches the code as it's written. They're like the co-pilot, suggesting where to go and pointing out possible issues. They think about the overall plan of the work.

To make sure both of you get to experience both roles and work together effectively, we strongly advise that you swap jobs often.

Even though it might seem like this way of working is slower, it often ends up being quicker. Two heads are better than one, and having two people looking at the same problem can lead to solutions being found more quickly.

You should also utilize pair programming whenever someone is stuck or struggling on their task. Remember, above all else, this needs to be a team effort, no one should get left behind.

**👨‍💻 Your Tasks 👩‍💻**

Your Enhanced Library Management System should involve the following:

1. **Database Integration:** As a team, you'll set up a PostgreSQL server using Railway and integrate it with your existing library system. 

	- Utilizing pair programming, two team members will create a new `Database` class to manage all interactions with your database. This class should contain methods for connecting to the database, executing queries, and fetching results. Your existing classes (`Book`, `Member`, and `Library`) will then utilize the `Database` class for all necessary database operations. So it should be able to connect to the database, and send queries to the database. 
		- When setting up your database connection make sure to reference this quick guide.
	- If your team has a third member, this person should start on the project documentation by filling in the sections within the README file, detailing the project setup, functionality, and features.


2. ***Library Operability***: Using the newly created `Database` class, improve each of the methods in your `Member` and `Library` classes by having them utilize the database. 

	- If your team has 3 members, 2 people should pair program the methods in `Library` class while the third person takes on the methods in the `Book` class. 
	- For example, when borrowing a book, you should add an entry to the borrowed_books table without a return date. 

3. **Data Analysis:** Using the `Database` class, create methods in your `Book`, `Member`, and `Library` classes to derive the following insights using SQL queries:

- The number of books borrowed per month. 
- The number of active members per month.
- The number of books borrowed per category.
- The top 3 most frequently borrowed books.
- The number of books borrowed by the top 3 active members.
- The most active member.

Each team member should pick two queries, implement them into the relevant class (`Book`, `Member`, or `Library`), and perform data analysis. This way, the tasks are evenly distributed, and the classes can be enhanced in parallel.

4. **Data Visualization:** Each team member will then use Matplotlib to visualize one of their findings from their respective data analysis query. The relevant classes (`Book`, `Member`, or `Library`) should be further extended to include methods that produce these visualizations.

- The "number of books borrowed per month" can be visualized using a line graph.
- For "the number of active members per month", a similar line graph can be drawn.
- The "number of books borrowed per category" could be visualized using a bar chart.
- The "most frequently borrowed book" can be presented with a histogram.
- The "number of books borrowed by the top 3 active members" can be represented using a bar chart.
- The "most active member" can be represented by a bar chart.

4. **Code Quality:** Each team member should strive for clean, well-structured, and easy to read code. Proper naming conventions should be followed, and the code should be well-documented with comments. Additionally, one team member should take on the role of "Code Quality/Git Czar". This person will be responsible for ensuring that the team's code adheres to these standards and that it is well managed within your version control system.

5. **Error Handling:** As a team, you should consider potential error scenarios and handle them gracefully. For example, what happens if there are no books in a certain category or if there are no active members in a particular month? The `Book`, `Member`, and `Library` classes should be extended to handle these potential errors.

6. **Documentation:** Lastly, your README file should be finalized. This document should detail the setup process, how to interact with your system, the findings from the data analysis, and how to interpret the visualizations. If your team has a third member, this person should take the lead on this task, with input from the rest of the team.
  

**📋 Rubric 📋**

Certainly! Here's an example of a Markdown table that includes the criteria you provided:

| Criteria                | Description                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------|
| Data Collection         | Have you appropriately tracked and stored necessary data? 📊                                     |
| Data Analysis           | Have you correctly analyzed the data to find popular books, peak times, active members, and popular categories? 🕵️‍♀️ |
| Data Visualization      | Have you displayed the data analysis results in a clear and intuitive way using Matplotlib? 📈     |
| Code Quality            | Is your code clean, well-structured, and easy to read? Are you following good naming conventions? Is your code properly documented with comments? 📖 |
| Error Handling          | Does your system handle potential errors gracefully? ⚠️                                          |
| Presentation            | Are you able to clearly explain your code and the insights you've drawn from the data? 🎤         |

**🏁 Submission 🏁**

Submit a Python (.py) file containing your solution and a report (.txt or .docx) that explains the insights you've drawn from the data. You're solution should generate photos of the charts and store them in a folder.


1. Set up a PostgreSQL server using Railway.
2. Use the included seeder script to populate your database.
2. Connect your existing library system and create an additional class to make it easier to interact with your database. 
4. Modify your classes as needed for additional data tracking.
5. Implement methods for data analysis and generating a text report.
6. Using the implemented methods and Matplotlib, generate charts to visualize your findings. Output the charts to image files and store them in a folder.
7. Test your project thoroughly and ensure you can draw meaningful insights from your data.
  

Good luck, and have fun enhancing your Library Management System! 🚀👨‍💻👩‍💻



### Database Schema

**members**

  

| Field | Type |

|------------|-------------|

| member_id | SERIAL PRIMARY KEY |

| name | VARCHAR(255)|

| join_date | TIMESTAMP |

  

**books**

  

| Field | Type |

|-----------|-------------|

| book_id | SERIAL PRIMARY KEY |

| title | VARCHAR(255)|

| author | VARCHAR(255)|

| category | VARCHAR(255)|

| status | VARCHAR(255)|

  

**borrowed_books**

  

| Field | Type |

|---------------|------|

| transaction_id | SERIAL PRIMARY KEY |

| member_id | INT REFERENCES members(member_id) |

| book_id | INT REFERENCES books(book_id) |

| borrow_date | TIMESTAMP |

| return_date | TIMESTAMP |

