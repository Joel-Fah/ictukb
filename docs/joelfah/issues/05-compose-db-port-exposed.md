# docker-compose publishes PostgreSQL on all interfaces with the default password

## What happens

`docker/docker-compose.yml` maps the `db` service as `"5432:5432"`, which Docker binds to `0.0.0.0` and `[::]`.
The credentials are the fixed `ictkb` / `ictkb`. After `docker compose -f docker/docker-compose.yml up -d db`:

```
docker-db-1   pgvector/pgvector:pg16   ...   0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp
```

On a laptop on campus Wi-Fi, anyone on the same network can connect with the documented password. Docker writes
its own iptables rules, so a host firewall such as `ufw` does not block the published port.

Little private data is at risk (the content is public), but the database also holds the `api_keys` table (hashes) and
is writable, so someone could alter a local index or the data used for testing.

## Proposal

One-line change (needs the infrastructure owner's approval, since it's under `docker/`):

```yaml
    ports:
      - "127.0.0.1:5432:5432"
```

Nothing else changes for local use: the tools connect through `localhost`, and the `api`/`pipeline` services reach the
database over the compose network (`db:5432`), not through the published port.
