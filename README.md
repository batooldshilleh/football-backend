
# 🏆 Football API Backend

A lightweight Flask-based backend that fetches football data from [API-SPORTS](https://www.api-football.com/). It provides endpoints to get league information, teams, and matches. The project is containerized using Docker, deployed via Kubernetes, and integrated with a CI/CD pipeline powered by Jenkins and GitHub Webhooks.

---

## 📑 Table of Contents

- [🎯 Features](#-features)
- [🏗️ Architecture](#-architecture)
- [🛠️ Tools & Technologies](#-tools--technologies)
- [🔁 GitHub Webhook + Jenkins](#-github-webhook--jenkins)
- [⚙️ Local Setup](#️-local-setup)
- [🐳 Docker & Kubernetes](#-docker--kubernetes)
- [🧪 Testing](#-testing)
- [📡 API Endpoints](#-api-endpoints)

---

## 🎯 Features

- Retrieve teams and matches by league and season.
- Fetch detailed league info.
- Automated deployment via GitHub Webhook and Jenkins.
- Dockerized and Kubernetes-ready.
- Unit tested using `pytest`.

---

## 🏗️ Architecture

```

\[ GitHub ] → \[ Jenkins ] → \[ Docker Image ] → \[ DockerHub ] → \[ Kubernetes Cluster ]
↘ Webhook                      ↘ Publish            ↘ Deploy (via kubectl)

````

- Flask handles API routing and logic.
- Jenkins pulls the code on push.
- Docker builds and tests the image.
- DockerHub hosts the final image.
- Kubernetes handles deployment in the cluster.

---

## 🛠️ Tools & Technologies

| Tool/Tech       | Purpose                                |
|-----------------|----------------------------------------|
| Flask           | Backend framework                      |
| requests        | External API communication             |
| Docker          | Containerization                       |
| Kubernetes      | Deployment and orchestration           |
| Jenkins         | CI/CD pipeline                         |
| GitHub Webhook  | Trigger build on every push            |
| pytest          | Unit testing                           |
| dotenv          | Environment configuration              |

---

## 🔁 GitHub Webhook + Jenkins

- A webhook is configured in the GitHub repo to notify Jenkins of any new push.
- Jenkinsfile contains:
  - Checkout source code
  - Build Docker image
  - Run unit tests
  - Push to DockerHub
  - Deploy to Kubernetes via `kubectl`

---

## ⚙️ Local Setup

1. **Clone the Repository**
```bash
git clone https://github.com/batooldshilleh/football-backend.git
cd football-backend/backend
````

2. **Create `.env` file**

```env
API_KEY=your_api_key_here
```

3. **Install Requirements**

```bash
pip install -r requirements.txt
```

4. **Run the App**

```bash
python app.py
```

> API will run at: `http://localhost:7000`

---

## 🐳 Docker & Kubernetes

### Docker

1. **Build Image**

```bash
docker build -t batoolsh2001/my-backend:latest .
```

2. **Run Container**

```bash
docker run -p 7000:7000 --env-file .env batoolsh2001/my-backend:latest
```

### Kubernetes

1. **Apply Deployment & Service**

```bash
kubectl apply -f backend-deployment.yaml
```

2. **Expose Locally (Optional)**

```bash
kubectl port-forward service/backend-service 7000:7000
```

---

## 🧪 Testing

Run unit tests using:

```bash
pytest -v test_app.py
```

### Sample Tests:

* ✅ `/league-teams?league=39`
* ✅ `/league-matches?league=39`
* ✅ `/league-info?league=39`
* ❌ Missing `league` param returns 400 error

---

## 📡 API Endpoints

| Endpoint                                                | Description                                   |
| ------------------------------------------------------- | --------------------------------------------- |
| `/league-teams?league=ID&season=YEAR`                   | Returns teams of a specific league            |
| `/league-matches?league=ID&season=YEAR&date=YYYY-MM-DD` | Returns fixtures, optionally filtered by date |
| `/league-info?league=ID`                                | Returns league details                        |

> Example:

```bash
curl "http://localhost:7000/league-teams?league=39"
```

---

## 📬 Contact

* GitHub: [batooldshilleh/football-backend](https://github.com/batooldshilleh/football-backend)

---

## 📝 Notes

* Make sure your `.env` file includes a valid API key.
* The current setup uses `ClusterIP`, so either use port-forwarding or add an Ingress controller to expose your service.




