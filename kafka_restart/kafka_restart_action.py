from robusta.api import *

# class BashParams(ActionParams):
#    bash_command: str

@action
def kafka_restart_action(alert: PrometheusKubernetesAlert):
    print(f"The alert {alert.alert_name} fired on pod {alert.pod.metadata.name}")
    print(f"The pod has these processes:", alert.pod.exec("ps aux"))
    print(f"The pod has {len(alert.pod.spec.containers)} containers")