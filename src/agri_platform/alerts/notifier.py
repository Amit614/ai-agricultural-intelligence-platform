class Notifier:
    def send(self,alert):
        return f"Queued {alert.channel}: {alert.message}"
