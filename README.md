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

    # install vercel globally on your machine
    npm i -g vercel

    # deploy
    vercel

Follow on-screen prompts from vercel:

    blah
    blah
    blah
