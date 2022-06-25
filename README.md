
> Em construção

Esse repositório é um projeto de estudo para automatização de fluxos do NiFi utilizando as APIs.

### Build Image for Mac M1
Como estou desenvolvendo em um Mac M1, precisei realizar o build da imagem oficial com a plataforma arm64.

```sh
docker buildx build --platform linux/arm64 --tag nifi --output type=docker .
```

### Create certificate
```sh
./tls-toolkit.sh standalone -n localhost -C 'CN=admin,OU=NiFi' --subjectAlternativeNames 'localhost,0.0.0.0'
```
