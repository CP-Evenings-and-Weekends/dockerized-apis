# Dockerized APIs

Dockerize a small Flask API, push it to Docker Hub, run a classmate's image, and build a frontend that talks to both.

Starter `server.py`, `requirements.txt`, and `Dockerfile` are included as a starting point.

## Prerequisites
- A [Docker Hub](https://hub.docker.com/) account (free) — you'll need one to push
- Docker Desktop running locally

## Requirements

### 1. Build and run a Flask API in a container

Use the Flask app and `Dockerfile` in this repo (or adapt your own from the lesson).  Add at least one **new** endpoint of your own that returns JSON — something more interesting than `/time`.

Build and run it locally:

```bash
docker build -t <YOUR_DOCKERHUB_USERNAME>/dockerized-api .
docker run --rm -d -p 5001:5000 <YOUR_DOCKERHUB_USERNAME>/dockerized-api
curl http://localhost:5001/your-new-endpoint
```

### 2. Push to Docker Hub

```bash
docker login
docker push <YOUR_DOCKERHUB_USERNAME>/dockerized-api
```

Share your image name (e.g. `username/dockerized-api`) and a one-line description of what your endpoint does with your cohort (Slack, in-class chat, whiteboard — whatever your class uses).

### 3. Run a classmate's image

Pick one of your classmates' images and pull/run it:

```bash
docker run --rm -d -p 5002:5000 <THEIR_USERNAME>/<THEIR_IMAGE>
curl http://localhost:5002/<their-endpoint>
```

> **Architecture note**: M-series Macs (arm64) and Intel/Linux machines (amd64) build different default images.  If your classmate's image was built on a different architecture and won't run, ask them to rebuild with `docker buildx build --platform linux/amd64,linux/arm64 -t ... --push .` (see the [`--platform` docs](https://docs.docker.com/reference/cli/docker/buildx/build/#platform)).  Flag this early so you don't burn class time on it.

### 4. Build a frontend that consumes both APIs

In `frontend/` (create it), build a small HTML/CSS/JS page that:
- Calls your own endpoint and renders the response
- Calls your classmate's endpoint and renders that too
- Shows them side by side or in a single combined view

You'll likely hit CORS issues again — fix it on the server side (`Access-Control-Allow-Origin: *`) like you did Wednesday.

## Things to think about
- The lesson's container is ~150MB with `python:3.12-slim`.  How would using `python:3.12` (the full image) compare?  How about `python:3.12-alpine`?
- Why do we need both `flask --app server run --host=0.0.0.0` *and* `-p 5001:5000`?  What does each one do?
- When you push an image, what actually gets uploaded — your source code, your Python interpreter, your operating system, all of the above?

## Stretch
- **Multi-arch build**: use `docker buildx` to produce both arm64 and amd64 versions of your image so it runs on any classmate's machine.
- Add a `.dockerignore` file so `__pycache__/`, `.git`, and other junk don't end up in your image.  Check the image size before and after.
- Read configuration (e.g. an environment variable like `GREETING`) from `os.environ` and pass it in with `docker run -e GREETING=howdy ...`.
- Set up a [GitHub Actions](https://docs.github.com/en/actions) workflow that rebuilds and pushes your image whenever you push to `main`.

> Stuck? Have a code error? Use the ["4 Before Me"](https://docs.google.com/document/d/1nseOs5oabYBKNHfwJZNAR7GlU0zkZxNagsw63AD7XV0/edit) debugging checklist to help you solve it!
