docker run --name nifi \
  -v ./certs/localhost:/opt/certs \
  -p 8443:8443 \
  -e KEYSTORE_PATH=/opt/certs/keystore.jks \
  -e KEYSTORE_TYPE=JKS \
  -e KEYSTORE_PASSWORD=mK5byii7lEvvXWwpwmCp2QhSdr+Np+Wcc1Tc3yiLsWU \
  -e TRUSTSTORE_PATH=/opt/certs/truststore.jks \
  -e TRUSTSTORE_PASSWORD=0SGy/SNSCmMkrh6R2TMj+dEjNMNmZpa2A1miWeP7API \
  -e TRUSTSTORE_TYPE=JKS \
  -e INITIAL_ADMIN_IDENTITY='cn=admin,dc=localhost' \
  -d \
  nifi
