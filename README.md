# Prometheus Example

## Prometheus

### Admin

http://localhost:9090/targets
http://localhost:9090/graph
http://localhost:9090/metrics

## Grafana

### Setup

* [OSX Installation Details](http://docs.grafana.org/installation/mac/)

Install with:
```bash
brew install grafana
```

Run with:
```bash
brew services start grafana
```

Connect to the Grafana server at http://localhost:3000 using `admin/admin`.

## Python

### Setup

```bash
pip install prometheus_client 
```