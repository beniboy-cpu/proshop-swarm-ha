# ProShop Swarm — E-commerce Haute Disponibilité

E-commerce Flask + PostgreSQL sur un cluster **Docker Swarm 3 nœuds** (haute disponibilité) :

## Fonctionnalités

- 3 replicas Flask (load-balancing automatique)
- PostgreSQL persistant (volume sur node1)
- Monitoring Grafana + Prometheus + cAdvisor
- Registry local + Portainer pour gestion web

---

## Démo

### 🛒 Site en live
![Site live](screenshots/site.png)

### 🖥️ Cluster Portainer
![Cluster Portainer](screenshots/cluster.png)

### 📊 Monitoring Grafana
![Monitoring Grafana](screenshots/grafana.png)

### 🧰 Podman registry (optionnel)
![Podman](screenshots/podman.png)

---

## 🚀 Lancement rapide (sur Ubuntu VMs)

```bash
docker swarm init --advertise-addr 192.168.137.60
docker stack deploy -c docker-compose.yml proshop
