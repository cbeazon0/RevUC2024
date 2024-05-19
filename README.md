# RevUC2024
RevolutionUC Hackathon team: Logan Muhlen, Cameran Beason, Andy Au

## Lingual Links
Lingual Links is a language learning web application that incorporates user sign in authentication, flashcards, quizzes, and a server wide chat. We are happy with what we were able to accomplish in the 24-hours we had, especially since we knew little about the tools we used to create the application going into its development.

## How Lingual Links Works

#### Server Hosting Lingual Links:
Lingual Links is ran on a server being run on a Raspberry Pi. Running the application on a Raspberry Pi server was a significant accomplishment for us and allowed for the server wide chat where anyone connected to the application can chat with anyone else connected as long as they are on the same wifi.

#### Initial Login Page:
This is the page users are greeted with whenever they first access Lingual Links.
<p align="center"><img src="https://github.com/cbeazon0/RevUC2024/assets/100247149/26d0e040-f449-42ae-aa51-5c31d280b193" alt="Home Page" style="border:1px solid black; width:100%;"></p>

#### User Login:
After pressing login, the user can choose to create an account or sign in with Google or GitHub. The login/user authentication process is handled by Auth0 which we've integrated into the application. Having the user login to access the app allows for a more secure application and also allows for user data to be saved allowing them to pick up where they left off once more content is added to Lingual Links.
<p align="center"><img src="https://github.com/cbeazon0/RevUC2024/assets/100247149/921f6383-c0e6-4129-aa8b-7405fc666893" alt="Home Page" style="border:1px solid black; width:100%;"></p>

#### Home Page:
The home page houses a menu on the left where you can choose between page options, buttons in the center which have the same effect, and a profile button in the top right allowing the user to logout of their account.
<p align="center"><img src="https://github.com/cbeazon0/RevUC2024/assets/100247149/05c1cc5c-b547-4d99-8e22-ead920115255" alt="Home Page" style="border:1px solid black; width:100%;"></p>

#### Learn Page:
The learn page allows the user to access the flashcards page and the quiz page.
<p align="center"><img src="https://github.com/cbeazon0/RevUC2024/assets/100247149/6a9907cd-470f-43c5-a911-04eeb51a9706" alt="Home Page" style="border:1px solid black; width:100%;"></p>

#### Flashcards Page:
The flashcards page is where the user will practice learning words and phrases in the language of their choosing. Currently the app only supports German, however, users may choose to add or delete flashcards allowing for a completely customizable flashcard learning experience.
<p align="center"><img src="https://github.com/cbeazon0/RevUC2024/assets/100247149/d3b9255d-052b-4e54-8fa8-dc5dc5b033cc" alt="Home Page" style="border:1px solid black; width:100%;"></p>
<p align="center"><img src="https://github.com/cbeazon0/RevUC2024/assets/100247149/a6771c31-125e-4388-a9f1-16063398ea14" alt="Home Page" style="border:1px solid black; width:60%;"></p>

#### Quiz Page:
The quiz page allows the user to test their knowledge by taking quick quizzes. In future versions of Lingual Links we'd hope to add the ability to see a local leaderboard of the scores users on the server have gotten on the quiz.
<p align="center"><img src="https://github.com/cbeazon0/RevUC2024/assets/100247149/b687af98-deeb-45d1-9bfb-3e06f1765afc" alt="Home Page" style="border:1px solid black; width:100%;"></p>
<p align="center"><img src="https://github.com/cbeazon0/RevUC2024/assets/100247149/56d5844b-82a9-4a08-ab4e-4f38a6dfe0f9" alt="Home Page" style="border:1px solid black; width:100%;"></p>

#### Chat Page:
The chat page is a server wide chat where anyone on Lingual Links and connected to the wifi the server is running on can chat and interact. The chat contains time stamps and saves messages so users can see the messages even after leaving the page.
<p align="center"><img src="https://github.com/cbeazon0/RevUC2024/assets/100247149/44818ee3-eac0-4e8c-a7c0-28519a921374" alt="Home Page" style="border:1px solid black; width:100%;"></p>

## Future Enhancements
- We hope to add more languages to Lingual Links. Along with this, more flashcards and quizzes will need to be created for each language.
- We'd also like to add more UI features that provide the user with information on how to use the app to eliminate areas of possible confusion.
- Along with this, adding a server wide scoreboard to rank users by their quiz scores is another addition we'd like to make.
