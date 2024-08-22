# fallacy-finder

Submit text and learn what fallacies it contains! Built using ChatGPT.

## Run locally

    # activate python virtual env
    python3 -m venv venv
    . venv/bin/activate

    # install dependencies
    pip3 install -r requirements.txt

    # setup flask to run as a development environment
    export FLASK_APP=index.py
    export FLASK_ENV=development

    # run the flask server
    flask run --reload


## Deploy with Vercel

These steps are optional. Every push to the main branch will automatically trigger a Vercel prod deployment.

    # install vercel globally on your machine
    npm i -g vercel

    # deploy
    vercel --prod


## Initial Vercel project setup (should not need to do this again)

Initialize Vercel

    vercel

Follow on-screen prompts from vercel:

    ? Set up and deploy “~/Code/fallacy-finder”? yes
    ? Which scope do you want to deploy to? cmonaghan's projects
    ? Link to existing project? no
    ? What’s your project’s name? fallacy-finder
    ? In which directory is your code located? ./
    Local settings detected in vercel.json:
    No framework detected. Default Project Settings:
    - Build Command: `npm run vercel-build` or `npm run build`
    - Development Command: None
    - Install Command: `yarn install`, `pnpm install`, `npm install`, or `bun install`
    - Output Directory: `public` if it exists, or `.`
    ? Want to modify these settings? no

It will return some links.

Disable authentication requirement in Settings > Deployment Protection > Vercel Authentication

### Connect to Github

From the Vercel project settings page, connect the git repository.
You'll need to follow the link to Github to enable Vercel to access the repo.

## Helpful resources

- [How to deploy a python flask app to vercel](https://dev.to/andrewbaisden/how-to-deploy-a-python-flask-app-to-vercel-2o5k)
