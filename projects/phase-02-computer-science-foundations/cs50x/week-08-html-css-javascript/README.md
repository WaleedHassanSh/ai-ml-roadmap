# CS50x Week 8 - HTML, CSS, and JavaScript

This folder contains my CS50x Week 8 work for HTML, CSS, and JavaScript.

## Folder Structure

```text
week-08-html-css-javascript/
├── trivia/
│   ├── index.html
│   └── styles.css
│
└── homepage/
    ├── index.html
    ├── about.html
    ├── roadmap.html
    ├── projects.html
    ├── styles.css
    └── specification.txt
```

## Projects Included

### 1. Trivia

The `trivia` project is a simple interactive webpage that lets users answer trivia questions.

It includes:

- One multiple-choice question
- One free-response question
- JavaScript feedback for correct and incorrect answers
- Color changes for selected answers
- A separate CSS file for styling

Expected behavior:

- Correct multiple-choice answer turns green and shows `Correct!`
- Incorrect multiple-choice answer turns red and shows `Incorrect`
- Correct free-response answer turns the input field green and shows `Correct!`
- Incorrect free-response answer turns the input field red and shows `Incorrect`

### 2. Homepage

The `homepage` project is a personal multi-page website.

It includes:

- `index.html` as the main page
- `about.html` for personal introduction
- `roadmap.html` for learning roadmap
- `projects.html` for project highlights
- `styles.css` for custom styling
- `specification.txt` describing HTML tags, CSS properties, JavaScript usage, and Bootstrap usage

The website focuses on my computer science and AI/ML learning journey.

## Technologies Used

- HTML
- CSS
- JavaScript
- Bootstrap

## How to Run

Open the terminal inside either project folder and run:

```bash
http-server
```

Then open the provided local server link in a browser.

Example:

```bash
cd trivia
http-server
```

or:

```bash
cd homepage
http-server
```

## CS50x Requirements Covered

### Trivia

- Added a multiple-choice question
- Added at least three answer choices
- Added exactly one correct answer
- Added JavaScript logic for button feedback
- Added a free-response question
- Added JavaScript logic for input feedback

### Homepage

- Contains at least four different `.html` pages
- Includes `index.html`
- Pages are connected through navigation links
- Uses at least ten distinct HTML tags
- Uses Bootstrap
- Uses a custom `styles.css`
- Uses at least five CSS selectors
- Uses at least five CSS properties
- Uses JavaScript for interactivity
- Includes `specification.txt`

## Testing

There is no `check50` for these assignments because implementations can vary.

Manual testing should include:

- Testing correct and incorrect answers in Trivia
- Checking that all Homepage navigation links work
- Testing the website on desktop and mobile screen sizes
- Validating HTML with an HTML validator
- Confirming CSS is loaded correctly
- Confirming JavaScript interactivity works

## Submission Commands

For Trivia:

```bash
submit50 cs50/problems/2026/x/trivia
```

For Homepage:

```bash
submit50 cs50/problems/2026/x/homepage
```

## Author

Waleed Hassan Sheikh
