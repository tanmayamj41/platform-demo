import sys

service = sys.argv[1]
image = sys.argv[2]
replicas = sys.argv[3]

template = f"""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {service}
spec:
  replicas: {replicas}
  selector:
    matchLabels:
      app: {service}
  template:
    metadata:
      labels:
        app: {service}
    spec:
      containers:
      - name: {service}
        image: {image}
        ports:
        - containerPort: 5000
"""

with open("generated-deployment.yaml", "w") as f:
    f.write(template)

print("Deployment YAML generated successfully!")
