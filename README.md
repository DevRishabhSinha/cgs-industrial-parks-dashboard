# Indonesian Industrial Parks Dashboard

## Overview

This repository contains a web-based dashboard that visualizes industrial parks in Indonesia. It leverages:
- **Leaflet.js** for interactive mapping
- **Firebase** for hosting and contact form data handling
- **HTML/CSS/JavaScript** for the front-end
- **CSV/GeoJSON** for the main dataset(s)

The primary goal is to provide policymakers, researchers, and the public with an interactive resource to explore and contribute information on Indonesian industrial parks.

---

## Table of Contents
1. [Project Structure](#project-structure)
2. [Key Features](#key-features)
3. [Installation & Setup](#installation--setup)
4. [Firebase Configuration](#firebase-configuration)
5. [Updating and Maintaining Data](#updating-and-maintaining-data)
6. [Front-End Pages Overview](#front-end-pages-overview)
7. [Deployment to Firebase](#deployment-to-firebase)
8. [GitHub Workflow](#github-workflow)
9. [Troubleshooting & Tips](#troubleshooting--tips)
10. [Big Files Summary](#big-files-summary)
11. [Contributing](#contributing)
12. [License](#license)

---

## Project Structure

indonesian-industrial-parks-dashboard/
├── index.html                   # Main interactive map page
├── dataset.html                 # Dataset download page
├── methodology.html             # Explanation of data collection methods
├── contact.html                 # Contact form page (submissions go to Firebase)
├── contribute.html              # Google Form embeds for community contributions
├── dashboard.html               # Dashboard page (charts/graphs)
├── about.html                   # About page with general info
├── 404.html                     # Custom 404 page
├── CGS_Industrial_Parks_Sept_2024.csv # Main dataset (downloadable)
├── assets/
│   ├── css/                     # CSS styles (if any external files are used)
│   ├── js/                      # JavaScript (if any external files are used)
│   ├── data/                    # Any additional data (CSV/GeoJSON)
│   └── images/                  # Image assets
├── firebase.json                # Firebase configuration (hosting, etc.)
├── .firebaserc                  # Firebase project aliases
└── README.md                    # This documentation


- **index.html** is the core landing page with the Leaflet map and interactive layers.
- **dataset.html** handles the CSV download and records user info to Firebase before allowing download.
- **methodology.html** explains how the data was collected and processed.
- **contact.html** sends user inquiries or corrections to Firebase.
- **contribute.html** embeds Google Forms for user contributions in English/Bahasa Indonesia.
- **dashboard.html** displays charts and graphs (currently static images).

---

## Key Features

1.  **Interactive Map**
    - Leaflet.js provides panning, zooming, and clickable markers for industrial parks.
    - Pop-ups show park-specific data.

2.  **Multiple Layers**
    - Users can switch between data layers (e.g., **Status**, **Energy Source**, **Disputes**, **Foreign Involvement**).

3.  **Contact Form**
    - Submits user-provided feedback to Firebase’s Realtime Database.

4.  **Data Download**
    - A CSV file (e.g., **CGS_Industrial_Parks_Sept_2024.csv**) is available for download once users submit basic info.

5.  **Dashboard**
    - High-level charts and graphs for quick data insights.

6.  **Methodology**
    - Transparency on how data is collected, processed, and verified.

---

## Installation & Setup

### Prerequisites
- **Node.js (>=14)** and **npm**
- **Firebase CLI** (`npm install -g firebase-tools`)
- **Git** (for version control)

### Steps

1.  **Clone the repository**
    ```bash
    git clone <REPOSITORY_URL>
    cd indonesian-industrial-parks-dashboard
    ```
2.  **Install Firebase CLI** (if not already installed)
    ```bash
    npm install -g firebase-tools
    ```
3.  **Login to Firebase**
    ```bash
    firebase login
    ```
4.  **Set the Firebase project**
    If you need to point the repo to your own Firebase project, run:
    ```bash
    firebase use --add
    ```
    Select your Firebase project from the list (or create a new one).

5.  **Local Development**
    ```bash
    firebase serve
    ```
    This spins up a local server. By default, it may run on `http://localhost:5000`.

---

## Firebase Configuration
The application uses Firebase for:

- **Hosting** – All HTML files are deployed to Firebase Hosting.
- **Realtime Database** – For storing submissions from `contact.html` and `dataset.html`.

In the HTML files (e.g., `contact.html`), you’ll see the Firebase configuration:

```js
const firebaseConfig = {
  apiKey: "...",
  authDomain: "...",
  projectId: "...",
  storageBucket: "...",
  messagingSenderId: "...",
  appId: "...",
  measurementId: "..."
};
firebase.initializeApp(firebaseConfig);

Make sure these values match your Firebase project settings. If you create a new Firebase project, update these accordingly.

**Security Note:** The Realtime Database rules should be configured to allow writes from the forms while preventing unauthorized reads/writes. Set this in your Firebase Console.

## Updating and Maintaining Data

### Industrial Park Data

#### GeoJSON Data (inline)
- In `index.html`, large sections of GeoJSON may appear inline (sometimes hundreds of lines).
- If you want to update an industrial park’s attributes, search for its `Feature` within the `features` array and modify the `properties`.

#### CSV File
- The main CSV (e.g., `CGS_Industrial_Parks_Sept_2024.csv`) is available for download.
- When you update the data, ensure the CSV is updated with corresponding changes.
- If you rename the file (e.g., `CGS_Industrial_Parks_Oct_2025.csv`), also update the download link in `dataset.html`.

#### Adding or Removing Parks
- Each park is a `Feature` with `properties` (e.g., name, manager, location, coordinates).
- Keep the structure consistent if you’re manually editing the JSON or re-importing from a CSV → GeoJSON converter.

### Methodology & Documentation
- Whenever you add new fields or update existing ones, revise `methodology.html` accordingly.
- Update the “last updated” date and changelog references.

### Page Content Updates

#### Common Navigation
- The navigation bar (top) is repeated across multiple HTML files. If you add a new page, ensure each file’s nav is updated with the new link.

#### Styling & Layout
- Inline CSS is prevalent. If you need uniform styling changes across pages, consider extracting styles into a dedicated `.css` file in `assets/css`.

#### Dashboard Charts
- Currently, the charts in `dashboard.html` are static images. To update them, replace the images in `public/images/` or wherever you’ve placed them.
- If you introduce dynamic charts, you can reference a JS library (e.g., Chart.js or D3) and load data accordingly.

---

## Front-End Pages Overview

| Page             | Description                                                                        |
|------------------|------------------------------------------------------------------------------------|
| `index.html`     | Main interactive Leaflet map with layer switcher.                                  |
| `dataset.html`   | User form → on submit, logs data to Firebase → triggers CSV download.              |
| `methodology.html`| Detailed explanation of data fields, sources, and updates.                         |
| `contact.html`   | Contact form (name, email, message) stored in Realtime Database.                   |
| `contribute.html`| Embeds Google Forms in English and Bahasa to crowdsource additional dataset info.  |
| `dashboard.html` | High-level data visualization (static images as placeholders).                     |
| `about.html`     | General intro about CGS, disclaimers, references, etc.                             |
| `404.html`       | Custom error page for Firebase Hosting.                                            |

---

## Deployment to Firebase

### Build/Prep (Optional)
- This project primarily uses HTML/CSS/JS with minimal build steps. If you do use a bundler or minifier, run it before deployment.

### Firebase Hosting Configuration
- You’ll see `firebase.json` and `.firebaserc` in the root. These define hosting behavior and project alias.

### Deploy
```bash
firebase deploy --only hosting

- Once deployed, Firebase will provide a live URL (e.g., `https://your-project.web.app`).

### Custom Domains
- In Firebase Console → “Hosting” → “Custom domain,” you can connect a domain you own.
- Follow Firebase’s instructions (DNS setup, verify ownership).

---

## GitHub Workflow

### Branching Model
- **main**: Production-ready code.
- **develop**: Active development, merges from feature branches.
- **feature/**: Create feature branches for new functionalities or fixes.

### Pull Requests
1. Commit your changes to a `feature` branch.
2. Open a PR into `develop`. Request code review.
3. Merge `develop` into `main` when stable.

### CI/CD (Optional)
- You can automate tests and deploy to Firebase upon merging into `main`.
- Example `.github/workflows/deploy.yml`:
```yaml
name: Firebase Deploy
on:
  push:
    branches: [ "main" ]

jobs:
  build_and_deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: 14

      - name: Install Firebase CLI
        run: npm install -g firebase-tools

      - name: Firebase Deploy
        run: firebase deploy --token ${{ secrets.FIREBASE_TOKEN }}

## Troubleshooting & Tips

- **Map not loading:**
    - Check for console errors regarding Leaflet or missing layers.
    - Ensure the tile layer URLs are correct.
    - Verify your internet connection if using external tile servers.

- **Contact form not writing to Firebase:**
    - Double-check your Firebase Realtime Database rules (must allow write).
    - Confirm `firebaseConfig` matches your project’s credentials.

- **CSV not downloading:**
    - Check the path in `dataset.html` (the JavaScript references `CGS_Industrial_Parks_Sept_2024.csv`).
    - Ensure the file is actually in the project root or correct folder.

- **Issues with large GeoJSON:**
    - Large inline GeoJSON can be slow. Consider hosting your GeoJSON externally or in a feature layer if performance becomes problematic.

- **Offline usage:**
    - This project is not optimized for offline usage. If needed, consider a service worker or local caching strategy.

---

## Big Files Summary
Several big HTML files contain large inline data or repeated code blocks. Below is a short summary:

- **`index.html`**
    - Main page using ArcGIS API for JavaScript + Leaflet.
    - Contains large GeoJSON objects describing each industrial park.
    - Has a “layer switcher” to toggle different data fields (Status, Energy, Disputes, Foreign Involvement, etc.).
    - Animations for pop-ups (e.g., a marketing/info popup sliding in/out).

- **`dataset.html`**
    - Form that captures user info, writes to Firebase, then triggers CSV download.
    - Logic to show a “Downloading…” image while preparing the download.

- **`methodology.html`**
    - Explains how we collect data, including field definitions.
    - Large table describing each data category (Basic Info, Location, Electricity, etc.).

- **`contact.html`**
    - Simple form that writes to Firebase’s `submissions` node.

- **`dashboard.html`**
    - Displays static images for charts (placed in `public/images/` or another images folder).

By separating these functionalities, each HTML file remains relatively focused on one user flow, though they share a consistent header/nav structure.

---

## Contributing
We welcome contributions and feedback! If you spot inaccuracies, you can:

- Open a GitHub Issue describing the correction.
- Create a Pull Request with improvements (data or code).
- Submit via the app: use the Contact or Contribute page if you do not have GitHub access.
