# ubuntu-core-test
Test of snap development for Ubuntu Core
Attempt to integrate gpio telemetry to gcloud iot core mqtt bridge

Before build:
Make sure snap/hooks/ files have sufficient access rights

After snap install:
snap connect iot-labs-uc-test:gpio-memory-control :gpio-memory-control
snap connect iot-labs-uc-test:home :home
snap set iot-labs-uc-test credentials_path=/home/haakonsbakken/pubsubcredentials.json project_id=appliedautonomybackend topic_name=test-iot-topic